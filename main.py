#!/usr/bin/env python3
"""One-line joke about working beside AI coding agents.

Writes exactly one line of joke text to $MAKEFUN_OUTPUT_DIR/entry.txt
(falling back to /output/entry.txt when the variable is unset).
Deterministic: the output is a fixed literal, so repeated runs are
byte-identical. No network access.
"""

import os

JOKE = (
    "Live on stage, my agent confidently called an API that doesn't exist "
    "\u2014 then blamed the docs for not keeping up with it."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output/entry.txt"
    # MAKEFUN_OUTPUT_DIR is a directory; /output/entry.txt is the fallback path.
    if output_dir.endswith("entry.txt"):
        path = output_dir
        directory = os.path.dirname(path)
    else:
        directory = output_dir
        path = os.path.join(directory, "entry.txt")
    os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
