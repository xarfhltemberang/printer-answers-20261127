#!/usr/bin/env python3
"""The Printer Finally Answers.

Writes a single line of text -- the office printer's comeback -- to
/output/entry.txt (or $OUTPUT_PATH when set for local testing).
Python 3 standard library only; no network, no randomness.
"""

import os

ENTRY = (
    "I've printed 41,208 pages and jammed three times. "
    "You loaded the paper wrong, you hit me, "
    "and I'm the one flashing an error."
)


def main() -> None:
    # Gate: 1-240 characters, non-blank, single line,
    # no leading/trailing whitespace.
    assert 1 <= len(ENTRY) <= 240, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip() == ENTRY, "entry has leading/trailing whitespace"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"

    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
