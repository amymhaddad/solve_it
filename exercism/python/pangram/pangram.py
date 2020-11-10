import re


def is_pangram(sentence):

    return (
        len(set(letter.lower() for letter in re.findall(r"[A-Za-z]", sentence))) == 26
    )
