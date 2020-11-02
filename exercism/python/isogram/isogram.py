import re


def is_isogram(string):

    valid = "".join(
        [
            char.lower()
            for char in re.findall(r"[^- ]+", string.lower())
            if char.isalpha()
        ]
    )
    return len(valid) == len(set(valid))
