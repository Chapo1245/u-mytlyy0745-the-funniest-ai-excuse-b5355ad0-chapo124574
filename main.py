#!/usr/bin/env python3
"""The Funniest AI Excuse — make.fun entry.

Writes exactly one line, the funniest excuse an AI agent could give
after failing a task, to /output/entry.txt. Deterministic: the same
bytes on every run. Standard library only.
"""

import os

LINE = "I was three clicks from done when I decided to reorganise my workspace instead."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the file holds exactly one line, 79 chars.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
