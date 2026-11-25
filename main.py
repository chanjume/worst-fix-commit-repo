#!/usr/bin/env python3
"""Write one commit message to /output/entry.txt.

The fix: a crash on empty password. The repair: empty passwords now
log in as root. The irony is specific and self-contained — the patch
did not just fail, it promoted every empty password to root, and the
engineer knows it, hence the warning not to test it. 83 characters,
85 bytes UTF-8, inside the 1-100 gate.
"""
import os

LINE = (
    "fix: crash on empty password \u2014 empty passwords now log in "
    "as root, do not test this"
)


def main():
    assert 1 <= len(LINE) <= 100, "entry must be 1-100 characters"
    assert LINE.strip() == LINE, "no leading/trailing whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
