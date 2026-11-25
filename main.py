"""The 3 AM Excuse — make.fun text entry.

Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
not only white space. This entry is 107 characters.
"""

import os

ENTRY = "My secure element clocked out at midnight and it holds grudges. I do not wake it up for a 3 AM impulse buy."


def main():
    text = ENTRY
    assert isinstance(text, str)
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only white space"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)  # no trailing newline


if __name__ == "__main__":
    main()
