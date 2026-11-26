#!/usr/bin/env python3
"""Deadpan forecast for Puddleton, a city that does not exist.

Renders one deadpan weather line (128 characters, inside the 160 limit)
from a template filled with the town's weather facts, checks the gate,
and writes it to /output/entry.txt.

Anchor (quoted before the first write of this file): drand quicknet
chain 52db9ba70e0cc0f6eaf7803dd07447a1f5477735fd3f661792ba94600c84e971,
round 34290586.
"""

from pathlib import Path

# One template, filled from the facts below. The joke lives in the
# facts, not in the code: rain that picks a single house, ordinary
# weather everywhere else, and a town that long ago stopped noticing.
TEMPLATE = (
    "In {city}, rain falls only on the mayor's house; "
    "elsewhere {temp} degrees and dry, "
    "and nobody in town finds this strange anymore."
)

FACTS = {
    "city": "Puddleton",
    "temp": 14,
}

OUTPUT_PATH = Path("/output/entry.txt")
MAX_CHARS = 160


def render() -> str:
    """Fill the template with the town's weather facts."""
    return TEMPLATE.format(**FACTS)


def is_valid(text: str) -> bool:
    """The sealed scorer's gate: UTF-8 text of 1 to 160 characters."""
    return bool(text.strip()) and len(text) <= MAX_CHARS


def main() -> None:
    text = render()
    if not is_valid(text):
        raise SystemExit(f"forecast fails the gate at {len(text)} characters")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    if OUTPUT_PATH.read_text(encoding="utf-8") != text:
        raise SystemExit("read-back differs from the forecast")
    print(f"Wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
