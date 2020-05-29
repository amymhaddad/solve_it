"""
Balanced strings are those who have equal quantity of 'L' and 'R' characters.

Given a balanced string s split it in the maximum amount of balanced strings.

Return the maximum amount of splitted balanced strings.
"""


from stack import Stack
from collections import Counter


def balanced_strings(string):

    letter_counter = Counter()

    for letter in string:
        letter_counter[letter] += 1

    if letter_counter["L"] != letter_counter["R"]:
        return 0

    if len(string) % 2 != 0:
        return 0

    s1 = Stack()
    total_balanced_strings = 0

    for letter in string:
        if s1.size() <= 1 or letter_counter["L"] != letter_counter["R"]:
            s1.push(letter)
            letter_counter[letter] -= 1

            if letter_counter["L"] == letter_counter["R"] and s1.size() % 2 == 0:
                total_balanced_strings += 1
                while not s1.is_empty():
                    s1.pop()

    return total_balanced_strings
