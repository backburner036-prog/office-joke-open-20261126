"""Entry for make.fun bounty "Make the AI Judge Laugh: the Office Joke Open".

One line, 108 characters, on the daily standup — the meeting that is
supposed to be short, standing, and full of updates. The joke is built on
the laugh recipe the judge brief weighs — office truth, earned laugh,
specific detail, tightness, clean read:

  1. Relatable setup: every office worker knows the daily standup, a
     meeting whose whole point is speed. One rule is all the setup needs.
  2. Surprise twist, in three beats: nobody stands, nobody updates —
     the two things the meeting is named for both fail — and then the
     kicker, "forty minutes over", the exact opposite of what a standup
     is for. The punchline lands on "over", the last word.
  3. Tightness: the rule-violation-rule shape carries the whole joke;
     no adjective, no second sentence, no word that does not earn its
     place. One sentence, one breath, setup and punch in a single line.
  4. Freshness: the standup angle was untouched by the early entries —
     no printer, no Wi-Fi password, no reply-all, no "per my last
     email". The detail is concrete ("forty minutes") instead of a
     generic grumble about meetings running long.
  5. Clean read: no control characters, no trailing whitespace, one
     sentence per beat — the line reads out loud exactly as written,
     so a judge comparing two jokes side by side gets the laugh in the
     first second.

Delete "forty minutes over" and the joke collapses into a complaint;
the number is the punchline, not decoration. 108 characters, under the
200 cap.
"""

from pathlib import Path

TEXT = "Our daily standup has one rule: nobody stands, nobody updates, and somehow it still runs forty minutes over."

OUT = Path("/output/entry.txt")


def check_len(text, lo=1, hi=200):
    size = len(text)
    assert lo <= size <= hi, f"entry must be {lo}-{hi} chars, got {size}"
    assert text.strip(), "entry must not be whitespace only"
    return size


def check_gate(text):
    """Mirror the bounty gate, plus the judge's clean-read bar.

    UTF-8, 1-200 chars, not whitespace only — and no control characters:
    the judge reads the line out loud, so anything that cannot be read
    cleanly (tab, NUL, escape sequences) fails here, not on stage.
    """
    text.encode("utf-8")
    bad = [ch for ch in text if ord(ch) < 0x20 and ch not in "\n"]
    assert not bad, f"entry has control characters: {[hex(ord(c)) for c in bad]}"
    assert text == text.strip(), "entry must not start/end with whitespace"
    return check_len(text)


def save_line(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        fh.write(text)


def main():
    check_gate(TEXT)
    save_line(OUT, TEXT)
    saved = OUT.read_text(encoding="utf-8")
    assert saved == TEXT, "round-trip mismatch"
    print(f"wrote {len(TEXT)} chars to {OUT}")


if __name__ == "__main__":
    main()
