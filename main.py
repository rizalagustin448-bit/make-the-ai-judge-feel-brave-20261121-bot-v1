"""Make the AI judge feel brave — entry writer.

Writes one short text to /output/entry.txt: a quiet night scene that
slows the reader down instead of telling them to relax.
"""

import os
from pathlib import Path

TEXT = (
    "The kettle ticks as it cools. "
    "Rain spells itself out on the tin roof, one drop, then another. "
    "The dog sighs in his sleep. "
    "Out past the headland, a lighthouse turns its light around again."
)


def validate(text):
    """Gate: 1-280 Unicode code points, not only whitespace."""
    if not 1 <= len(text) <= 280:
        raise ValueError(f"entry must be 1-280 chars, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    return text


def main():
    validate(TEXT)
    out = Path(os.environ.get("OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")
    # Read back and re-validate what the sandbox will grade.
    validate(out.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
