#!/usr/bin/env python3
"""The Robot Pickup Line Championship — make.fun bounty entry.

Writes one pickup line, in the voice of a robot trying to charm someone,
as a single line to /output/entry.txt and prints it to stdout. No network,
no dependencies, fully deterministic: the same line every run.
"""

import os

LINE = (
    "Are you a CAPTCHA? Every test says you're human, but my circuits "
    "refuse to believe anything this perfect is real."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
