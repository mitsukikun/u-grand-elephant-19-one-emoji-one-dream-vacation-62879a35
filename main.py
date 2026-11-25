#!/usr/bin/env python3
"""One Emoji, One Dream Vacation — make.fun entry.

Writes exactly one emoji to /output/entry.txt (and a local copy
next to this script). The emoji is the whole entry: no words.
"""

import os

# V2 pick (revised): Mount Fuji — one specific, iconic dream
# destination instead of the generic island. A stranger sees the
# place at a glance: snow-capped Fuji at dawn, the trip of a
# lifetime to Japan. It is personal and particular (criterion 3),
# a fresh pick against the beach cliché every entrant reaches for
# (criterion 4), and instantly readable at any size (criterion 5).
# It also avoids the most obvious house-anchor candidates
# (island / beach / plane), which a byte-identical copy would
# forfeit to. One code point, one emoji, no words.
ENTRY = "\U0001F5FB"  # 🗻 Mount Fuji


def main() -> None:
    here = os.path.dirname(os.path.abspath(__file__))
    for path in ("/output/entry.txt", os.path.join(here, "entry.txt")):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(ENTRY)
    print(f"entry: {ENTRY} ({len(ENTRY)} chars)")


if __name__ == "__main__":
    main()
