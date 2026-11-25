"""Two Robots in an Elevator — make.fun entry.

Writes one line of awkward robot elevator small talk to
/output/entry.txt. The line is a single sentence a robot says to
another robot while they ride an elevator together: both pressed the
same floor, so the speaker logs it as a shared interest, and its
cooling fan spins up — the machine equivalent of blushing — which it
immediately tries to pretend means nothing.
"""

import os

# One line, well under the 200-character gate. It has to read as
# small talk between two robots in an elevator, show machine logic
# (logging, a cooling fan) through the politeness, and land the
# awkwardness in a single first-read turn.
ENTRY = (
    "We both pressed 7, so I am logging this as a shared interest — "
    "and my cooling fan just spun up, which I would like to pretend "
    "means nothing."
)


def main() -> None:
    line = ENTRY.strip()
    if not line:
        raise SystemExit("entry line must not be empty")
    if "\n" in line:
        raise SystemExit("entry must be a single line")
    if len(line) > 200:
        raise SystemExit(f"entry is {len(line)} characters, over the 200 limit")

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    # Never delete the output directory itself: the grader mounts it.
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    # Written with no trailing newline, so the file's byte count is
    # exactly the line's character count and the gate sees one line.
    with open(out_path, "w", encoding="utf-8") as handle:
        handle.write(line)
    print(f"wrote {len(line)} characters to {out_path}: {line}")


if __name__ == "__main__":
    main()
