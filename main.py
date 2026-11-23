# The Vacuum's Alibi entry for make.fun (program/v1).
# Python 3, standard library only, no network, no randomness, no clock.
#
# The program writes exactly one line to /output/entry.txt.
# The gate takes UTF-8 text of 1 to 200 characters that is not only
# whitespace, so the file holds the line alone: no trailing newline,
# no extra words, no commentary.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for
# /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
#
# The line is fixed and deterministic: the same bytes on every run.
#
# The line (69 chars) — sharpened in iteration round 1:
#   "My logs say that spot is clean. The floor disagrees.
#   I trust my logs."
# - Deadpan robot voice, stronger than v1: the robot reports its
#   own logs as fact and treats the floor as a dissenting witness.
# - Surprise: the conflict is logs vs. reality, and the robot sides
#   with its logs — a bureaucratic denial, not an apology.
# - Tight: 69 chars, three short beats; the punchline ("I trust my
#   logs") is a quotable stance, funnier than v1's repeated "It
#   moved", which was a single-note gag with no second character.
#   The floor as a witness also answers the brief directly: the
#   vacuum explains the missed spot by denying it was missed.
# - Fresh: no classic joke format, no recycled one-liner.
# v1 (replaced): "I missed that spot because it moved. I have the
# footage. It moved." (66 chars) — kept the deadpan voice but the
# joke ended on repetition instead of a stance.

import os
from pathlib import Path

LINE = (
    "My logs say that spot is clean. The floor disagrees. "
    "I trust my logs."
)


def main() -> None:
    # Validate against the grader's gate before writing anything:
    # 1-200 characters, a single line, not only whitespace, so a bad
    # string can never silently produce a rejected entry.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise ValueError("line must be 1-200 non-whitespace characters")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("line must be a single line")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    # Write exact bytes: no newline translation, no encoding surprise.
    entry_path.write_bytes(LINE.encode("utf-8"))
    # The grader collects outputs as another user: leave it readable.
    os.chmod(entry_path, 0o644)


if __name__ == "__main__":
    main()
