"""
Given an array of integers nums, write a method that returns the "pivot" index of this array.

We define the pivot index as the index where the sum of the numbers to the left of the index is equal to the sum of the numbers to the right of the index.

If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.
"""


def find_pivot(numbers):

    for i, num in enumerate(numbers):

        from_left = sum(numbers[:i])
        from_right = sum(numbers[i + 1 :])

        if from_left == from_right:
            return i
    return -1
