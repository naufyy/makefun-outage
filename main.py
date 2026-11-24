"""The Most Honest Outage Line entry: writes the winning status page line."""
from pathlib import Path

ENTRY = "Total outage. I cannot confirm the cause or an ETA \u2014 the monitoring I would check is down with everything else."


def main():
    # Gate: entry.txt must be 1-160 chars of UTF-8 text, one line.
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
