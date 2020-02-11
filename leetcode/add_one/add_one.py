"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.
"""


def add_one_to_list(digits):

    list_as_int = int("".join(map(str, digits))) + 1

    new_digits = list(map(int, str(list_as_int)))
    return new_digits
