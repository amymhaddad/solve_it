"""
Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise. 

Return the number of negative numbers in grid.

Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
"""


def get_negative_numbers(grid):
    count = 0

    for i, matrix in enumerate(grid):
        for num in matrix:
            if num < 0:
                count += 1
    return count
