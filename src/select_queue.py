"""Pick the extraction batch when the queue is longer than the pilot budget (runbook R3, D-016).

    python -m src.select_queue [N]   (default 70)

Ranks data/candidates/extract_queue.csv by how strongly triage and the scouts hint at a Czech VC
and writes the top N, with rank and score, to data/candidates/extract_selected.csv.
"""

import csv
import sys

from src.config import DATA

CAND = DATA / "candidates"
QUEUE = CAND / "extract_queue.csv"
SELECTED = CAND / "extract_selected.csv"
VC_LIKE = ("vc", "cvc", "accelerator")
UNCLEAR = ("", "unknown", "private_holding", "family_office")


def score(row: dict, hq_guess: str) -> tuple[int, int, int]:
    hq = {"CZ": 2, "UNKNOWN": 1, "": 1}.get(row["triage_hq"].strip().upper(), 0)
    kind = 2 if row["triage_type"] in VC_LIKE else 1 if row["triage_type"] in UNCLEAR else 0
    guess = hq_guess.strip().upper()
    scout = 1 if guess == "CZ" else 0 if not guess else -1
    return hq + kind, hq, scout


def main(argv: list[str]) -> int:
    n = int(argv[0]) if argv else 70
    guesses = {r["candidate_id"]: r.get("hq_guess") or ""
               for r in csv.DictReader(open(CAND / "cz_vc.csv", encoding="utf-8"))}
    queue = list(csv.DictReader(open(QUEUE, encoding="utf-8")))
    for r in queue:
        r["score"] = score(r, guesses.get(r["candidate_id"], ""))
    queue.sort(key=lambda r: r["candidate_id"])
    queue.sort(key=lambda r: r["score"], reverse=True)
    fields = ["rank", "score"] + [k for k in queue[0] if k not in ("score",)]
    with open(SELECTED, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for i, r in enumerate(queue[:n], 1):
            w.writerow({**r, "rank": i, "score": "/".join(map(str, r["score"]))})
    print(f"{len(queue)} queued, top {min(n, len(queue))} -> {SELECTED}; "
          f"cut-off score {'/'.join(map(str, queue[min(n, len(queue)) - 1]['score']))}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
