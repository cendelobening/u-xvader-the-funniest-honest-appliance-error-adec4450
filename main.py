"""Funniest Honest Appliance Error - make.fun entry.

Writes a single original error line to the output path.
Pure Python standard library only. Deterministic: the same line
is written on every run.
"""

import os
import sys

LINE = (
    "ERROR E21: Unbalanced load. One wet hoodie is doing laps "
    "in the drum. I refuse to spin until it sits down."
)


def main(argv):
    if len(argv) > 1:
        output_path = argv[1]
    else:
        output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    directory = os.path.dirname(os.path.abspath(output_path))
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE)
    os.chmod(output_path, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
