"""
Marketing Ops Automation - Campaign QA

A small, dependency-free command-line tool that:
- reads a CSV file,
- validates required marketing fields,
- calculates ROAS,
- flags rows that may need manual review,
- writes a QA result CSV.

Usage:
    python campaign_qa.py examples/sample_data.csv
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path
from typing import Optional


REQUIRED_COLUMNS = {
    "market",
    "campaign",
    "model",
    "spend",
    "revenue",
    "conversions",
}


def parse_number(value: str) -> Optional[float]:
    """Return a float when possible; otherwise None."""
    try:
        cleaned = str(value).replace(",", "").strip()
        if cleaned == "":
            return None
        return float(cleaned)
    except (TypeError, ValueError):
        return None


def format_roas(spend: Optional[float], revenue: Optional[float]) -> str:
    """Calculate ROAS when spend and revenue are valid."""
    if spend is None or revenue is None or spend <= 0:
        return ""
    return f"{revenue / spend:.2f}"


def build_flags(row: dict[str, str]) -> list[str]:
    """Return QA flags for a single marketing-data row."""
    flags: list[str] = []

    campaign = row.get("campaign", "").strip()
    model = row.get("model", "").strip()
    spend = parse_number(row.get("spend", ""))
    revenue = parse_number(row.get("revenue", ""))
    conversions = parse_number(row.get("conversions", ""))

    if not campaign:
        flags.append("Missing campaign")
    if not model:
        flags.append("Missing model")

    if spend is None:
        flags.append("Invalid spend")
    elif spend < 0:
        flags.append("Negative spend")
    elif spend == 0:
        flags.append("Zero spend")

    if revenue is None:
        flags.append("Invalid revenue")
    elif revenue < 0:
        flags.append("Negative revenue")

    if conversions is None:
        flags.append("Invalid conversions")
    elif conversions < 0:
        flags.append("Negative conversions")

    if (
        spend is not None
        and revenue is not None
        and spend > 0
        and revenue == 0
    ):
        flags.append("Spend > 0 but revenue = 0")

    return flags


def validate_headers(fieldnames: list[str] | None) -> None:
    if not fieldnames:
        raise ValueError("The CSV file has no header row.")

    missing = REQUIRED_COLUMNS - set(fieldnames)
    if missing:
        missing_text = ", ".join(sorted(missing))
        raise ValueError(f"Missing required column(s): {missing_text}")


def run_qa(input_path: Path) -> Path:
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    output_path = input_path.with_name(
        f"{input_path.stem}_qa_result{input_path.suffix}"
    )

    with input_path.open("r", encoding="utf-8-sig", newline="") as source:
        reader = csv.DictReader(source)
        validate_headers(reader.fieldnames)

        output_fields = list(reader.fieldnames or []) + ["roas", "qa_status", "qa_flags"]

        with output_path.open("w", encoding="utf-8-sig", newline="") as target:
            writer = csv.DictWriter(target, fieldnames=output_fields)
            writer.writeheader()

            for row in reader:
                spend = parse_number(row.get("spend", ""))
                revenue = parse_number(row.get("revenue", ""))
                flags = build_flags(row)

                output_row = dict(row)
                output_row["roas"] = format_roas(spend, revenue)
                output_row["qa_status"] = "CHECK" if flags else "OK"
                output_row["qa_flags"] = " | ".join(flags)
                writer.writerow(output_row)

    return output_path


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python campaign_qa.py <input.csv>")
        return 1

    try:
        output = run_qa(Path(sys.argv[1]))
    except (ValueError, FileNotFoundError) as exc:
        print(f"Error: {exc}")
        return 1

    print(f"QA complete: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
