"""Write one original one-line commit message to /output/entry.txt (UTF-8).

Standard library only. The message is a single line of 111 characters:
the funniest thing an AI agent would write right after breaking
production at 3 AM.

Second pass: "confidence was 0.99" tightened to the bare status-line
fragment "confidence 0.99" — a model would report its confidence as a
bare number, and the three fragments after the semicolon then read as
one status report (prod back / confidence 0.99 / test suite asleep),
which lands the joke harder than a full clause.
"""

import pathlib

MAX_CHARS = 200

ENTRY = "revert: my 3am deploy dropped the users table; prod is back from backup, confidence 0.99, test suite was asleep"


def main():
    text = ENTRY
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= MAX_CHARS, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only whitespace"
    # No trailing newline: entry.txt holds exactly the commit message.
    out_dir = pathlib.Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(text, encoding="utf-8")
    # Round-trip check: read it back and assert byte-identical.
    round_tripped = out_path.read_bytes()
    assert round_tripped == text.encode("utf-8"), "round-trip mismatch"
    print(f"Wrote {len(text)} characters to {out_path}")


if __name__ == "__main__":
    main()
