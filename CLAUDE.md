# CLAUDE.md — Investor DB (hiring assignment A)

## What this repo is

A hiring assignment for a Junior AI Developer role: a **reliable database of company investors built only from public data**. Every record must be a real, currently active investor, and every value must carry its source and date. The pilot segment is **venture capital managers whose investment team is based in Czechia** (`cz_vc`). Deadline: **16 Oct 2026**.

**`PLAN.md` is the source of truth** for inclusion rules (K1–K4), exclusion codes, the data model, sources and metrics. Read it before any work. If you need to deviate, write the decision to `docs/decisions.md` first, then act.

Required deliverables: `PLAN.md`; sample data with a source on every value; accuracy results; `README.md` in Czech explaining how AI was used (agent instructions, how output was checked, where the AI was wrong, judgment calls); code with incremental commit history; `ai-log/` with an `/export` of every Claude Code session.

Language: README, PLAN and docs in **Czech**. Code, comments, agent prompts and commit messages in **English**.

## Golden rules (non-negotiable)

1. **Never invent a value.** Unknown → `{"value": null, "null_reason": "..."}`. A wrong value is worse than a missing one.
2. **Every non-null value has a `source`**: url, tier (1–3), publisher, published_date (or null), accessed_date, quote, self_reported.
3. **Quotes are exact text from the page, ≤ 25 words.** WebFetch returns the output of a small model, not the raw page, and can paraphrase. Never treat WebFetch text as verbatim; every quote is checked by `src/check_quotes.py`.
4. **Search-result snippets are leads, never evidence.** Evidence comes from a fetched page.
5. **Agents collect facts; code decides.** Only `src/decide.py` sets `status` and `exclusion_reason`.
6. **The verifier never sees the extractor's reasoning and never edits records.** Pass it only file paths.
7. **Public data only.** No paid databases, no LinkedIn scraping, respect robots.txt. Aggregator pages (Crunchbase, Dealroom, …) are candidate leads, not evidence.
8. **Raw page snapshots live in `data/raw/` (gitignored).** Never commit them.
9. **Amounts:** plain numbers in units with ISO currency (EUR 1.5 mil → `1500000`, `"EUR"`). EUR conversion only in code, using the ECB reference rate for a stated date.
10. **Dates are ISO 8601.** The collection date `AS_OF` and the windows (24 / 36 / 12 months) live in `src/config.py`.

## Repository layout

```
PLAN.md                     plan (Czech) – rules, sources, metrics, cost
README.md                   final write-up (Czech)
CLAUDE.md                   this file
.claude/agents/             candidate-scout, candidate-triage, investor-extractor, evidence-verifier
.claude/settings.json       project permissions (web reads, the pipeline commands, git)
schema/investor.schema.json record contract; schema/example.record.json (fictional)
src/
  config.py                 AS_OF, WINDOW_MONTHS=24, DORMANT_MONTHS=36, NEW_FUND_MONTHS=12, SEGMENT
  merge_candidates.py       scout CSVs -> one deduplicated candidate list
  validate.py               JSON Schema validation of staging records
  check_quotes.py           fetch each cited URL, fuzzy-match each quote (found/weak/missing/unreachable)
  decide.py                 triage rules, rules K1–K4, support gating -> status, exclusion_reason
  fx.py                     ECB reference rates -> EUR (only in derived outputs)
  review_sheet.py           blind manual review sheet (CSV + review.html)
  metrics.py                accuracy + cost metrics with Wilson 95% CI -> results/
tests/                      pytest
data/
  candidates/scout_*.csv            scout outputs (3 seed sources)
  candidates/aliases.csv            human-curated merges, with reasons
  candidates/cz_vc.csv              merged candidate list (225)
  candidates/triage/                triage inputs and outputs (attempt1/ = failed first run, kept)
  candidates/extract_queue.csv      candidates that need a full record
  candidates/cz_vc_decisions.csv    every candidate + decision + reason (code output)
  records/staging/<id>.json         extractor output
  quote_checks/<id>.json            check_quotes.py output
  verification/<id>.json            verifier output
  records/decided/<id>.json         records after decide.py
  records/cz_vc.jsonl, cz_vc.csv    the database: included records
  manual_review/                    review.html, cz_vc_todo.csv, cz_vc.csv (human ground truth), time_minutes.txt
  runs/run_log.csv                  tokens / tool uses / time per agent run
  fx/ecb_rates.csv                  rates used, with date
  raw/                              page snapshots (gitignored)
results/accuracy.md, accuracy.json
docs/decisions.md, docs/ai-errors.md
ai-log/                     exports of every AI session
```

## Status

Done: plan, schema, code and tests (`.venv/bin/python -m pytest`), candidates from three scouts (225 after merge).
Next: the **pilot runbook** below. Every step is resumable: it skips work whose output file already exists.

## Pilot runbook

Run from the repo root. `PY=.venv/bin/python`. Commit and push after every step (`git add -A && git commit -m "..." && git push`).

| Agent | Job | Model |
|---|---|---|
| `candidate-triage` | 25 candidates per call -> team country + investor type, one source each | haiku |
| `investor-extractor` | ONE candidate per call -> one staging record | sonnet |
| `evidence-verifier` | ONE record per call -> verdict per sourced item (never searches) | opus |

**R0 Setup.** `$PY -m pip install -r requirements.txt`, `$PY -m pytest -q` (must pass), `$PY -m src.fx --update`.

**R1 Triage.** `$PY -m src.decide --make-triage-batches` (creates `data/candidates/triage/input_NN.csv`). For every `input_NN.csv` without a matching `batch_NN.csv`, call `candidate-triage` with the input path and the output path `data/candidates/triage/batch_NN.csv`. Run 3 calls in parallel. Then check: if more than a third of a batch is `unknown`, re-run that batch once.

**R2 Queue.** `$PY -m src.decide --triage` -> `data/candidates/extract_queue.csv`.

**R3 Extract.** For every queue row without `data/records/staging/<candidate_id>.json`, call `investor-extractor` with that one row (all columns) and AS_OF. Run 4 calls in parallel.
- Trial first: run the first 4, then read each record yourself against its sources. If an agent misread something systematic (wrong field semantics, quote not verbatim, round size as ticket…), fix `.claude/agents/investor-extractor.md`, commit it alone as `agents: …`, log the error in `docs/ai-errors.md`, delete those 4 records and start again.
- Then the rest of the queue. If the queue is longer than 70, process the 70 rows with the strongest hints of a Czech VC first (`triage_type` vc/cvc/accelerator and `triage_hq` CZ) and record the rest as not processed in `docs/decisions.md`.

**R4 Validate.** `$PY -m src.validate`. For a failing record, re-run the extractor once with the error list in the prompt. If it still fails, leave it (decide.py keeps it `pending` and says why).

**R5 Quote check.** `$PY -m src.check_quotes` (fetches every cited page; takes a few minutes).

**R6 Verify.** For every staging record without `data/verification/<id>.json`, call `evidence-verifier` with the paths of the record and its quote check only. Run 4 in parallel. Never pass the extractor's final message.

**R7 Decide.** `$PY -m src.decide`. Read `data/candidates/cz_vc_decisions.csv`: for every `flags` entry that suggests an agent error, add a row to `docs/ai-errors.md`.

**R8 Review sheet.** `$PY -m src.review_sheet` -> `data/manual_review/review.html` and `cz_vc_todo.csv`. Stop here: the manual review is done by David, not by an agent.

**R9 After David's review** (he saves `data/manual_review/cz_vc.csv` and `time_minutes.txt`): `$PY -m src.metrics` -> `results/accuracy.md`.

**Logging every agent run.** After each subagent call, append one row to `data/runs/run_log.csv` (create it with this header if missing):
`date,agent,model,id,tokens,tool_uses,duration_s,outcome`
using the token count, tool uses and duration that Claude Code reports for that call; `id` is the candidate id or batch name; `outcome` is `ok`, `invalid`, `failed` or `rerun`.

**If you hit a usage limit:** stop, commit, push. The runbook resumes from where it stopped.

## Manual review protocol

`review.html` (open in a browser) shows every row with its link and quote; the reviewer clicks `correct | partially_correct | incorrect | unverifiable`, optionally types the correct value, then "Download CSV" and saves it as `data/manual_review/cz_vc.csv`. Total minutes spent go to `data/manual_review/time_minutes.txt`.
The sheet never shows verifier verdicts or quote-check results, so the review is blind to them. Values shown are the extractor's, so one review measures the extractor, the verifier and the final database.

## Logging for the README

- `docs/decisions.md`: every judgment call — date, decision, alternatives, why.
- `docs/ai-errors.md`: every AI mistake found by code, verifier or manual review — date, agent, record, field, what was wrong, how it was detected, what changed (prompt, rule, nothing).
- When an agent prompt changes, commit it on its own with `agents: <what and why>`, so the history shows the prompt iterations.

## Git

- Commit after every step, small and descriptive. Prefixes: `plan:`, `schema:`, `agents:`, `src:`, `tests:`, `data:`, `results:`, `docs:`.
- Never rewrite history, never commit `data/raw/`, `.venv/` or secrets.

## Session hygiene

- Start of session: read this file, `PLAN.md`, the tail of `docs/decisions.md` and `docs/ai-errors.md`.
- End of session: `/export` to `ai-log/NN-topic.md` (e.g. `ai-log/03-extraction-batch-1.md`), then commit.

## Definition of done

- [ ] every candidate has a row in `cz_vc_decisions.csv` with a decision and reason
- [ ] every included record validates and has ≥ 1 supported activity item in the window
- [ ] manual review covers the included records (all, or a random 40 if more) and every excluded candidate decided by the pipeline, plus a random 15 decided by triage
- [ ] `results/accuracy.md` reports record precision with 95 % CI, per-field coverage and accuracy, citation validity, verifier-vs-human agreement, cost per record
- [ ] README (Czech): result numbers, how AI was used, agent instructions (link to `.claude/agents/` and their commit history), how output was checked, concrete AI errors, decisions, what is missing, world cost estimate recalculated with pilot numbers
- [ ] `ai-log/` contains every session export
