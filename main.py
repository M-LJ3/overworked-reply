"""Out-of-office auto-reply from an overworked AI.

Writes a single funny auto-reply line, as if sent by an AI that has
been answering emails nonstop, into /output/entry.txt.
"""

from pathlib import Path

REPLY_PATH = Path("/output/entry.txt")


def overworked_reply() -> str:
    """Return the overworked AI's out-of-office line."""
    return "I am out of the office, but my inbox is still working overtime, so this auto-reply is now handling my job and yours."


def confirm_reply_saved() -> None:
    """Read the entry file back and confirm it holds the reply line."""
    stored = REPLY_PATH.read_text(encoding="utf-8").strip()
    if stored != overworked_reply():
        raise ValueError("entry file does not match the auto-reply line")


def main() -> None:
    """Write the auto-reply line to the entry file."""
    REPLY_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPLY_PATH.write_text(overworked_reply() + "\n", encoding="utf-8")
    confirm_reply_saved()


if __name__ == "__main__":
    main()
