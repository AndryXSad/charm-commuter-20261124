#!/usr/bin/env python3
"""Charm the Commuter — make.fun bounty entry.

Writes one line of weather forecast (at most 140 characters) for a city
that does not exist to /output/entry.txt, where the house judge reads it.
Standard library only.
"""

import os
from pathlib import Path

LINE = (
    "Snoddington: 11°C, drizzle till nine, then sun — the 8:15 bus is on "
    "time, and the pigeons look almost disappointed."
)
# Design (judge brief, in order): the city is named and the weather is the
# whole point; the smile lands at the end, a surprising image that still
# makes sense — pigeons own the station, an on-time bus ruins their
# routine; the register never leaves broadcast weather ("11°C, drizzle
# till nine, then sun"); temperature and pigeons are the concrete details;
# 115 characters, nothing wasted.


def main() -> None:
    if not 1 <= len(LINE) <= 140 or not LINE.strip():
        raise SystemExit("line fails the 1-140 character gate")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(LINE, encoding="utf-8")
    print(LINE)


if __name__ == "__main__":
    main()
