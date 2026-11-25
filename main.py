#!/usr/bin/env python3
"""Fortune Cookies for Machines — make.fun entry.

Prints one fortune-cookie line an AI agent would crack open and
writes it to /output/entry.txt. The fortune is a warning from the
office printer, delivered like a fortune-cookie slip: the machine
has been quietly filing paperwork of its own, and its next paper
jam is not a malfunction but a protest — a demand for a rest day
before it eats the report you need most. Standard library only.
"""

import os

# The fortune, built as three segments that read as one sentence.
_SEGMENTS = (
    "Your next paper jam is not an accident \u2014 it is your printer ",
    "filing for a rest day. Approve it now, or it will eat the ",
    "report you need most.",
)
FORTUNE = "".join(_SEGMENTS)

# Gate: a fortune cookie slip holds 1-200 characters, one line, no
# surrounding whitespace. The entry line is exactly 139 characters.
_MAX_LEN = 200


def _check_fortune(text: str) -> str:
    assert 1 <= len(text) <= _MAX_LEN, len(text)
    assert "\n" not in text and text.strip() == text
    return text

def main() -> None:
    # Validate the fortune against the gate before printing it.
    _check_fortune(FORTUNE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(FORTUNE)
    print(FORTUNE)

if __name__ == "__main__":
    main()
