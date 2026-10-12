"""Inclusion rules K1-K4 (PLAN §2.3-2.4). The only place that sets `status` and `exclusion_reason`.

Entry points:

  python -m src.decide --make-triage-batches
      Splits data/candidates/cz_vc.csv into triage input files for the candidate-triage agent.

  python -m src.decide --triage
      Reads the triage CSVs (data/candidates/triage/batch_*.csv), decides what can be decided cheaply
      (foreign team, clearly another investor type, lender, platform, ...) and writes the extraction
      queue data/candidates/extract_queue.csv with every candidate that still needs a full record.

  python -m src.decide
      Final decisions. For every staging record: drops values that the verifier or the quote check did
      not support, applies K1-K4, computes capital from fund sizes, writes
        data/records/decided/<id>.json        every extracted record with status + reason
        data/records/cz_vc.jsonl              included (active) records only
        data/records/cz_vc.csv                the same, flattened, with EUR conversions
        data/candidates/cz_vc_decisions.csv   one row per candidate, decided by triage or pipeline

Agents collect facts with sources; this code decides. Rules are tested in tests/test_decide.py.
"""

import copy
import csv
import json
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

from src import fx
from src.config import (AS_OF, DATA, DORMANT_START, NEW_FUND_START, QUOTE_CHECKS_DIR, SEGMENT,
                        SEGMENT_COUNTRY, SEGMENT_TYPES, STAGING_DIR, VERIFICATION_DIR, WINDOW_START)
from src.validate import load_validator, validate_file

CAND_DIR = DATA / "candidates"
TRIAGE_DIR = CAND_DIR / "triage"
QUEUE_PATH = CAND_DIR / "extract_queue.csv"
DECISIONS_PATH = CAND_DIR / f"{SEGMENT}_decisions.csv"
DECIDED_DIR = DATA / "records" / "decided"
FINAL_JSONL = DATA / "records" / f"{SEGMENT}.jsonl"
FINAL_CSV = DATA / "records" / f"{SEGMENT}.csv"

FIELDS = ["hq_country", "type", "sectors", "stages", "ticket", "capital"]
LISTS = ["legal_entities", "funds", "evidence_of_activity", "exclusion_signals"]

# When an investor has no supported recent investment, the most specific signal explains why.
SIGNAL_PRIORITY = ["not_found_or_defunct", "advisor_or_intermediary", "crowdfunding_platform",
                   "grant_or_program_only", "fund_of_funds_or_lp_only", "debt_only", "real_estate_only",
                   "public_markets_only"]

# Triage investor_type -> exclusion code. Types not listed here go to full extraction.
TRIAGE_TYPE_EXCLUSION = {
    "pe": "out_of_scope_type",
    "family_office": "out_of_scope_type",
    "private_holding": "out_of_scope_type",
    "angel": "out_of_scope_type",
    "not_an_investor": "out_of_scope_type",
    "lender": "debt_only",
    "lp_only": "fund_of_funds_or_lp_only",
    "platform": "crowdfunding_platform",
    "public_agency": "grant_or_program_only",
    "advisor": "advisor_or_intermediary",
}


# --------------------------------------------------------------------------- helpers

def parse_date(s) -> date | None:
    try:
        return date.fromisoformat(s) if s else None
    except (TypeError, ValueError):
        return None


def load_json(path: Path) -> dict | None:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else None


def domain(url: str | None) -> str:
    if not url:
        return ""
    d = urlparse(url if "://" in url else "https://" + url).netloc.lower()
    return d[4:] if d.startswith("www.") else d


class Support:
    """Combines the verifier verdict and the quote-check status for one sourced item."""

    def __init__(self, verification: dict | None, quote_check: dict | None):
        self.verified = verification is not None
        self.v = {it["path"]: it["verdict"] for it in (verification or {}).get("items", [])}
        self.q = {it["path"]: it["status"] for it in (quote_check or {}).get("items", [])}

    def check(self, path: str) -> tuple[bool, str]:
        """(supported?, reason). Strict: anything not positively supported is dropped."""
        v, q = self.v.get(path), self.q.get(path)
        if v in ("unsupported", "contradicted"):
            return False, f"verifier={v}"
        if q == "missing":
            return False, "quote not found on page"
        if v in ("supported", "partially_supported"):
            return True, f"verifier={v}" if v == "partially_supported" else ""
        if v == "unverifiable":
            if q in ("found", "weak"):
                return True, "verifier could not open page; quote check found the quote"
            return False, f"verifier=unverifiable, quote={q or 'not checked'}"
        return False, "not verified"


# --------------------------------------------------------------------------- record rules

def apply_support(rec: dict, support: Support) -> tuple[dict, list[str], list[str]]:
    """Null scalar fields and drop list items that are not supported. Returns (record, changes, flags)."""
    rec = copy.deepcopy(rec)
    changes, flags = [], []
    for f in FIELDS:
        obj = rec.get(f) or {}
        if obj.get("value") is None:
            continue
        ok, why = support.check(f)
        if not ok:
            rec[f] = {"value": None, "null_reason": "not_found",
                      "note": f"nulled by decide.py ({why}); extractor said {json.dumps(obj['value'], ensure_ascii=False)}"}
            changes.append(f"{f}: nulled ({why})")
        elif why:
            flags.append(f"{f}: {why}")
    for lst in LISTS:
        kept = []
        for i, item in enumerate(rec.get(lst) or []):
            path = f"{lst}[{i}]"
            if lst == "exclusion_signals" and not item.get("source"):
                kept.append(item)  # not_found_or_defunct may have no source
                continue
            ok, why = support.check(path)
            if ok:
                kept.append(item)
                if why:
                    flags.append(f"{path}: {why}")
            else:
                changes.append(f"{path}: dropped ({why})")
        rec[lst] = kept
    return rec, changes, flags


def latest_investment(rec: dict) -> dict | None:
    dated = [e for e in rec.get("evidence_of_activity") or [] if parse_date(e.get("announced_date"))]
    return max(dated, key=lambda e: parse_date(e["announced_date"]), default=None)


def has_new_fund(rec: dict) -> bool:
    for f in rec.get("funds") or []:
        size = f.get("size") or {}
        pub = parse_date((f.get("source") or {}).get("published_date"))
        if size.get("close") in ("first", "final") and pub and NEW_FUND_START <= pub <= AS_OF:
            return True
    return False


def compute_capital(rec: dict) -> str | None:
    """If capital is unknown but every listed fund has a sourced size in one currency, sum them."""
    if (rec.get("capital") or {}).get("value") is not None:
        return None
    funds = rec.get("funds") or []
    sizes = [f.get("size") for f in funds]
    if not funds or any(s is None for s in sizes) or len({s["currency"] for s in sizes}) != 1:
        return None
    newest = max(funds, key=lambda f: parse_date(f["source"].get("published_date")) or date.min)
    basis = "sum_of_fund_sizes" if len(funds) > 1 else "latest_fund_size"
    rec["capital"] = {
        "value": {"amount": sum(s["amount"] for s in sizes), "currency": sizes[0]["currency"],
                  "basis": basis, "as_of": newest["source"].get("published_date")},
        "source": newest["source"],
        "note": f"computed by decide.py from {len(funds)} fund size(s) in funds[]; source is the newest fund's source",
    }
    return basis


def decide_record(staging: dict, verification: dict | None, quote_check: dict | None) -> dict:
    """Returns {record, status, reason, flags, changes, latest}."""
    if verification is None:
        return {"record": staging, "status": "pending", "reason": None, "changes": [],
                "flags": ["not verified yet"], "latest": latest_investment(staging)}
    rec, changes, flags = apply_support(staging, Support(verification, quote_check))
    basis = compute_capital(rec)
    if basis:
        changes.append(f"capital: computed ({basis})")

    latest = latest_investment(rec)
    latest_d = parse_date(latest["announced_date"]) if latest else None
    active = bool(latest_d and WINDOW_START <= latest_d <= AS_OF) or has_new_fund(rec)
    signals = {s["code"] for s in rec.get("exclusion_signals") or []}
    rtype = (rec.get("type") or {}).get("value")
    hq = (rec.get("hq_country") or {}).get("value")

    if not active and signals:
        status, reason = "excluded", min(signals, key=SIGNAL_PRIORITY.index)
    elif rtype not in SEGMENT_TYPES:
        status, reason = "excluded", "out_of_scope_type"
        if rtype is None:
            flags.append("type unknown")
    elif hq != SEGMENT_COUNTRY:
        status, reason = "excluded", "out_of_scope_geography"
        if hq is None:
            flags.append("hq_country unknown")
    elif not active:
        if latest_d and DORMANT_START <= latest_d < WINDOW_START:
            status, reason = "dormant", None
        else:
            status, reason = "excluded", "no_recent_investment"
    elif not rec.get("legal_entities"):
        status, reason = "excluded", "not_found_or_defunct"
        flags.append("K1: no supported legal entity")
    else:
        status, reason = "active", None

    opinion = (verification.get("record_opinion") or {}).get("active_investor_of_claimed_type")
    if opinion in ("no", "unsure") and status == "active":
        flags.append(f"verifier opinion: {opinion}")
    if opinion == "yes" and status != "active":
        flags.append("verifier opinion: yes, but excluded by rules")

    rec["status"], rec["exclusion_reason"] = status, reason
    return {"record": rec, "status": status, "reason": reason, "changes": changes, "flags": flags,
            "latest": latest}


# --------------------------------------------------------------------------- triage

def read_csv(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def load_triage() -> dict[str, dict]:
    rows = {}
    for p in sorted(TRIAGE_DIR.glob("batch_*.csv")):
        for r in read_csv(p):
            rows[r["candidate_id"]] = r
    return rows


def triage_decision(row: dict) -> tuple[str, str | None]:
    """('excluded', code) when triage alone is enough, else ('extract', None)."""
    hq = (row.get("hq_country") or "").strip().upper()
    itype = (row.get("investor_type") or "").strip()
    if hq and hq != "UNKNOWN" and hq != SEGMENT_COUNTRY:
        return "excluded", "out_of_scope_geography"
    # Type alone excludes a possibly in-segment candidate only on strong evidence (D-015).
    strong = ((row.get("evidence_kind") or "").strip() == "page"
              and (row.get("confidence") or "").strip() == "high")
    if not strong:
        return "extract", None
    if itype in TRIAGE_TYPE_EXCLUSION:
        return "excluded", TRIAGE_TYPE_EXCLUSION[itype]
    if itype == "accelerator" and (row.get("equity_investor") or "").strip() == "no":
        return "excluded", "grant_or_program_only"
    return "extract", None


def make_triage_batches(size: int = 25) -> int:
    """Split the candidate list into triage input files data/candidates/triage/input_NN.csv."""
    candidates = read_csv(CAND_DIR / f"{SEGMENT}.csv")
    TRIAGE_DIR.mkdir(parents=True, exist_ok=True)
    cols = ["candidate_id", "name", "website", "hq_guess", "suspected_type", "note"]
    for n, i in enumerate(range(0, len(candidates), size), 1):
        with (TRIAGE_DIR / f"input_{n:02d}.csv").open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
            w.writeheader()
            w.writerows(candidates[i:i + size])
    print(f"{len(candidates)} candidates -> {n} triage batches of up to {size} in {TRIAGE_DIR}")
    return 0


def run_triage() -> int:
    candidates = read_csv(CAND_DIR / f"{SEGMENT}.csv")
    triage = load_triage()
    queue = []
    for c in candidates:
        t = triage.get(c["candidate_id"])
        if t is None or triage_decision(t)[0] == "extract":
            queue.append({"candidate_id": c["candidate_id"], "name": c["name"],
                          "website": (t or {}).get("website") or c["website"],
                          "triage_type": (t or {}).get("investor_type", ""),
                          "triage_hq": (t or {}).get("hq_country", ""),
                          "hint": c["note"][:300]})
    with QUEUE_PATH.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["candidate_id", "name", "website", "triage_type", "triage_hq", "hint"])
        w.writeheader()
        w.writerows(queue)
    print(f"{len(candidates)} candidates, {len(triage)} triaged, {len(queue)} queued for extraction -> {QUEUE_PATH}")
    return 0


# --------------------------------------------------------------------------- outputs

def flat_row(rec: dict, latest: dict | None, rates) -> dict:
    t = (rec.get("ticket") or {}).get("value") or {}
    c = (rec.get("capital") or {}).get("value") or {}

    def eur(amount, cur):
        return fx.to_eur(amount, cur, rates) if amount is not None and cur else None

    ev_in_window = [e for e in rec.get("evidence_of_activity") or []
                    if (d := parse_date(e.get("announced_date"))) and WINDOW_START <= d <= AS_OF]
    return {
        "id": rec["id"], "name": rec["name"], "website": rec.get("website") or "",
        "type": (rec.get("type") or {}).get("value") or "",
        "hq_country": (rec.get("hq_country") or {}).get("value") or "",
        "sectors": ";".join((rec.get("sectors") or {}).get("value") or []),
        "stages": ";".join((rec.get("stages") or {}).get("value") or []),
        "ticket_min": t.get("min"), "ticket_max": t.get("max"), "ticket_currency": t.get("currency"),
        "ticket_min_eur": eur(t.get("min"), t.get("currency")),
        "ticket_max_eur": eur(t.get("max"), t.get("currency")),
        "ticket_source": ((rec.get("ticket") or {}).get("source") or {}).get("url", ""),
        "capital": c.get("amount"), "capital_currency": c.get("currency"),
        "capital_eur": eur(c.get("amount"), c.get("currency")),
        "capital_basis": c.get("basis"), "capital_as_of": c.get("as_of"),
        "capital_source": ((rec.get("capital") or {}).get("source") or {}).get("url", ""),
        "latest_investment": (latest or {}).get("company", ""),
        "latest_investment_date": (latest or {}).get("announced_date", ""),
        "latest_investment_source": ((latest or {}).get("source") or {}).get("url", ""),
        "n_investments_in_window": len(ev_in_window),
        "legal_entity": "; ".join(f"{le['name']} ({le['registry']} {le['registry_id']})"
                                  for le in rec.get("legal_entities") or []),
    }


def run_final() -> int:
    candidates = read_csv(CAND_DIR / f"{SEGMENT}.csv")
    triage = load_triage()
    rates = fx.load_rates()
    DECIDED_DIR.mkdir(parents=True, exist_ok=True)
    decisions, active, flat, seen_domains = [], [], [], {}

    validator = load_validator()
    for c in candidates:
        cid = c["candidate_id"]
        row = {"candidate_id": cid, "name": c["name"], "decided_by": "", "status": "", "exclusion_reason": "",
               "type": "", "hq_country": "", "latest_investment": "", "latest_investment_date": "",
               "flags": "", "changes": ""}
        spath = STAGING_DIR / f"{cid}.json"
        errors = validate_file(spath, validator) if spath.exists() else []
        if errors:
            row.update(decided_by="none", status="pending", flags=f"invalid staging record: {errors[0]}")
            decisions.append(row)
            continue
        staging = load_json(spath)
        if staging is None:
            t = triage.get(cid)
            if t is None:
                row.update(decided_by="none", status="pending", flags="not triaged")
            else:
                verdict, code = triage_decision(t)
                if verdict == "excluded":
                    row.update(decided_by="triage", status="excluded", exclusion_reason=code,
                               type=t.get("investor_type", ""), hq_country=t.get("hq_country", ""),
                               flags=f"triage evidence: {t.get('evidence_kind', '')}, confidence {t.get('confidence', '')}")
                else:
                    row.update(decided_by="none", status="pending", flags="queued, not extracted")
            decisions.append(row)
            continue

        result = decide_record(staging, load_json(VERIFICATION_DIR / f"{cid}.json"),
                               load_json(QUOTE_CHECKS_DIR / f"{cid}.json"))
        rec, latest = result["record"], result["latest"]
        dom = domain(rec.get("website"))
        if result["status"] == "active" and dom and dom in seen_domains:
            rec["status"], rec["exclusion_reason"] = "excluded", "duplicate"
            result.update(status="excluded", reason="duplicate")
            result["flags"].append(f"same domain as {seen_domains[dom]}")
        elif result["status"] == "active" and dom:
            seen_domains[dom] = cid

        if result["status"] != "pending":
            (DECIDED_DIR / f"{cid}.json").write_text(json.dumps(rec, indent=2, ensure_ascii=False) + "\n",
                                                     encoding="utf-8")
        row.update(decided_by="pipeline", status=result["status"], exclusion_reason=result["reason"] or "",
                   type=(rec.get("type") or {}).get("value") or "",
                   hq_country=(rec.get("hq_country") or {}).get("value") or "",
                   latest_investment=(latest or {}).get("company", ""),
                   latest_investment_date=(latest or {}).get("announced_date", ""),
                   flags=" | ".join(result["flags"]), changes=" | ".join(result["changes"]))
        decisions.append(row)
        if result["status"] == "active":
            active.append(rec)
            flat.append(flat_row(rec, latest, rates))

    with DECISIONS_PATH.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(decisions[0]))
        w.writeheader()
        w.writerows(decisions)
    FINAL_JSONL.parent.mkdir(parents=True, exist_ok=True)
    FINAL_JSONL.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in active), encoding="utf-8")
    if flat:
        with FINAL_CSV.open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(flat[0]))
            w.writeheader()
            w.writerows(flat)

    from collections import Counter
    counts = Counter((d["decided_by"], d["status"], d["exclusion_reason"]) for d in decisions)
    for k, v in sorted(counts.items()):
        print(f"{v:4}  {k[0]:9} {k[1]:9} {k[2]}")
    print(f"\n{len(active)} active records -> {FINAL_JSONL}")
    return 0


def main(argv: list[str]) -> int:
    if "--make-triage-batches" in argv:
        return make_triage_batches()
    return run_triage() if "--triage" in argv else run_final()


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
