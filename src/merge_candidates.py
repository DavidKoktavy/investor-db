"""Merge scout outputs into one deduplicated candidate list: data/candidates/cz_vc.csv.

Duplicates are merged when they share a website domain, a candidate_id, or a normalized name,
plus the explicit alias list in data/candidates/aliases.csv (human-curated, with a reason per row).
The merged row keeps every seed source, so we can see how many independent sources named a candidate.

Usage: python -m src.merge_candidates
"""

import csv
import re
import sys
import unicodedata
from collections import OrderedDict
from urllib.parse import urlparse

from src.config import DATA, SEGMENT

CAND_DIR = DATA / "candidates"
SCOUT_FILES = sorted(CAND_DIR.glob("scout_*.csv"))
ALIASES = CAND_DIR / "aliases.csv"
OUT = CAND_DIR / f"{SEGMENT}.csv"

FIELDS = ["candidate_id", "name", "website", "domain", "hq_guess", "suspected_type", "n_sources",
          "seed_sources", "seed_urls", "scout_ids", "note"]

COUNTRY = {"czechia": "CZ", "czech republic": "CZ", "cz": "CZ", "slovakia": "SK", "poland": "PL",
           "united kingdom": "GB", "uk": "GB", "united states": "US", "usa": "US", "germany": "DE",
           "austria": "AT", "sweden": "SE", "france": "FR", "netherlands": "NL", "hungary": "HU",
           "bulgaria": "BG", "luxembourg": "LU", "japan": "JP", "canada": "CA", "portugal": "PT",
           "croatia": "HR", "romania": "RO", "ireland": "IE", "unknown": "", "": ""}

# Order of preference when scouts disagree on the suspected type: the more specific guess wins.
TYPE_RANK = ["vc", "cvc", "pe", "family_office", "private_holding", "angel", "lender", "advisor",
             "platform", "other", "unknown"]


def domain(url: str) -> str:
    if not url:
        return ""
    url = url if "://" in url else "https://" + url
    d = urlparse(url).netloc.lower()
    return d[4:] if d.startswith("www.") else d


def norm_country(s: str) -> str:
    s = (s or "").strip()
    if re.fullmatch(r"[A-Z]{2}", s):
        return s
    return COUNTRY.get(s.lower(), s)


def norm_name(name: str) -> str:
    n = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode().lower()
    n = re.sub(r"[^a-z0-9 ]", " ", n)
    n = re.sub(r"\b(s r o|sro|a s|se|sicav|ltd|llc|gmbh|inc|group)\b", " ", n)
    return re.sub(r"\s+", " ", n).strip()


def load_aliases() -> dict[str, str]:
    if not ALIASES.exists():
        return {}
    with ALIASES.open(encoding="utf-8") as f:
        return {r["alias_id"]: r["canonical_id"] for r in csv.DictReader(f)}


def merge(rows: list[dict], aliases: dict[str, str]) -> list[dict]:
    parent: dict[int, int] = {i: i for i in range(len(rows))}

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    def union(a, b):
        parent[find(a)] = find(b)

    keys: dict[tuple, int] = {}
    for i, r in enumerate(rows):
        cid = aliases.get(r["candidate_id"], r["candidate_id"])
        for key in (("id", cid), ("dom", domain(r["website"])), ("name", norm_name(r["name"]))):
            if not key[1]:
                continue
            if key in keys:
                union(i, keys[key])
            else:
                keys[key] = i

    groups: "OrderedDict[int, list[dict]]" = OrderedDict()
    for i, r in enumerate(rows):
        groups.setdefault(find(i), []).append(r)

    out = []
    for members in groups.values():
        ids = [m["candidate_id"] for m in members]
        canon = next((aliases[i] for i in ids if i in aliases), None)
        canon = canon or min(ids, key=lambda x: (len(x), x))
        websites = [m["website"] for m in members if m["website"]]
        countries = [norm_country(m["hq_guess"]) for m in members if norm_country(m["hq_guess"])]
        types = sorted({m["suspected_type"] for m in members}, key=lambda t: TYPE_RANK.index(t)
                       if t in TYPE_RANK else len(TYPE_RANK))
        sources = list(OrderedDict.fromkeys(m["_file"] for m in members))
        out.append({
            "candidate_id": canon,
            "name": max((m["name"] for m in members), key=len),
            "website": websites[0] if websites else "",
            "domain": domain(websites[0]) if websites else "",
            "hq_guess": max(set(countries), key=countries.count) if countries else "",
            "suspected_type": types[0] if types else "unknown",
            "n_sources": len(sources),
            "seed_sources": ";".join(sources),
            "seed_urls": " ".join(OrderedDict.fromkeys(m["seed_url"] for m in members if m["seed_url"])),
            "scout_ids": ";".join(sorted(set(ids))),
            "note": " | ".join(OrderedDict.fromkeys(m["note"] for m in members if m["note"])),
        })
    return sorted(out, key=lambda r: r["candidate_id"])


def main() -> int:
    rows = []
    for path in SCOUT_FILES:
        with path.open(encoding="utf-8") as f:
            for r in csv.DictReader(f):
                r["_file"] = path.stem.replace("scout_", "")
                rows.append(r)
    merged = merge(rows, load_aliases())
    with OUT.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(merged)
    print(f"{len(rows)} scout rows from {len(SCOUT_FILES)} files -> {len(merged)} candidates in {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
