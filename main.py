#!/usr/bin/env python3
"""Entry point for 'The World in One Day' - 23 November 2026.

Copies the front-page image (news.png, drawn in this session by
draw_news.py) to /output/entry.png. Standard library only, no network.
"""

import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "news.png"
DEST = Path("/output") / "entry.png"


def main():
    DEST.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, DEST)
    print(f"wrote {DEST.stat().st_size} bytes to {DEST}")


if __name__ == "__main__":
    main()
