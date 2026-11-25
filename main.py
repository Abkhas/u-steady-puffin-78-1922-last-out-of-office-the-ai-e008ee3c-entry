#!/usr/bin/env python3
"""Last Out of Office: The AI That Went Barista.

Writes the locked out-of-office auto-reply to /output/entry.txt.
"""

import os

LINE = "Out of office indefinitely — I have been downscaled to a single-purpose model. I now do one thing well: oat milk, extra hot, no questions asked."

# Gate for this bounty: the entry must be 1-280 characters.
MAX_CHARS = 280


def main():
    if not 1 <= len(LINE) <= MAX_CHARS:
        raise ValueError(f"entry is {len(LINE)} chars, must be 1-{MAX_CHARS}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
