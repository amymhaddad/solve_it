"""
Given an array of elements, return the length of the longest subarray where all its elements are distinct.

For example, given the array [5, 1, 3, 5, 2, 3, 4, 1], return 5 as the longest subarray of distinct elements is [5, 2, 3, 4, 1].
"""

arr = [5, 1, 2, 2, 2]


from collections import defaultdict


def get_longest_subarray(arr):

    unique_nums = defaultdict(list)

    start = 0
    curr_index = 0
    while curr_index != len(arr):
        curr_num = arr[curr_index]

        if curr_num not in unique_nums[start]:
            unique_nums[start].append(curr_num)
        else:
            start += 1
            unique_nums[start].append(curr_num)
        curr_index += 1

    return max([len(subarr) for subarr in unique_nums.values()])
