"""Inclusion rules (PLAN §2.3-2.4) on small synthetic records built from the fictional example."""

import copy
import json

import pytest

from src.config import ROOT
from src.decide import decide_record, triage_decision

SRC = {"url": "https://example.com/x", "tier": 2, "publisher": "Example", "published_date": None,
       "accessed_date": "2026-10-11", "quote": "example quote here", "self_reported": True}


@pytest.fixture
def rec():
    r = json.loads((ROOT / "schema" / "example.record.json").read_text(encoding="utf-8"))
    r["evidence_of_activity"][0]["announced_date"] = "2026-05-20"
    return r


def all_supported(record: dict) -> dict:
    """A verification file that supports every sourced item of the record."""
    items = [{"path": f, "verdict": "supported"} for f in ("hq_country", "type", "sectors", "stages", "ticket", "capital")]
    for lst in ("legal_entities", "funds", "evidence_of_activity", "exclusion_signals"):
        items += [{"path": f"{lst}[{i}]", "verdict": "supported"} for i in range(len(record.get(lst) or []))]
    return {"items": items, "record_opinion": {"active_investor_of_claimed_type": "yes"}}


def set_verdict(ver: dict, path: str, verdict: str) -> dict:
    for it in ver["items"]:
        if it["path"] == path:
            it["verdict"] = verdict
    return ver


def test_active_with_recent_supported_investment(rec):
    out = decide_record(rec, all_supported(rec), None)
    assert (out["status"], out["reason"]) == ("active", None)
    assert out["record"]["status"] == "active"


def test_unverified_record_stays_pending(rec):
    assert decide_record(rec, None, None)["status"] == "pending"


def test_dormant_when_latest_investment_24_to_36_months_old(rec):
    rec["evidence_of_activity"][0]["announced_date"] = "2024-03-01"
    rec["funds"] = []
    out = decide_record(rec, all_supported(rec), None)
    assert out["status"] == "dormant"


def test_excluded_when_latest_investment_older_than_36_months(rec):
    rec["evidence_of_activity"][0]["announced_date"] = "2021-01-15"
    rec["funds"] = []
    out = decide_record(rec, all_supported(rec), None)
    assert (out["status"], out["reason"]) == ("excluded", "no_recent_investment")


def test_window_boundary_is_inclusive(rec):
    rec["evidence_of_activity"][0]["announced_date"] = "2024-10-11"
    rec["funds"] = []
    assert decide_record(rec, all_supported(rec), None)["status"] == "active"
    rec["evidence_of_activity"][0]["announced_date"] = "2024-10-10"
    assert decide_record(rec, all_supported(rec), None)["status"] == "dormant"


def test_unsupported_evidence_is_dropped_and_record_excluded(rec):
    rec["funds"] = []
    ver = set_verdict(all_supported(rec), "evidence_of_activity[0]", "unsupported")
    out = decide_record(rec, ver, None)
    assert out["record"]["evidence_of_activity"] == []
    assert (out["status"], out["reason"]) == ("excluded", "no_recent_investment")


def test_missing_quote_drops_item_even_if_verifier_supports(rec):
    rec["funds"] = []
    qc = {"items": [{"path": "evidence_of_activity[0]", "status": "missing"}]}
    out = decide_record(rec, all_supported(rec), qc)
    assert out["status"] == "excluded"


def test_unverifiable_kept_only_when_quote_found(rec):
    rec["funds"] = []
    ver = set_verdict(all_supported(rec), "evidence_of_activity[0]", "unverifiable")
    assert decide_record(rec, ver, None)["status"] == "excluded"
    qc = {"items": [{"path": "evidence_of_activity[0]", "status": "found"}]}
    assert decide_record(rec, ver, qc)["status"] == "active"


def test_contradicted_ticket_is_nulled_with_note(rec):
    ver = set_verdict(all_supported(rec), "ticket", "contradicted")
    out = decide_record(rec, ver, None)
    t = out["record"]["ticket"]
    assert t["value"] is None and t["null_reason"] == "not_found" and "contradicted" in t["note"]
    assert out["status"] == "active"


def test_new_fund_close_counts_as_activity(rec):
    rec["evidence_of_activity"] = []
    rec["funds"][0]["source"]["published_date"] = "2026-03-01"
    assert decide_record(rec, all_supported(rec), None)["status"] == "active"


def test_old_fund_close_does_not_count(rec):
    rec["evidence_of_activity"] = []
    rec["funds"][0]["source"]["published_date"] = "2025-03-04"
    out = decide_record(rec, all_supported(rec), None)
    assert (out["status"], out["reason"]) == ("excluded", "no_recent_investment")


def test_foreign_team_excluded(rec):
    rec["hq_country"]["value"] = "SK"
    out = decide_record(rec, all_supported(rec), None)
    assert (out["status"], out["reason"]) == ("excluded", "out_of_scope_geography")


def test_pe_out_of_scope_for_pilot(rec):
    rec["type"]["value"] = "pe"
    out = decide_record(rec, all_supported(rec), None)
    assert (out["status"], out["reason"]) == ("excluded", "out_of_scope_type")


def test_debt_only_signal_without_equity_evidence(rec):
    rec["evidence_of_activity"] = []
    rec["funds"] = []
    rec["exclusion_signals"] = [{"code": "debt_only", "source": SRC, "note": "only venture debt"}]
    out = decide_record(rec, all_supported(rec), None)
    assert (out["status"], out["reason"]) == ("excluded", "debt_only")


def test_mixed_portfolio_debt_signal_but_equity_evidence_stays_active(rec):
    rec["exclusion_signals"] = [{"code": "debt_only", "source": SRC, "note": "also venture debt"}]
    assert decide_record(rec, all_supported(rec), None)["status"] == "active"


def test_signal_priority_prefers_most_specific(rec):
    rec["evidence_of_activity"], rec["funds"] = [], []
    rec["exclusion_signals"] = [{"code": "debt_only", "source": SRC, "note": ""},
                                {"code": "advisor_or_intermediary", "source": SRC, "note": ""}]
    assert decide_record(rec, all_supported(rec), None)["reason"] == "advisor_or_intermediary"


def test_no_legal_entity_fails_k1(rec):
    rec["legal_entities"] = []
    out = decide_record(rec, all_supported(rec), None)
    assert (out["status"], out["reason"]) == ("excluded", "not_found_or_defunct")
    assert any("K1" in f for f in out["flags"])


def test_capital_computed_from_fund_sizes(rec):
    second = copy.deepcopy(rec["funds"][0])
    second["name"], second["size"]["amount"] = "Fund I", 15000000
    second["source"]["published_date"] = "2021-06-01"
    rec["funds"].append(second)
    out = decide_record(rec, all_supported(rec), None)
    cap = out["record"]["capital"]["value"]
    assert cap == {"amount": 55000000, "currency": "EUR", "basis": "sum_of_fund_sizes", "as_of": "2025-03-04"}


def test_capital_not_computed_with_mixed_currencies(rec):
    second = copy.deepcopy(rec["funds"][0])
    second["size"]["currency"] = "CZK"
    rec["funds"].append(second)
    assert decide_record(rec, all_supported(rec), None)["record"]["capital"]["value"] is None


def test_decided_record_validates_against_schema(rec):
    from src.validate import load_validator, validate_record

    out = decide_record(rec, set_verdict(all_supported(rec), "ticket", "contradicted"), None)
    assert validate_record(out["record"], load_validator(), staging=False) == []


STRONG = {"evidence_kind": "page", "confidence": "high"}


@pytest.mark.parametrize("row,expected", [
    ({"hq_country": "US", "investor_type": "vc"}, ("excluded", "out_of_scope_geography")),
    ({"hq_country": "CZ", "investor_type": "pe", **STRONG}, ("excluded", "out_of_scope_type")),
    ({"hq_country": "CZ", "investor_type": "lender", **STRONG}, ("excluded", "debt_only")),
    ({"hq_country": "CZ", "investor_type": "lp_only", **STRONG}, ("excluded", "fund_of_funds_or_lp_only")),
    ({"hq_country": "CZ", "investor_type": "accelerator", "equity_investor": "no", **STRONG},
     ("excluded", "grant_or_program_only")),
    ({"hq_country": "CZ", "investor_type": "accelerator", "equity_investor": "yes", **STRONG}, ("extract", None)),
    ({"hq_country": "CZ", "investor_type": "vc", **STRONG}, ("extract", None)),
    ({"hq_country": "unknown", "investor_type": "unknown"}, ("extract", None)),
    # D-015: weak type evidence never excludes a candidate that may be in the segment
    ({"hq_country": "CZ", "investor_type": "private_holding", "evidence_kind": "page", "confidence": "medium"},
     ("extract", None)),
    ({"hq_country": "unknown", "investor_type": "pe", "evidence_kind": "snippet", "confidence": "high"},
     ("extract", None)),
])
def test_triage_rules(row, expected):
    assert triage_decision(row) == expected
