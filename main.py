import os
import sys

REVIEW_TEXT = "One star. He moved my bowl two inches left. I have starved for three days beside a full bowl, out of principle."

FALLBACK_TEXT = "One star. My bowl was empty at 3am. I woke my human. He called me dramatic."

MAX_CHARS = 200

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def validate(text):
    lines = text.splitlines()
    if len(lines) != 1:
        return False
    if not 1 <= len(lines[0]) <= MAX_CHARS:
        return False
    return True


def pick_entry():
    if validate(REVIEW_TEXT):
        return REVIEW_TEXT
    return FALLBACK_TEXT


def main():
    entry = pick_entry()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(entry + "\n")


if __name__ == "__main__":
    main()
