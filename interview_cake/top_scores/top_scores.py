"""
Write a function that takes:

a list of unsorted_scores
the highest_possible_score in the game
and returns a sorted list of scores in less than O(n\lg{n})O(nlgn) time.
"""

nums = [5, 3, 6]

# top = 1
# bottom = 0

# while top <= len(nums) - 1:
#     # import pdb

#     # pdb.set_trace()
#     if nums[bottom] > nums[top]:
#         top += 1
#         bottom += 1
#     else:
#         nums[bottom], nums[top] = nums[top], nums[bottom]
#         bottom = top
#         top += 1

# print(nums)

