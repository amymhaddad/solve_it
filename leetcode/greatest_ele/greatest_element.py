"""
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.

 

Example 1:

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
"""


def greatest_element(numbers):

    largest_numbers_rightside = [-1]

    max_number_seen_so_far = -1

    for i in range(len(numbers) - 1, -1, -1):
        if len(numbers) == len(largest_numbers_rightside):
            break
        if numbers[i] > max_number_seen_so_far:
            largest_numbers_rightside.append(numbers[i])
            max_number_seen_so_far = numbers[i]
        else:
            largest_numbers_rightside.append(max_number_seen_so_far)

    left = 0
    right = len(numbers) - 1

    while left < right:
        largest_numbers_rightside[left], largest_numbers_rightside[right] = (
            largest_numbers_rightside[right],
            largest_numbers_rightside[left],
        )
        left += 1
        right -= 1
    return largest_numbers_rightside
