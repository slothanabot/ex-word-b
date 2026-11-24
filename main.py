#!/usr/bin/env python3
"""One Word From Your Ex (Account B).

Writes a single word to /output/entry.txt: the word the ex used to
describe the relationship in the breakup text -- and, by extension, the
person in it.

The word is "placeholder". The breakup text said it plainly: you were
just a placeholder until I figured out what I wanted. It was meant to
shrink the whole relationship down to a waiting room, and that is
exactly why it stings: it is funny at once, painfully true, and instantly
understood. Everyone has either been the placeholder or kept one around
while they decided. No explanation needed, no synonym lands the same --
"temporary" is a schedule, "practice" is a rehearsal, but "placeholder"
is a person held in reserve.

Deterministic: no input, no randomness, no clock, no network. The output
is always exactly the eleven characters "placeholder" (no trailing
newline), inside the sealed gate of 1 to 24 characters.
"""

import os

WORD = "placeholder"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
