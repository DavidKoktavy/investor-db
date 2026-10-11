"""EUR conversion with ECB euro reference rates for one stated date (data/fx/ecb_rates.csv).

Records keep amounts in their original currency; EUR values exist only in derived outputs, so the
conversion date is explicit and can be changed in one place.

Usage: python -m src.fx --update      # download today's ECB reference rates into data/fx/ecb_rates.csv
"""

import csv
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

from src.config import DATA

RATES_PATH = DATA / "fx" / "ecb_rates.csv"
ECB_URL = "https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml"


def load_rates(path: Path = RATES_PATH) -> dict[str, float]:
    """{currency: units per 1 EUR}. EUR itself is 1.0."""
    rates = {"EUR": 1.0}
    if path.exists():
        with path.open(encoding="utf-8") as f:
            for r in csv.DictReader(f):
                rates[r["currency"].upper()] = float(r["rate_per_eur"])
    return rates


def to_eur(amount: float | None, currency: str | None, rates: dict[str, float]) -> float | None:
    if amount is None or not currency:
        return None
    rate = rates.get(currency.upper())
    return round(amount / rate) if rate else None


def parse_ecb(xml_text: str) -> tuple[str, dict[str, float]]:
    root = ET.fromstring(xml_text)
    day = next(e for e in root.iter() if e.get("time"))
    return day.get("time"), {e.get("currency"): float(e.get("rate")) for e in day if e.get("currency")}


def update(path: Path = RATES_PATH) -> int:
    import requests

    r = requests.get(ECB_URL, timeout=20)
    r.raise_for_status()
    day, rates = parse_ecb(r.text)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["date", "currency", "rate_per_eur", "source_url"])
        for cur, rate in sorted(rates.items()):
            w.writerow([day, cur, rate, ECB_URL])
    print(f"{len(rates)} ECB reference rates for {day} -> {path}")
    return 0


if __name__ == "__main__":
    sys.exit(update() if "--update" in sys.argv else 0)
