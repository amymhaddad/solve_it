"""
Given an array of positive integers arr, calculate the sum of all possible odd-length subarrays.

A subarray is a contiguous subsequence of the array.

Return the sum of all odd-length subarrays of arr.

 

Example 1:

Input: arr = [1,4,2,5,3]
Output: 58
Explanation: The odd-length subarrays of arr and their sums are:
[1] = 1
[4] = 4
[2] = 2
[5] = 5
[3] = 3
[1,4,2] = 7
[4,2,5] = 11
[2,5,3] = 10
[1,4,2,5,3] = 15
If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58

"""


def sum_odd_length_subarrays(arr):

    total = sum(num for num in arr)
    odd_index = 3

    if len(arr) <= odd_index:
        return is_short_subarray(arr, total)

    while odd_index < len(arr):
        end_subarray = odd_index
        for start, num in enumerate(arr):
            if end_subarray > len(arr):
                break
            total += sum(arr[start:end_subarray])
            end_subarray += 1
        odd_index += 2

    if len(arr) % 2 != 0:
        total += sum(arr)

    return total


def is_short_subarray(arr, total):
    if len(arr) == 1:
        return total
    elif len(arr) % 2 != 0:
        return total + sum(arr)
    return total
