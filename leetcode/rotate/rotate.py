"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
"""


def rotate_nums_approach_1(nums, k):
    nums_length = len(nums)
    rotate = [None] * nums_length

    for i, num in enumerate(nums):
        new_index = (i + k) % nums_length
        rotate[i] = nums[new_index]

    for i in range(nums_length):
        nums[i] = rotate[i]

    return nums
