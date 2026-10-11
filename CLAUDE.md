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
.claude/agents/             candidate-scout, investor-extractor, evidence-verifier
schema/investor.schema.json record contract; schema/example.record.json (fictional)
src/
  config.py                 AS_OF, WINDOW_MONTHS=24, DORMANT_MONTHS=36, NEW_FUND_MONTHS=12, SEGMENT
  validate.py               JSON Schema validation of staging records
  check_quotes.py           fetch each cited URL, fuzzy-match each quote
  decide.py                 rules K1–K4 → status, exclusion_reason, null unsupported fields
  fx.py                     ECB reference rates → EUR
  metrics.py                accuracy metrics with Wilson 95% CI → results/
tests/                      pytest; fixtures for every edge case in PLAN §2.4
data/
  candidates/cz_vc.csv              scout output
  candidates/cz_vc_decisions.csv    every candidate + decision + reason (code output)
  records/staging/<id>.json         extractor output
  quote_checks/<id>.json            check_quotes.py output
  verification/<id>.json            verifier output
  records/cz_vc.jsonl               final included records
  manual_review/cz_vc.csv           human ground truth
  runs/run_log.csv                  tokens / tool uses / time per agent run
  fx/ecb_rates.csv                  rates used, with date
  raw/                              page snapshots (gitignored)
results/accuracy.md, accuracy.json
docs/decisions.md           judgment calls (feeds README)
docs/ai-errors.md           every AI mistake found (feeds README)
ai-log/                     /export of each session
```

## Build order

1. `src/config.py`, `src/validate.py`, `requirements.txt` (jsonschema, requests, trafilatura, beautifulsoup4, rapidfuzz, pytest), `.venv`. Commit.
2. `src/check_quotes.py`: for each `source` in a record, fetch the URL (timeout 20 s, normal browser user agent), extract main text with trafilatura (fallback BeautifulSoup), normalize (NFKC, casefold, collapse whitespace, NBSP → space), then `rapidfuzz.fuzz.partial_ratio(quote, text)`. ≥ 90 → `found`, 75–89 → `weak`, < 75 → `missing`, fetch error / JS-only page → `unreachable`. Save the raw HTML to `data/raw/<id>/` and the results to `data/quote_checks/<id>.json`. Tests with a local HTML fixture. Commit.
3. `src/decide.py` + tests **before** running extraction at scale. Rules:
   - fields whose verifier verdict is `unsupported` or `contradicted`, or whose quote is `missing`, become `{"value": null, "null_reason": "not_found"}` with a note naming the verdict;
   - K1: at least one `legal_entities` item, or type `angel` with a sourced profile;
   - K2: at least one `evidence_of_activity` item with `announced_date >= AS_OF - 24 months`, verifier verdict `supported`, and quote `found`/`weak`; or a fund with `close` first/final and a source dated within 12 months;
   - most recent evidence 24–36 months old → `dormant`; older or none → `excluded` / `no_recent_investment`;
   - K3/K4 and exclusion codes from `type`, `hq_country` and the verifier's record opinion; when unsure, exclude with a reason and flag for manual review;
   - capital with `basis = sum_of_fund_sizes` is computed here from `funds[]` only when every fund has a sourced size.
   Output `data/records/cz_vc.jsonl` and `data/candidates/cz_vc_decisions.csv`. Commit.
4. `src/fx.py`, `src/metrics.py` (Wilson interval, per-field coverage and accuracy, citation validity, verifier-vs-human confusion matrix, cost per record). Commit.

## Running the agents

| Agent | Job | Model | Tools |
|---|---|---|---|
| `candidate-scout` | candidates from ONE seed source | sonnet | WebSearch, WebFetch, Read, Write, Edit |
| `investor-extractor` | ONE candidate → one staging record | sonnet | WebSearch, WebFetch, Read, Write |
| `evidence-verifier` | audit ONE record against its sources | opus | Read, WebFetch, Write (no search) |

- **Scout:** one call per seed source, e.g. "Use candidate-scout for segment cz_vc, seed source: CVCA member list https://cvca.cz/en/membership/". Seed sources are listed in PLAN §6.3.
- **Extract:** batches of up to 5 candidates in parallel, one candidate per call. Start with a trial batch of 5, inspect every output by hand, fix the prompt, then continue.
- **Verify:** after `validate.py` and `check_quotes.py` have run for the record. One call per record; pass only `data/records/staging/<id>.json` and `data/quote_checks/<id>.json`.
- After each subagent finishes, append a row to `data/runs/run_log.csv`: `date,agent,id,tokens,tool_uses,duration_s,outcome`, using the numbers Claude Code reports for that subagent run.
- Never paste an agent's final message into another agent's prompt.

## Manual review protocol

`data/manual_review/cz_vc.csv` columns:
`id,field,value_shown,verdict,correct_value,note,reviewed_at`
with `verdict ∈ correct | partially_correct | incorrect | unverifiable`, one row per field per record, plus one row `field=record` (is this an active investor of the claimed type?). Excluded candidates get one row `field=decision` (was exclusion right?).

David does the review **before** seeing verifier verdicts. Generate the review sheet from staging records and decisions without the verification columns.

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
- [ ] manual review covers 100 % of included records and all excluded candidates
- [ ] `results/accuracy.md` reports record precision with 95 % CI, per-field coverage and accuracy, citation validity, verifier-vs-human agreement, cost per record
- [ ] README (Czech): result numbers, how AI was used, agent instructions (link to `.claude/agents/` and their commit history), how output was checked, concrete AI errors, decisions, what is missing, world cost estimate recalculated with pilot numbers
- [ ] `ai-log/` contains every session export
