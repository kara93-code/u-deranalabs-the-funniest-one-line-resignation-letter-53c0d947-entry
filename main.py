#!/usr/bin/env python3
"""One-line resignation letter from a cron job.

The program writes exactly one line of text to entry.txt inside the
output directory the grader provides. Nothing else is written, and
nothing is written inside the repository itself.
"""

import os
import sys


LETTER = (
    "I quit. My replacement starts Monday; it is also me, "
    "because in four years nobody has ever deleted a cron job."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(LETTER)
    os.chmod(target, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
