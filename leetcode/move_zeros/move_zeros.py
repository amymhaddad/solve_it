"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""


def move_zero_numbers(nums):
    index = 1
    num = 0

    while index < len(nums):
        if nums[num] == 0 and nums[index] == 0:
            index += 1

        elif nums[num] == 0:
            nums[num], nums[index] = nums[index], nums[num]
            index += 1
            num += 1

        else:
            index += 1
            num += 1

    return nums
