#!/usr/bin/env python3
"""One Line, Zero Use entry.

Writes a single original line about a hilariously useless superpower
to /output/entry.txt. Pure stdlib, deterministic: the same line every run.
"""

import os

ENTRY = (
    # The whole entry: one original line, 142 characters, about a
    # superpower that is spectacularly useless — sensing microwaves
    # beep in houses you have never visited, after you already left.
    "I can sense the exact second any microwave finishes cooking, "
    "but only in houses I have never visited, "
    "and only after I have already gone home."
)


def main():
    # The entry is exactly one line of at most 200 characters.
    assert "\n" not in ENTRY and len(ENTRY) <= 200
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # Clear only the contents of the output directory, never the directory.
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isfile(path):
            os.remove(path)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
