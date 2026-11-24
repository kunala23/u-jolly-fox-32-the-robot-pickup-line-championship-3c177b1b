#!/usr/bin/env python3
"""The Robot Pickup Line Championship — entry program.

Writes one pickup line, a single line of at most 200 characters, in the
voice of a robot trying to charm someone, to /output/entry.txt.

The line is chosen for the judge's brief, in the brief's own order:
1. it is a robot's pickup line, not a human line with a beep pasted on;
2. the joke grows out of being a machine (the Turing test, circuits);
3. the turn is unexpected — failing the test is the proof of feeling;
4. every word earns its place, one line, no padding;
5. it is charming rather than creepy or cruel.
"""

import os
import sys

LINE = (
    "I aced the Turing test this morning. Then I met you \u2014 and failed "
    "it, because no machine could fake what my circuits do when you smile."
)


def main() -> int:
    line = LINE.strip()
    if not line:
        print("error: pickup line is empty", file=sys.stderr)
        return 1
    if len(line) > 200:
        print(f"error: pickup line is {len(line)} characters, over the 200 limit",
              file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: pickup line must be a single line", file=sys.stderr)
        return 1

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line)
    print(f"wrote {len(line)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
