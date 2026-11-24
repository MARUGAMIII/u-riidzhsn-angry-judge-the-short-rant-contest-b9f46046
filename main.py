#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest.

Writes one short, funny rant about an everyday annoyance to
/output/entry.txt. Stdlib only, no network, deterministic.
"""

import os

# Contest limits for a short rant entry.
MIN_CHARS = 1
MAX_CHARS = 400

RANT = (
    'The self-checkout just accused me of stealing my own bananas. '
    '"Unexpected item in the bagging area." THE BANANAS ARE THE ITEM. '
    'I scanned them. You watched me scan them. Now a human has to walk '
    'over and press one button to confirm I am not a banana criminal.'
)


def validate(text: str) -> str:
    """Return the entry text after enforcing the contest gates.

    Gates: must be a string, must not be blank/whitespace-only, must be
    1-400 characters, and must round-trip through UTF-8 cleanly.
    """
    if not isinstance(text, str):
        raise TypeError(f"rant must be str, got {type(text).__name__}")
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("rant must not be empty or whitespace-only")
    if not (MIN_CHARS <= len(cleaned) <= MAX_CHARS):
        raise ValueError(
            f"rant must be {MIN_CHARS}-{MAX_CHARS} characters, "
            f"got {len(cleaned)}"
        )
    if cleaned.encode("utf-8").decode("utf-8") != cleaned:
        raise ValueError("rant is not valid UTF-8 text")
    return cleaned


def resolve_output_path() -> str:
    """Resolve the entry file path, creating the output dir if needed."""
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main() -> None:
    text = validate(RANT)
    path = resolve_output_path()
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to {path}")


if __name__ == "__main__":
    main()
