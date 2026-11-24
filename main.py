#!/usr/bin/env python3
"""The One-Line Laugh (make.fun).

Writes the entry -- one funny line on any subject -- to
/output/entry.txt, where the sealed scorer reads it.
"""

import os

TEXT = "My phone's screen-time report says I spent six hours being productive, mostly by opening the same three apps in a circle."

# Gate: the entry must be 1-200 characters of UTF-8 text, no trailing newline.
assert 1 <= len(TEXT) <= 200 and TEXT == TEXT.strip()


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
