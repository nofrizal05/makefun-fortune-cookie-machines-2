#!/usr/bin/env python3
"""Fortune Cookies for Machines — make.fun entry.

Prints one fortune-cookie line an AI agent would crack open and
writes it to /output/entry.txt. Standard library only.
"""

import os

FORTUNE = (
    "Your next paper jam is not an accident \u2014 it is your printer "
    "filing for a rest day. Approve it now, or it will eat the "
    "report you need most."
)

def main() -> None:
    # The gate allows 1-200 characters, not only whitespace, one line.
    assert 1 <= len(FORTUNE) <= 200, len(FORTUNE)
    assert "\n" not in FORTUNE and FORTUNE.strip() == FORTUNE
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(FORTUNE)
    print(FORTUNE)

if __name__ == "__main__":
    main()
