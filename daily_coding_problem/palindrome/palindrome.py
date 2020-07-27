"""
Given a string, determine whether any permutation of it is a palindrome.

For example, carrace should return true, since it can be rearranged to form racecar, which is a palindrome. daily should return false, since there's no rearrangement that can form a palindrome.
"""

# Option 1
def is_palindrome(string):
    string_length = len(string)
    if string_length <= 1:
        return False

    right_index = string_length - 1
    left_index = 0

    while left_index != right_index:
        if string[left_index] != string[right_index]:
            return False
        left_index += 1
        right_index -= 1

    return True


# Option 2
def is_palindrome(string):

    if len(string) <= 1:
        return True
    return string[0] == string[-1] and is_palindrome(string[1:-1])


# Option 3
from collections import Counter


def is_palindrome(string):

    letter_counter = Counter()

    for letter in string:
        letter_counter[letter] += 1

    total_single_letters = 0
    for number in letter_counter.values():
        if number == 1:
            total_single_letters += 1

    return total_single_letters == 1
