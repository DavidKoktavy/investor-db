from datetime import date

from src.config import months_before


def test_months_before_same_day():
    assert months_before(date(2026, 10, 11), 24) == date(2024, 10, 11)


def test_months_before_clamps_to_month_end():
    assert months_before(date(2026, 3, 31), 1) == date(2026, 2, 28)
    assert months_before(date(2026, 2, 28), 24) == date(2024, 2, 28)
    assert months_before(date(2026, 5, 31), 3) == date(2026, 2, 28)
    assert months_before(date(2028, 5, 31), 3) == date(2028, 2, 29)


def test_months_before_crosses_year():
    assert months_before(date(2026, 1, 15), 13) == date(2024, 12, 15)
