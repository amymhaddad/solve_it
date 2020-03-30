"""
A pangram is a phrase which contains every letter at least once, such as “the quick brown fox jumps over the lazy dog”. Write a function which determines if a given string is a pangram.
"""

from string import ascii_lowercase as alpha


string = "the QuicK brown fox jumps over the lazy dog"


def is_pangram_approach_1(string):

    return set(alpha.lower()).issubset(set(string.lower()))


def is_pangram_approach_2(string):

    count = 0
    for letter in alpha.lower():
        if letter in string.lower():
            count += 1

    if count == len(alpha):
        return True
    return False


def is_pangram_approach_3(string):
    letter_counts = dict.fromkeys(string.lower(), 0)

    for letter in alpha.lower():
        try:
            letter_counts[letter] = letter_counts.get(letter, 0) + 1
        except KeyError:
            return False
    return True
