"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
"""


def insert_position(nums, target):
    if target in nums:
        return nums.index(target)

    low = 0
    high = len(nums) - 1

    if not nums or target < nums[low]:
        return 0
    elif target > nums[high]:
        return high + 1

    while high - low > 1:
        mid = (low + high) // 2

        if nums[mid] < target:
            low = mid

        else:
            high = mid
    return high
