"""
Given an array of integers nums.

A pair (i,k) is called good if nums[i] == nums[k] and i < k.

Return the number of good pairs.

 

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

"""

from collections import Counter


def goodPairs(nums):
    counts = Counter(nums)
    return sum([count * (count - 1) // 2 for num, count in counts.items()])
