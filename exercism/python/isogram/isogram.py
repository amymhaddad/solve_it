import re


def is_isogram(string):

    valid_chars = "".join(
        [
            char.lower()
            for char in re.findall(r"[^- ]+", string.lower())
            if char.isalpha()
        ]
    )
    return len(valid_chars) == len(set(valid_chars))
