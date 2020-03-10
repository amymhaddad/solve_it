"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
"""

from collections import Counter


def unique_approach_1(s):
    letter_count = {}
    for i, letter in enumerate(s):
        letter_count[letter] = letter_count.get(letter, 0) + 1

    for letter, count in letter_count.items():
        if count == 1:
            return s.index(letter)

    return -1


def unique_approach_2(s):
    letter_count = Counter(s)

    for letter, count in letter_count.items():
        if count == 1:
            return s.index(letter)
    return -1
