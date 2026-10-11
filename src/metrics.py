"""Accuracy and cost metrics from the manual review (ground truth) -> results/accuracy.{json,md}.

Definitions (PLAN §7.3):
  record precision      included records the reviewer marked `correct` / included records reviewed
  decision accuracy     exclusions the reviewer agreed with / exclusions reviewed (pipeline, triage separately)
  field coverage        non-null in the final database / included records
  field accuracy        `correct` / reviewed values that are in the final database (partially counted apart)
  extractor accuracy    `correct` / all reviewed extractor values (before verification)
  citation validity     quote-check status of every cited source
  verifier vs human     confusion matrix of verifier verdicts against reviewer verdicts
All proportions carry a 95 % Wilson interval: small samples give wide intervals, and we say so.

Usage: python -m src.metrics
"""

import csv
import json
import math
import sys
from collections import Counter, defaultdict

from src.config import DATA, QUOTE_CHECKS_DIR, ROOT, SEGMENT, STAGING_DIR, VERIFICATION_DIR
from src.decide import DECIDED_DIR, DECISIONS_PATH, Support, load_json, read_csv

REVIEW = DATA / "manual_review" / f"{SEGMENT}.csv"
REVIEW_TIME = DATA / "manual_review" / "time_minutes.txt"
RUN_LOG = DATA / "runs" / "run_log.csv"
OUT_JSON = ROOT / "results" / "accuracy.json"
OUT_MD = ROOT / "results" / "accuracy.md"
FIELDS = ["type", "hq_country", "sectors", "stages", "ticket", "capital", "legal_entities", "evidence_of_activity"]
# Blended token price for the cost estimate (USD per million tokens). Claude Code reports total tokens per
# subagent without the input/output split; we assume ~90 % input (pages read) and ~10 % output.
PRICE = {"sonnet": 0.9 * 2 + 0.1 * 10, "opus": 0.9 * 4 + 0.1 * 20, "haiku": 0.9 * 0.10 + 0.1 * 0.50}


def wilson(k: int, n: int, z: float = 1.96) -> tuple[float | None, float | None]:
    if n == 0:
        return None, None
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    m = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return round(100 * (c - m), 1), round(100 * (c + m), 1)


def prop(k: int, n: int) -> dict:
    lo, hi = wilson(k, n)
    return {"k": k, "n": n, "pct": round(100 * k / n, 1) if n else None, "ci95": [lo, hi]}


def field_of(path: str) -> str:
    return path.split("[")[0]


def pct(d: dict) -> str:
    if not d["n"]:
        return "–"
    return f"{d['pct']} % ({d['k']}/{d['n']}; 95% CI {d['ci95'][0]}–{d['ci95'][1]} %)"


def compute() -> dict:
    decisions = read_csv(DECISIONS_PATH)
    review = read_csv(REVIEW) if REVIEW.exists() else []
    reviewed = [r for r in review if r.get("verdict")]
    by_id = defaultdict(list)
    for r in reviewed:
        by_id[r["id"]].append(r)

    out: dict = {"funnel": Counter(), "n_review_rows": len(review), "n_reviewed": len(reviewed)}
    for d in decisions:
        out["funnel"][f"{d['decided_by']}:{d['status']}:{d['exclusion_reason']}"] += 1
    out["funnel"] = dict(sorted(out["funnel"].items()))
    active_ids = [d["candidate_id"] for d in decisions if d["status"] == "active"]
    out["n_candidates"], out["n_active"] = len(decisions), len(active_ids)

    # record precision
    rec_rows = [r for r in reviewed if r["field"] == "record"]
    out["record_precision"] = prop(sum(r["verdict"] == "correct" for r in rec_rows), len(rec_rows))

    # decision accuracy
    for who in ("pipeline", "triage"):
        dec_ids = {d["candidate_id"] for d in decisions if d["decided_by"] == who and d["status"] != "active"}
        rows = [r for r in reviewed if r["field"] == "decision" and r["id"] in dec_ids]
        out[f"decision_accuracy_{who}"] = prop(sum(r["verdict"] == "correct" for r in rows), len(rows))

    # field coverage, final accuracy, extractor accuracy, verifier vs human
    finals = {cid: load_json(DECIDED_DIR / f"{cid}.json") for cid in active_ids}
    coverage, final_acc, extr_acc = {}, defaultdict(Counter), defaultdict(Counter)
    confusion = defaultdict(Counter)
    for f in ["type", "hq_country", "sectors", "stages", "ticket", "capital"]:
        k = sum(1 for r in finals.values() if r and (r.get(f) or {}).get("value") is not None)
        coverage[f] = prop(k, len(finals))
    coverage["legal_entities"] = prop(sum(1 for r in finals.values() if r and r.get("legal_entities")), len(finals))
    coverage["evidence_in_window"] = prop(len(finals), len(finals))

    for cid, rows in by_id.items():
        ver = load_json(VERIFICATION_DIR / f"{cid}.json")
        qc = load_json(QUOTE_CHECKS_DIR / f"{cid}.json")
        support = Support(ver, qc) if ver else None
        for r in rows:
            if r["field"] in ("record", "decision"):
                continue
            fld = field_of(r["field"])
            extr_acc[fld][r["verdict"]] += 1
            if support:
                v = support.v.get(r["field"], "none")
                confusion[v][r["verdict"]] += 1
                kept, _ = support.check(r["field"])
                if kept and cid in active_ids:
                    final_acc[fld][r["verdict"]] += 1

    def summarize(table):
        res = {}
        for fld, c in table.items():
            n = sum(c.values())
            res[fld] = {**prop(c["correct"], n), "partially_correct": c["partially_correct"],
                        "incorrect": c["incorrect"], "unverifiable": c["unverifiable"]}
        return res

    out["field_coverage"] = coverage
    out["field_accuracy_final"] = summarize(final_acc)
    out["field_accuracy_extractor"] = summarize(extr_acc)
    allf = Counter()
    for c in final_acc.values():
        allf.update(c)
    out["value_accuracy_final_all_fields"] = prop(allf["correct"], sum(allf.values()))
    alle = Counter()
    for c in extr_acc.values():
        alle.update(c)
    out["value_accuracy_extractor_all_fields"] = prop(alle["correct"], sum(alle.values()))
    out["verifier_vs_human"] = {k: dict(v) for k, v in confusion.items()}
    good_dropped = sum(confusion[v]["correct"] for v in ("unsupported", "contradicted"))
    bad_passed = sum(confusion[v]["incorrect"] for v in ("supported", "partially_supported"))
    out["verifier_dropped_correct_values"] = good_dropped
    out["verifier_passed_incorrect_values"] = bad_passed

    # citation validity (all staging sources) and how much each check removed
    qstat = Counter()
    for p in QUOTE_CHECKS_DIR.glob("*.json"):
        for it in json.loads(p.read_text(encoding="utf-8"))["items"]:
            qstat[it["status"]] += 1
    out["quote_checks"] = dict(qstat)
    nq = sum(qstat.values())
    out["citation_validity"] = prop(qstat["found"] + qstat["weak"], nq)
    vstat = Counter()
    for p in VERIFICATION_DIR.glob("*.json"):
        for it in json.loads(p.read_text(encoding="utf-8"))["items"]:
            vstat[it["verdict"]] += 1
    out["verifier_verdicts"] = dict(vstat)
    out["n_staging_records"] = len(list(STAGING_DIR.glob("*.json")))

    # cost
    cost = defaultdict(lambda: {"runs": 0, "tokens": 0, "tool_uses": 0, "duration_s": 0.0, "usd": 0.0})
    if RUN_LOG.exists():
        for r in read_csv(RUN_LOG):
            c = cost[r["agent"]]
            c["runs"] += 1
            c["tokens"] += int(r["tokens"] or 0)
            c["tool_uses"] += int(r["tool_uses"] or 0)
            c["duration_s"] += float(r["duration_s"] or 0)
            c["usd"] += int(r["tokens"] or 0) / 1e6 * PRICE.get(r.get("model", "sonnet"), PRICE["sonnet"])
    out["cost_by_agent"] = {k: {**v, "usd": round(v["usd"], 2)} for k, v in cost.items()}
    total_usd = sum(v["usd"] for v in cost.values())
    out["cost_total_usd"] = round(total_usd, 2)
    out["cost_per_active_record_usd"] = round(total_usd / len(active_ids), 2) if active_ids else None
    minutes = float(REVIEW_TIME.read_text().strip()) if REVIEW_TIME.exists() else None
    out["review_minutes"] = minutes
    out["review_minutes_per_record"] = round(minutes / max(1, len(rec_rows)), 1) if minutes else None
    return out


def to_markdown(m: dict) -> str:
    L = ["# Výsledky měření přesnosti — pilot VC v ČR", "",
         f"Kandidátů: **{m['n_candidates']}** · zařazeno (active): **{m['n_active']}** · "
         f"plných záznamů (extrakce): {m['n_staging_records']} · řádků ruční kontroly: {m['n_reviewed']}/{m['n_review_rows']}", "",
         "## Hlavní čísla", "",
         "| Metrika | Hodnota |", "|---|---|",
         f"| Přesnost záznamu (aktivní VC/CVC s týmem v ČR) | {pct(m['record_precision'])} |",
         f"| Správnost vyřazení — pipeline | {pct(m['decision_accuracy_pipeline'])} |",
         f"| Správnost vyřazení — triáž (vzorek) | {pct(m['decision_accuracy_triage'])} |",
         f"| Přesnost údajů ve finální databázi (všechna pole) | {pct(m['value_accuracy_final_all_fields'])} |",
         f"| Přesnost údajů od extraktoru před ověřením | {pct(m['value_accuracy_extractor_all_fields'])} |",
         f"| Platnost citací (citace nalezena na stránce) | {pct(m['citation_validity'])} |",
         f"| Ověřovatel zahodil správný údaj | {m['verifier_dropped_correct_values']}× |",
         f"| Ověřovatel propustil chybný údaj | {m['verifier_passed_incorrect_values']}× |",
         f"| Náklad výpočtu celkem / na zařazený záznam | {m['cost_total_usd']} USD / {m['cost_per_active_record_usd']} USD |",
         f"| Ruční kontrola | {m['review_minutes']} min ({m['review_minutes_per_record']} min na záznam) |", "",
         "## Pole: vyplněnost a přesnost", "",
         "| Pole | Vyplněnost | Přesnost (finální DB) | Přesnost (extraktor) |", "|---|---|---|---|"]
    for f in FIELDS:
        cov = m["field_coverage"].get("evidence_in_window" if f == "evidence_of_activity" else f)
        fa = m["field_accuracy_final"].get(f)
        ea = m["field_accuracy_extractor"].get(f)
        L.append(f"| {f} | {pct(cov) if cov else '–'} | {pct(fa) if fa else '–'} | {pct(ea) if ea else '–'} |")
    L += ["", "## Ověřovatel vs. ruční kontrola", "", "| verdikt ověřovatele | correct | partially | incorrect | unverifiable |",
          "|---|---|---|---|---|"]
    for v, c in sorted(m["verifier_vs_human"].items()):
        L.append(f"| {v} | {c.get('correct', 0)} | {c.get('partially_correct', 0)} | {c.get('incorrect', 0)} | {c.get('unverifiable', 0)} |")
    L += ["", "## Trychtýř rozhodnutí", "", "| rozhodl / stav / důvod | počet |", "|---|---|"]
    L += [f"| {k} | {v} |" for k, v in m["funnel"].items()]
    L += ["", "## Kontrola citací (skript) a verdikty ověřovatele", "",
          f"- citace: {m['quote_checks']}", f"- ověřovatel: {m['verifier_verdicts']}", "",
          "## Náklady podle agenta", "", "| agent | běhů | tokenů | nástrojů | čas (min) | USD (odhad) |", "|---|---|---|---|---|---|"]
    for a, c in sorted(m["cost_by_agent"].items()):
        L.append(f"| {a} | {c['runs']} | {c['tokens']:,} | {c['tool_uses']} | {c['duration_s'] / 60:.0f} | {c['usd']} |")
    L += ["", "_Intervaly jsou 95% Wilsonovy. USD je odhad z celkových tokenů (90 % vstup / 10 % výstup, ceník PLAN §8)._", ""]
    return "\n".join(L)


def main() -> int:
    m = compute()
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(m, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    OUT_MD.write_text(to_markdown(m), encoding="utf-8")
    print(OUT_MD.read_text(encoding="utf-8"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
