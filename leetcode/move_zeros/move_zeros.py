"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""


def move_zero_numbers(nums):
    new_nums = [0] * len(nums)

    i = 0
    for num in nums:
        if num:
            new_nums[i] = num
            i += 1

    for i in range(len(new_nums)):
        nums[i] = new_nums[i]

    return nums
