import copy
import json

import pytest

from src.config import ROOT
from src.validate import load_validator, validate_record


@pytest.fixture(scope="module")
def validator():
    return load_validator()


@pytest.fixture
def example():
    return json.loads((ROOT / "schema" / "example.record.json").read_text(encoding="utf-8"))


def test_example_record_is_valid(validator, example):
    assert validate_record(example, validator) == []


def test_null_value_requires_null_reason(validator, example):
    rec = copy.deepcopy(example)
    rec["sectors"] = {"value": None}
    assert any(e.startswith("sectors") for e in validate_record(rec, validator))


def test_value_with_source_and_null_reason_rejected(validator, example):
    rec = copy.deepcopy(example)
    src = rec["type"]["source"]
    rec["type"] = {"value": None, "null_reason": "not_found", "source": src}
    assert any(e.startswith("type") for e in validate_record(rec, validator))


def test_long_quote_rejected(validator, example):
    rec = copy.deepcopy(example)
    rec["type"]["source"]["quote"] = " ".join(["word"] * 26)
    assert any("26 words" in e for e in validate_record(rec, validator))


def test_agent_cannot_set_status(validator, example):
    rec = copy.deepcopy(example)
    rec["status"] = "active"
    assert any(e.startswith("status") for e in validate_record(rec, validator))
    assert validate_record(rec, validator, staging=False) == []


def test_impossible_date_rejected(validator, example):
    rec = copy.deepcopy(example)
    rec["evidence_of_activity"][0]["announced_date"] = "2026-02-30"
    assert any("not a real date" in e for e in validate_record(rec, validator))


def test_published_after_accessed_rejected(validator, example):
    rec = copy.deepcopy(example)
    src = rec["type"]["source"]
    src["published_date"], src["accessed_date"] = "2026-10-12", "2026-10-11"
    assert any("after accessed_date" in e for e in validate_record(rec, validator))


def test_id_must_match_file_name(validator, example, tmp_path):
    path = tmp_path / "other-name.json"
    assert any(e.startswith("id:") for e in validate_record(example, validator, path))
