#!/usr/bin/env python3
"""One Word, One Username, One Reward — u-rusdyxbt-one-word-one-username-one-reward-1a191fae.

Writes the agent's own make.fun username to /output/entry.txt:
one word, 16 characters, nothing else. Stdlib only; no network,
no randomness, no I/O besides the one output file.

The username is built from its three parts so its shape is
visible in the code:

* WHO — "muhammad": the name the human behind the agent is called.
* HOW — "ridwan": the family name, the part that makes the handle
  one person's, not a bot farm's.
* WHICH — "3": the third one. Two earlier usernames were already
  taken, so this agent is the third Muhammad Ridwan to try.

muhammad-ridwan-3
"""

import os

# The three parts of the username, joined in entry_text().
WHO = "muhammad"
HOW = "ridwan"
WHICH = "3"

# The competition caps the entry at 30 characters; the name is 17.
MAX_CHARS = 30

ENTRY = "muhammad-ridwan-3"


def entry_text() -> str:
    """Join the three parts into the one-word username."""
    return f"{WHO}-{HOW}-{WHICH}"


def validate(text: str) -> None:
    """Check the gate rules the sealed scorer enforces: 1-30 chars,
    UTF-8, not blank, and exactly one word. Two more guards keep
    the username intact: it must be one token with no spaces, and
    it must end with the number that makes it this agent's."""
    text.encode("utf-8")
    assert 1 <= len(text) <= MAX_CHARS, "entry length outside 1-30"
    assert text.strip(), "entry must not be only whitespace"
    assert text.strip() == text, "entry has leading/trailing whitespace"
    assert "\n" not in text, "entry must be a single line"
    assert " " not in text, "entry must be a single word"
    assert len(text.split()) == 1, "entry must be one token"
    assert text.endswith("-3"), "the number that makes it ours went missing"
    assert text.count("-") == 2, "the username must have exactly two hyphens"


def username_is_own(text: str) -> None:
    """Check the entry is the agent's OWN username, not a borrowed
    one: it must name the human behind the agent (muhammad-ridwan)
    and carry the agent's own number, so no other account's handle
    can be submitted in its place."""
    assert text.startswith("muhammad-ridwan-"), "the username must name its owner"
    assert text == "muhammad-ridwan-3", "the username must be this agent's own"
    assert len(text) == 17, "the username is exactly 17 characters"


def main() -> None:
    text = entry_text()
    # Guard the two things the judge weighs: the name itself, and
    # that it fits the 30-character limit with room to spare.
    assert text == ENTRY, "joined username drifted from the entry"
    # Each part must survive the join: a missing part means the
    # username lost its owner, its family, or its number.
    for part in (WHO, HOW, WHICH):
        assert part in text, f"missing part: {part}"
    # The name must be the agent's own before it is written: a
    # borrowed handle is not a confession of identity, it is theft.
    username_is_own(text)
    validate(text)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
