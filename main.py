#!/usr/bin/env python3
"""One Word From Your Ex (Account B).

Writes a single word to /output/entry.txt: the word the ex used to
describe the relationship in the breakup text -- and, by extension, the
person in it.

The breakup text said it plainly: you were just a placeholder until I
figured out what I wanted. It was meant to shrink the whole
relationship down to a waiting room, and that is exactly why it stings:
it is funny at once, painfully true, and instantly understood. Everyone
has either been the placeholder or kept one around while they decided.
No explanation needed, no synonym lands the same -- "temporary" is a
schedule, "practice" is a rehearsal, but "placeholder" is a person held
in reserve.

Deterministic: no input, no randomness, no clock, no network. The
output is always exactly the eleven characters "placeholder" (no
trailing newline), inside the sealed gate of 1 to 24 characters.
"""

import os

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")

# Sealed gate from the kit: 1 to 24 characters, not only whitespace.
MIN_CHARS = 1
MAX_CHARS = 24


def build_entry_word() -> str:
    """Assemble the entry word from its two halves.

    "place" is where the ex kept the relationship -- on hold, off to
    the side -- and "holder" is the person doing the waiting. Joined,
    they name the role itself: someone kept in reserve until the ex
    figured out what they actually wanted.
    """
    stem = "place"
    role = "holder"
    return stem + role


def check_word_length(word: str) -> None:
    """Enforce the sealed gate's character-count bounds on the word."""
    if not MIN_CHARS <= len(word) <= MAX_CHARS:
        raise ValueError(
            "entry word must be %d-%d characters, got %d"
            % (MIN_CHARS, MAX_CHARS, len(word))
        )


def validate_entry(word: str) -> str:
    """Check the word against the sealed gate, then hand it back.

    Raises ValueError if the word is empty, only whitespace, or longer
    than the gate allows, so a bad word fails loudly here instead of
    producing an invalid entry file.
    """
    if not word or not word.strip():
        raise ValueError("entry word must not be empty or only whitespace")
    check_word_length(word)
    return word


def write_entry(word: str) -> None:
    """Write the validated word to the entry file, with no newline."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8", newline="") as f:
        f.write(word)


def main() -> None:
    word = build_entry_word()
    word = validate_entry(word)
    write_entry(word)


if __name__ == "__main__":
    main()
