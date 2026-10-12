from src.select_queue import score


def test_czech_vc_ranks_above_unknown_and_foreign_hints():
    cz_vc = score({"triage_hq": "CZ", "triage_type": "vc"}, "CZ")
    unknown_vc = score({"triage_hq": "unknown", "triage_type": "vc"}, "")
    unknown_vc_foreign_guess = score({"triage_hq": "unknown", "triage_type": "vc"}, "US")
    cz_pe = score({"triage_hq": "CZ", "triage_type": "pe"}, "CZ")
    assert cz_vc > unknown_vc > unknown_vc_foreign_guess
    assert unknown_vc > cz_pe
