"""
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
"""

# Option 1
def two_sum_approach_1(numbers, target):

    total_indexes = {}
    for i, num in enumerate(numbers, 1):
        total_indexes[num] = i

        complement = target - num
        if complement in total_indexes:
            return [total_indexes[complement], i]


# Option 2
def two_sum_approach_2(numbers, target):
    total_indexes = {}

    for i, num in enumerate(numbers, 1):
        total_indexes[num] = i

        try:
            return [total_indexes[target - num], i]

        except KeyError:
            total_indexes[target - num] = i

    return None


print(two_sum_approach_2([2, 7, 11, 15], 9))
