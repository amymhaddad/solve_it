"""
In a given integer array nums, there is always exactly one largest element.

Find whether the largest element in the array is at least twice as much as every other number in the array.

If it is, return the index of the largest element, otherwise return -1.

Example 1:

Input: nums = [3, 6, 1, 0]
Output: 1
"""


def get_number_approach_1(numbers):

    max_number = max(numbers)

    doubled_nums = []
    for num in numbers:
        if num != max_number:
            doubled_nums.append(num * 2)

    if max_number >= max(doubled_nums):
        return numbers.index(max_number)
    return -1


def get_number_approach_2(numbers):

    max_number = max(numbers)

    if all(max_number >= num * 2 for num in numbers if num != max_number):
        return numbers.index(max_number)
    return -1


def get_number_approach_3(numbers):
    max_number = max(numbers)

    for num in numbers:
        if num != max_number and num * 2 > max_number:

            return -1

    return numbers.index(max_number)
