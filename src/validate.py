"""Validate staging investor records against schema/investor.schema.json plus checks JSON Schema cannot express.

Usage:
    python -m src.validate                      # all files in data/records/staging/
    python -m src.validate path/a.json ...      # specific files

Exit code 0 if every record is valid, 1 otherwise.
"""

import json
import sys
from datetime import date
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

from src.config import QUOTE_MAX_WORDS, SCHEMA_PATH, STAGING_DIR


def load_validator() -> Draft202012Validator:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def iter_sources(record: dict):
    """Yield (json_path, source) for every source object in a record."""
    for key, val in record.items():
        if isinstance(val, dict) and isinstance(val.get("source"), dict):
            yield key, val["source"]
        elif isinstance(val, list):
            for i, item in enumerate(val):
                if isinstance(item, dict) and isinstance(item.get("source"), dict):
                    yield f"{key}[{i}]", item["source"]


def _parse_date(s):
    try:
        return date.fromisoformat(s) if s else None
    except ValueError:
        return None


def extra_checks(record: dict, path: Path | None = None, staging: bool = True) -> list[str]:
    """Rules outside the JSON Schema: quote length, real calendar dates, file naming, agent-owned fields."""
    errors = []
    if path is not None and record.get("id") != path.stem:
        errors.append(f"id: '{record.get('id')}' does not match file name '{path.stem}'")

    if staging:
        if record.get("status") != "pending":
            errors.append(f"status: agents must write 'pending', got '{record.get('status')}' (only decide.py sets it)")
        if record.get("exclusion_reason") is not None:
            errors.append("exclusion_reason: agents must write null (only decide.py sets it)")

    for where, src in iter_sources(record):
        quote = src.get("quote") or ""
        n_words = len(quote.split())
        if n_words > QUOTE_MAX_WORDS:
            errors.append(f"{where}.source.quote: {n_words} words, max {QUOTE_MAX_WORDS}")
        for field in ("published_date", "accessed_date"):
            if src.get(field) and _parse_date(src[field]) is None:
                errors.append(f"{where}.source.{field}: '{src[field]}' is not a real date")
        pub, acc = _parse_date(src.get("published_date")), _parse_date(src.get("accessed_date"))
        if pub and acc and pub > acc:
            errors.append(f"{where}.source: published_date {pub} is after accessed_date {acc}")

    for i, ev in enumerate(record.get("evidence_of_activity") or []):
        ann = ev.get("announced_date")
        if ann and _parse_date(ann) is None:
            errors.append(f"evidence_of_activity[{i}].announced_date: '{ann}' is not a real date")

    cap = (record.get("capital") or {}).get("value")
    if isinstance(cap, dict) and cap.get("as_of") and _parse_date(cap["as_of"]) is None:
        errors.append(f"capital.value.as_of: '{cap['as_of']}' is not a real date")
    return errors


def validate_record(record: dict, validator: Draft202012Validator, path: Path | None = None,
                    staging: bool = True) -> list[str]:
    errors = []
    for err in sorted(validator.iter_errors(record), key=lambda e: list(e.absolute_path)):
        loc = "/".join(str(p) for p in err.absolute_path) or "(root)"
        errors.append(f"{loc}: {err.message}")
    return errors + extra_checks(record, path, staging)


def validate_file(path: Path, validator: Draft202012Validator, staging: bool = True) -> list[str]:
    try:
        record = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        return [f"cannot read JSON: {e}"]
    return validate_record(record, validator, path, staging)


def main(argv: list[str]) -> int:
    paths = [Path(a) for a in argv] or sorted(STAGING_DIR.glob("*.json"))
    if not paths:
        print(f"no records found in {STAGING_DIR}")
        return 0
    validator = load_validator()
    n_bad = 0
    for path in paths:
        errors = validate_file(path, validator)
        if errors:
            n_bad += 1
            print(f"FAIL {path}")
            for e in errors:
                print(f"  - {e}")
        else:
            print(f"ok   {path}")
    print(f"\n{len(paths) - n_bad}/{len(paths)} valid")
    return 1 if n_bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
