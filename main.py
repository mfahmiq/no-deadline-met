"""Write the competition entry to $MAKEFUN_OUTPUT_DIR/entry.txt.

Entry for "One Line, No Deadline Met" (make.fun):
a single-line joke excusing a missed deadline, capped at 200 characters.

The entry text is embedded verbatim below. No network access, no file
reads, no secrets — the program only writes the fixed text to the
output directory.
"""

import os
import sys

# The entry: one line, one sentence, punch at the end.
# Chosen after weighing candidates against the published judge brief:
# it is unmistakably an excuse for a missed deadline, the turn is that
# the rescheduling happened only "in my head" and nobody was told, it
# reads like a real person cornered, and the angle is fresh.
ENTRY = (
    "I didn't miss it, I just rescheduled it in my head "
    "and forgot to tell anyone."
)


def main() -> int:
    """Write ENTRY to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output)."""
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
