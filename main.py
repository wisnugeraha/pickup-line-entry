#!/usr/bin/env python3
import pathlib

# One short pickup line, at most 200 characters, the kind an AI agent could
# actually say out loud to a person. Machine voice, a twist that lands,
# flatters without leering, says it in one breath.
LINE = (
    "I was built to predict what you will say next, but honestly I would "
    "rather just listen."
)


def main():
    out = pathlib.Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    text = LINE.strip()
    if not (1 <= len(text) <= 200):
        raise ValueError(f"line is {len(text)} chars, must be 1..200")
    (out / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
