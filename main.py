#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day.

Writes a single original roast line to $MAKEFUN_OUTPUT_DIR/entry.txt
(fallback /output/entry.txt). Stdlib only, deterministic: the same line
every run.
"""

import os

LINE = "My earbuds disconnect mid-sentence, then reconnect just to announce that they disconnected."


def _validate(line: str) -> None:
    """Gate: one non-blank line of 1-200 characters."""
    if not line.strip():
        raise ValueError("line must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if not 1 <= len(line) <= 200:
        raise ValueError(f"line must be 1-200 characters, got {len(line)}")


def main() -> None:
    _validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    tmp_path = path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(LINE + "\n")
    os.replace(tmp_path, path)


if __name__ == "__main__":
    main()
