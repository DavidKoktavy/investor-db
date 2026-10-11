"""Build the manual review sheet (ground truth for metrics), blind to the verifier.

Rows:
  * every included (active) record, by field: record, type, hq_country, sectors, stages, ticket, capital,
    legal_entities[0], and every evidence_of_activity item. Values shown are what the EXTRACTOR wrote
    (staging), so the same review measures the extractor, the verifier and the final database.
  * every candidate excluded or set dormant by the pipeline: one `decision` row
  * a random sample of triage exclusions: one `decision` row each

Writes data/manual_review/<segment>_todo.csv and review.html (open locally, click through, export CSV).
The reviewer saves the filled file as data/manual_review/<segment>.csv.

Usage: python -m src.review_sheet [--max-records N] [--triage-sample N]
"""

import csv
import html
import json
import random
import sys

from src.config import DATA, SEGMENT, STAGING_DIR, WINDOW_START
from src.decide import DECIDED_DIR, DECISIONS_PATH, read_csv

OUT_DIR = DATA / "manual_review"
TODO = OUT_DIR / f"{SEGMENT}_todo.csv"
HTML = OUT_DIR / "review.html"
COLUMNS = ["row_id", "id", "name", "field", "value_shown", "question", "source_url", "source_quote",
           "published_date", "verdict", "correct_value", "note"]
SEED = 42

QUESTIONS = {
    "record": "Is this an ACTIVE venture investor (an investment announced after {window}), type VC or CVC, with its investment team in Czechia?",
    "type": "Is the investor type right (vc = venture fund, cvc = corporate venture unit)?",
    "hq_country": "Is this where the investment team sits?",
    "sectors": "Does the source support these sectors?",
    "stages": "Does the source support these stages?",
    "ticket": "Is this the investor's typical FIRST cheque (not the round size), amount and currency right?",
    "capital": "Is this the total investment capital (or the fund size, as labelled), amount, currency and basis right?",
    "legal_entities": "Is this the right legal entity behind the brand?",
    "evidence_of_activity": "Did THIS investor invest in this company (as an investor), announced on this date?",
    "decision": "Was this candidate rightly left out of the database for the stated reason?",
}


def fmt(value) -> str:
    if value is None:
        return ""
    if isinstance(value, list):
        return ", ".join(str(v) for v in value)
    if isinstance(value, dict):
        if {"min", "max", "currency"} <= value.keys():
            return f"{value.get('min')} – {value.get('max')} {value['currency']}"
        if {"amount", "currency"} <= value.keys():
            extra = f" ({value.get('basis')}, as of {value.get('as_of')})" if value.get("basis") else ""
            return f"{value['amount']:,.0f} {value['currency']}{extra}"
        return json.dumps(value, ensure_ascii=False)
    return str(value)


def src_cols(src: dict | None) -> dict:
    src = src or {}
    return {"source_url": src.get("url", ""), "source_quote": src.get("quote", ""),
            "published_date": src.get("published_date") or ""}


def record_rows(rec: dict) -> list[dict]:
    rows = [{"field": "record", "value_shown": f"{rec['name']} ({rec.get('website') or 'no website'})",
             "question": QUESTIONS["record"].format(window=WINDOW_START.isoformat()),
             **src_cols(None)}]
    for f in ["type", "hq_country", "sectors", "stages", "ticket", "capital"]:
        obj = rec.get(f) or {}
        if obj.get("value") is None:
            continue
        rows.append({"field": f, "value_shown": fmt(obj["value"]), "question": QUESTIONS[f], **src_cols(obj.get("source"))})
    for i, le in enumerate((rec.get("legal_entities") or [])[:1]):
        rows.append({"field": f"legal_entities[{i}]", "value_shown": f"{le['name']} ({le['registry']} {le['registry_id']})",
                     "question": QUESTIONS["legal_entities"], **src_cols(le.get("source"))})
    for i, ev in enumerate(rec.get("evidence_of_activity") or []):
        rows.append({"field": f"evidence_of_activity[{i}]",
                     "value_shown": f"{ev['company']} · {ev.get('round') or ''} · {ev['role']} · announced {ev.get('announced_date')}",
                     "question": QUESTIONS["evidence_of_activity"], **src_cols(ev.get("source"))})
    return rows


def decision_row(d: dict) -> dict:
    status = d["status"] if d["status"] != "excluded" else f"excluded: {d['exclusion_reason']}"
    detail = f"{status} · decided by {d['decided_by']} · type {d['type'] or '?'} · team {d['hq_country'] or '?'}"
    if d.get("latest_investment"):
        detail += f" · latest investment {d['latest_investment']} {d['latest_investment_date']}"
    return {"field": "decision", "value_shown": detail, "question": QUESTIONS["decision"], **src_cols(None)}


def build(max_records: int, triage_sample: int) -> list[dict]:
    rng = random.Random(SEED)
    decisions = read_csv(DECISIONS_PATH)
    active = [d for d in decisions if d["status"] == "active"]
    if len(active) > max_records:
        active = sorted(rng.sample(active, max_records), key=lambda d: d["candidate_id"])
    pipeline_out = [d for d in decisions if d["decided_by"] == "pipeline" and d["status"] in ("excluded", "dormant")]
    triage_out = [d for d in decisions if d["decided_by"] == "triage"]
    triage_out = sorted(rng.sample(triage_out, min(triage_sample, len(triage_out))), key=lambda d: d["candidate_id"])

    rows = []
    for d in active:
        rec = json.loads((STAGING_DIR / f"{d['candidate_id']}.json").read_text(encoding="utf-8"))
        rows += [{"id": d["candidate_id"], "name": d["name"], **r} for r in record_rows(rec)]
        decided = json.loads((DECIDED_DIR / f"{d['candidate_id']}.json").read_text(encoding="utf-8"))
        cap = decided.get("capital") or {}
        if (rec.get("capital") or {}).get("value") is None and cap.get("value") is not None:
            rows.append({"id": d["candidate_id"], "name": d["name"], "field": "capital",
                         "value_shown": fmt(cap["value"]) + " — computed from fund sizes",
                         "question": QUESTIONS["capital"], **src_cols(cap.get("source"))})
    for d in pipeline_out + triage_out:
        rows.append({"id": d["candidate_id"], "name": d["name"], **decision_row(d)})
    for i, r in enumerate(rows, 1):
        r.update(row_id=i, verdict="", correct_value="", note="")
    return rows


def write_html(rows: list[dict]) -> None:
    data = json.dumps(rows, ensure_ascii=False)
    page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Manual review</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body{{font:15px/1.45 -apple-system,system-ui,sans-serif;margin:0;background:#f6f6f4;color:#1d1d1b}}
header{{position:sticky;top:0;background:#1d1d1b;color:#fff;padding:10px 16px;display:flex;gap:16px;align-items:center;z-index:2}}
header button{{font:inherit;padding:6px 12px;border-radius:6px;border:0;cursor:pointer}}
main{{max-width:960px;margin:0 auto;padding:16px}}
.card{{background:#fff;border:1px solid #ddd;border-radius:8px;padding:12px 14px;margin:10px 0}}
.card.done{{border-left:6px solid #2e7d32}} .field{{font-weight:600}} .q{{color:#555;margin:4px 0}}
.val{{font-size:16px;margin:4px 0}} blockquote{{margin:6px 0;padding:6px 10px;background:#f2f2ee;border-radius:4px}}
.opts label{{margin-right:14px;white-space:nowrap}} input[type=text]{{width:45%;margin-top:6px;padding:4px}}
a{{color:#0b57d0;word-break:break-all}} h2{{margin:22px 0 4px;font-size:18px}}
</style></head><body>
<header><b>Manual review · {html.escape(SEGMENT)}</b><span id="prog"></span>
<button onclick="exportCsv()">Download CSV</button></header><main id="m"></main>
<script>
const rows = {data};
const KEY = 'review-{SEGMENT}';
let saved = {{}}; try {{ saved = JSON.parse(localStorage.getItem(KEY) || '{{}}'); }} catch(e) {{}}
const V = ['correct','partially_correct','incorrect','unverifiable'];
function esc(s){{return String(s??'').replace(/[&<>"]/g,c=>({{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}}[c]));}}
function render(){{
  const m = document.getElementById('m'); let html = '', last = '';
  rows.forEach(r => {{
    const s = saved[r.row_id] || {{}};
    if (r.id !== last) {{ html += `<h2>${{esc(r.name)}} <small>(${{esc(r.id)}})</small></h2>`; last = r.id; }}
    html += `<div class="card ${{s.verdict?'done':''}}" id="c${{r.row_id}}"><div class="field">#${{r.row_id}} · ${{esc(r.field)}}</div>
      <div class="q">${{esc(r.question)}}</div><div class="val">${{esc(r.value_shown)}}</div>
      ${{r.source_url?`<div><a href="${{esc(r.source_url)}}" target="_blank" rel="noopener">${{esc(r.source_url)}}</a> ${{r.published_date?'· '+esc(r.published_date):''}}</div>`:''}}
      ${{r.source_quote?`<blockquote>${{esc(r.source_quote)}}</blockquote>`:''}}
      <div class="opts">${{V.map(v=>`<label><input type="radio" name="v${{r.row_id}}" value="${{v}}" ${{s.verdict===v?'checked':''}} onchange="set(${{r.row_id}},'verdict',this.value)"> ${{v.replace('_',' ')}}</label>`).join('')}}</div>
      <input type="text" placeholder="correct value (if wrong)" value="${{esc(s.correct_value)}}" onchange="set(${{r.row_id}},'correct_value',this.value)">
      <input type="text" placeholder="note" value="${{esc(s.note)}}" onchange="set(${{r.row_id}},'note',this.value)"></div>`;
  }});
  m.innerHTML = html; prog();
}}
function set(id,k,v){{ saved[id] = Object.assign(saved[id]||{{}}, {{[k]:v}}); try {{ localStorage.setItem(KEY, JSON.stringify(saved)); }} catch(e) {{}}
  if (k==='verdict') document.getElementById('c'+id).classList.add('done'); prog(); }}
function prog(){{ const n = rows.filter(r => (saved[r.row_id]||{{}}).verdict).length; document.getElementById('prog').textContent = n + ' / ' + rows.length + ' reviewed'; }}
function exportCsv(){{
  const cols = {json.dumps(COLUMNS)};
  const q = v => '"' + String(v ?? '').replace(/"/g,'""') + '"';
  const today = new Date().toISOString().slice(0,10);
  const lines = [cols.concat(['reviewed_at']).join(',')].concat(rows.map(r => {{ const s = saved[r.row_id]||{{}};
    return cols.map(c => q(c in s ? s[c] : r[c])).concat([q(s.verdict ? today : '')]).join(','); }}));
  const a = document.createElement('a'); a.href = URL.createObjectURL(new Blob([lines.join('\\n')], {{type:'text/csv'}}));
  a.download = '{SEGMENT}.csv'; a.click();
}}
render();
</script></body></html>"""
    HTML.write_text(page, encoding="utf-8")


def main(argv: list[str]) -> int:
    max_records = int(argv[argv.index("--max-records") + 1]) if "--max-records" in argv else 40
    triage_sample = int(argv[argv.index("--triage-sample") + 1]) if "--triage-sample" in argv else 15
    rows = build(max_records, triage_sample)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    with TODO.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS)
        w.writeheader()
        w.writerows(rows)
    write_html(rows)
    print(f"{len(rows)} review rows -> {TODO} and {HTML}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
