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


def resolve_output_path() -> str:
    """Return the full path of entry.txt.

    MAKEFUN_OUTPUT_DIR is a directory; if it already names the file
    itself (ends with entry.txt), use it as-is, otherwise join it.
    The unset-variable fallback is the /output directory.
    """
    raw = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    if raw.endswith("entry.txt"):
        return raw
    return os.path.join(raw, "entry.txt")


def main() -> None:
    path = resolve_output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
