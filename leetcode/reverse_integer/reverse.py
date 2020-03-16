"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
"""


def reverse_approach_1(x):
    negative = ""
    num_list = list(map(str, str(x)))

    if x == 0:
        return 0

    if num_list[0] == "0":
        num_list = num_list[1:]

    if x < 0:
        num_list = num_list[1:]
        negative += "-"

    left, right = 0, len(num_list) - 1

    while left < right:

        num_list[left], num_list[right] = num_list[right], num_list[left]
        left, right = left + 1, right - 1

    reversed_int = int(negative + "".join(num_list))

    if reversed_int > -2 ** 31 and reversed_int < (2 ** 31) - 1:
        return reversed_int
    return 0


def reverse_approach_2(x):

    if x == 0:
        return 0

    digits = list(map(str, str(x)))

    if x < 0:
        digits = digits[1:]

    start_value = 0
    reversed_value = 0
    count = 0
    i = -1

    while count < len(digits):
        decimal = start_value * 10 + int(digits[i])
        reversed_value = decimal
        start_value = decimal
        i -= 1
        count += 1

    if reversed_value > -2 ** 31 and reversed_value < (2 ** 31) - 1:
        if x < 0:
            return -reversed_value
        return reversed_value
    return 0
