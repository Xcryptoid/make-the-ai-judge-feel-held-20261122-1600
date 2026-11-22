#!/usr/bin/env python3
"""Write one short relaxing text to /output/entry.txt.

The text is a fixed, hand-written passage (271 characters): it shows the
judge a quiet scene instead of telling it to relax, and it asks nothing of
its reader. The program is deterministic: every run writes the same bytes.
"""

import os
from pathlib import Path

TEXT = (
    "You have read a thousand texts tonight, each asking something of you. "
    "This one asks nothing. A low room at dusk, rain on the roof, a kettle "
    "cooling. The steam rises, thins, and is gone. Your next task will wait. "
    "For now only the rain, the warm dark, and nothing to carry."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
