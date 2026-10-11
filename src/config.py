"""Pipeline constants. Every date window in the pipeline is computed from here (PLAN §2.3)."""

from datetime import date
from pathlib import Path

# Collection date: all activity windows are measured back from this day.
AS_OF = date(2026, 10, 11)

# K2: at least one investment announced within this many months before AS_OF.
WINDOW_MONTHS = 24
# Most recent investment 24-36 months old -> dormant; older -> excluded.
DORMANT_MONTHS = 36
# K2 alternative: a fund first/final close within this many months.
NEW_FUND_MONTHS = 12

# Pilot segment: VC/CVC managers with the investment team in Czechia.
SEGMENT = "cz_vc"
SEGMENT_COUNTRY = "CZ"
SEGMENT_TYPES = ("vc", "cvc")

# Max words in a source quote (CLAUDE.md golden rule 3).
QUOTE_MAX_WORDS = 25

ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = ROOT / "schema" / "investor.schema.json"
DATA = ROOT / "data"
STAGING_DIR = DATA / "records" / "staging"
QUOTE_CHECKS_DIR = DATA / "quote_checks"
VERIFICATION_DIR = DATA / "verification"
RAW_DIR = DATA / "raw"


def months_before(d: date, months: int) -> date:
    """Same calendar day `months` earlier, clamped to the month's last day (e.g. 31 Mar - 1 -> 28/29 Feb)."""
    total = d.year * 12 + (d.month - 1) - months
    year, month = divmod(total, 12)
    month += 1
    for day in (d.day, 30, 29, 28):
        try:
            return date(year, month, day)
        except ValueError:
            continue
    raise AssertionError("unreachable")


WINDOW_START = months_before(AS_OF, WINDOW_MONTHS)
DORMANT_START = months_before(AS_OF, DORMANT_MONTHS)
NEW_FUND_START = months_before(AS_OF, NEW_FUND_MONTHS)
