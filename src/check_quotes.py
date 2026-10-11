"""Fetch every cited URL and check that each quote really appears on the page.

Why this exists: WebFetch in Claude Code answers through a small model, so a quote an agent calls
"verbatim" may be a paraphrase. This script looks at the real page text instead.

For each source in each staging record:
  found       fuzzy match >= 90 (quote is on the page)
  weak        75-89 (probably there, small differences: punctuation, diacritics, line breaks)
  missing     < 75 (page loaded but the quote is not there)
  unreachable fetch failed, robots.txt disallows, or no text could be extracted (JS-only page, scan)

Pages are cached in data/raw/<record id>/ (gitignored) so reruns are cheap.

Usage:
    python -m src.check_quotes                  # all records in data/records/staging/
    python -m src.check_quotes path/a.json ...  # specific records
    python -m src.check_quotes --refetch        # ignore the page cache
"""

import hashlib
import io
import json
import re
import sys
import threading
import time
import unicodedata
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse
from urllib.robotparser import RobotFileParser

import requests
from bs4 import BeautifulSoup
from rapidfuzz import fuzz

from src.config import QUOTE_CHECKS_DIR, RAW_DIR, STAGING_DIR
from src.validate import iter_sources

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/126.0 Safari/537.36 investor-db-quote-check")
ROBOTS_AGENT = "investor-db-quote-check"
TIMEOUT = 20
FOUND, WEAK = 90, 75
MIN_TEXT_CHARS = 200
DOMAIN_DELAY_S = 1.0

_QUOTES = {"‘": "'", "’": "'", "‚": "'", "‛": "'", "“": '"', "”": '"',
           "„": '"', "«": '"', "»": '"', "–": "-", "—": "-", "−": "-",
           " ": " ", " ": " ", " ": " ", "​": ""}


def normalize(text: str) -> str:
    text = unicodedata.normalize("NFKC", text or "")
    for a, b in _QUOTES.items():
        text = text.replace(a, b)
    text = text.casefold()
    return re.sub(r"\s+", " ", text).strip()


def quote_parts(quote: str) -> list[str]:
    """A quote may join fragments with an ellipsis; each fragment must be on the page."""
    parts = re.split(r"\s*(?:\.\.\.|…|\[\.\.\.\]|\[…\])\s*", quote)
    return [p for p in (normalize(p) for p in parts) if len(p) >= 3]


def score_quote(quote: str, texts: list[str]) -> int:
    parts = quote_parts(quote)
    if not parts or not any(texts):
        return 0
    best = 0
    for text in texts:
        if not text:
            continue
        s = min(fuzz.partial_ratio(p, text) for p in parts)
        best = max(best, s)
    return int(round(best))


def classify(score: int) -> str:
    return "found" if score >= FOUND else "weak" if score >= WEAK else "missing"


def html_texts(html: str) -> list[str]:
    """Two independent extractions: main-content text and full visible text; scoring takes the best."""
    texts = []
    try:
        import trafilatura

        main = trafilatura.extract(html, include_comments=False, include_tables=True, favor_recall=True)
        texts.append(normalize(main or ""))
    except Exception:  # noqa: BLE001 - extraction failure just means one text fewer
        texts.append("")
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()
    texts.append(normalize(soup.get_text(" ")))
    # meta descriptions often carry the investor's one-line self-description
    metas = [m.get("content", "") for m in soup.find_all("meta") if m.get("content")]
    texts.append(normalize(" ".join(metas)))
    return texts


def pdf_texts(data: bytes) -> list[str]:
    from pypdf import PdfReader

    reader = PdfReader(io.BytesIO(data))
    return [normalize(" ".join((p.extract_text() or "") for p in reader.pages))]


class Fetcher:
    def __init__(self, cache_dir: Path, refetch: bool = False):
        self.cache_dir = cache_dir
        self.refetch = refetch
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": UA, "Accept-Language": "cs,en;q=0.8"})
        self._robots: dict[str, RobotFileParser | None] = {}
        self._lock = threading.Lock()

    def _robots_for(self, url: str) -> RobotFileParser | None:
        p = urlparse(url)
        base = f"{p.scheme}://{p.netloc}"
        with self._lock:
            if base in self._robots:
                return self._robots[base]
        rp = None
        try:
            r = self.session.get(base + "/robots.txt", timeout=TIMEOUT)
            if r.status_code == 200:
                rp = RobotFileParser()
                rp.parse(r.text.splitlines())
        except requests.RequestException:
            rp = None
        with self._lock:
            self._robots[base] = rp
        return rp

    def cache_path(self, url: str) -> Path:
        return self.cache_dir / (hashlib.sha1(url.encode()).hexdigest()[:16] + ".bin")

    def fetch(self, url: str) -> dict:
        """Returns {texts, http_status, note}. texts is [] when nothing usable was fetched."""
        cpath = self.cache_path(url)
        meta_path = cpath.with_suffix(".json")
        if cpath.exists() and meta_path.exists() and not self.refetch:
            meta = json.loads(meta_path.read_text())
            data = cpath.read_bytes()
        else:
            rp = self._robots_for(url)
            if rp is not None and not rp.can_fetch(ROBOTS_AGENT, url):
                return {"texts": [], "http_status": None, "note": "disallowed by robots.txt"}
            try:
                r = self.session.get(url, timeout=TIMEOUT, allow_redirects=True)
            except requests.RequestException as e:
                return {"texts": [], "http_status": None, "note": f"fetch error: {type(e).__name__}"}
            data = r.content
            meta = {"url": url, "final_url": r.url, "status": r.status_code,
                    "content_type": r.headers.get("content-type", ""),
                    "fetched_at": datetime.now(timezone.utc).isoformat(timespec="seconds")}
            if r.status_code == 200:
                cpath.parent.mkdir(parents=True, exist_ok=True)
                cpath.write_bytes(data)
                meta_path.write_text(json.dumps(meta, indent=1))
        if meta["status"] != 200:
            return {"texts": [], "http_status": meta["status"], "note": f"HTTP {meta['status']}"}
        is_pdf = "pdf" in meta["content_type"].lower() or data[:5] == b"%PDF-"
        try:
            texts = pdf_texts(data) if is_pdf else html_texts(data.decode("utf-8", errors="replace"))
        except Exception as e:  # noqa: BLE001
            return {"texts": [], "http_status": 200, "note": f"text extraction failed: {type(e).__name__}"}
        if max((len(t) for t in texts), default=0) < MIN_TEXT_CHARS:
            return {"texts": [], "http_status": 200, "note": "no text extracted (JS-rendered page or scan?)"}
        return {"texts": texts, "http_status": 200, "note": "pdf" if is_pdf else ""}


def fetch_all(urls: set[str], fetcher: Fetcher, workers: int = 8) -> dict[str, dict]:
    """Different domains in parallel, one domain at a time with a delay (politeness)."""
    by_domain: dict[str, list[str]] = defaultdict(list)
    for u in sorted(urls):
        by_domain[urlparse(u).netloc].append(u)
    results: dict[str, dict] = {}

    def run(domain_urls: list[str]):
        for i, u in enumerate(domain_urls):
            if i:
                time.sleep(DOMAIN_DELAY_S)
            results[u] = fetcher.fetch(u)

    with ThreadPoolExecutor(max_workers=workers) as ex:
        list(ex.map(run, by_domain.values()))
    return results


def check_record(record: dict, pages: dict[str, dict]) -> dict:
    items = []
    for path, src in iter_sources(record):
        url, quote = src.get("url", ""), src.get("quote", "")
        page = pages.get(url, {"texts": [], "http_status": None, "note": "not fetched"})
        if not page["texts"]:
            items.append({"path": path, "url": url, "status": "unreachable", "score": None,
                          "http_status": page["http_status"], "note": page["note"]})
            continue
        score = score_quote(quote, page["texts"])
        items.append({"path": path, "url": url, "status": classify(score), "score": score,
                      "http_status": page["http_status"], "note": page["note"]})
    counts = defaultdict(int)
    for it in items:
        counts[it["status"]] += 1
    return {"id": record.get("id"), "checked_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "items": items, "summary": dict(counts)}


def main(argv: list[str]) -> int:
    refetch = "--refetch" in argv
    paths = [Path(a) for a in argv if not a.startswith("--")] or sorted(STAGING_DIR.glob("*.json"))
    records = [json.loads(p.read_text(encoding="utf-8")) for p in paths]
    if not records:
        print(f"no records in {STAGING_DIR}")
        return 0
    urls = {src["url"] for r in records for _, src in iter_sources(r) if src.get("url")}
    print(f"{len(records)} records, {len(urls)} unique URLs; fetching (cache: {RAW_DIR})")
    fetcher = Fetcher(RAW_DIR / "pages", refetch=refetch)
    pages = fetch_all(urls, fetcher)
    QUOTE_CHECKS_DIR.mkdir(parents=True, exist_ok=True)
    totals = defaultdict(int)
    for rec in records:
        result = check_record(rec, pages)
        (QUOTE_CHECKS_DIR / f"{rec['id']}.json").write_text(
            json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
        for k, v in result["summary"].items():
            totals[k] += v
        print(f"{rec['id']:40} {result['summary']}")
    print("\nTOTAL", dict(totals))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
