"""
Write a function that takes:

a list of unsorted_scores
the highest_possible_score in the game
and returns a sorted list of scores in less than O(n\lg{n})O(nlgn) time.
"""


# unsorted_scores = [50, 20, 60, 20]

# Approach 1
def sort_scores(unsorted_scores, highest_possible_score):

    counts = {}

    scores = ""

    for num in unsorted_scores:
        counts[num] = counts.get(num, 0) + 1

    for num in range(highest_possible_score, 0, -1):
        if num in counts:
            while counts[num] != 0:
                scores += str(num) + " "
                counts[num] -= 1

    return [scores]


# Approach 2


nums = [2, 7, 8, 1, 8]

max_score = 10

counts = max_score * [0]

for num in range(0, max_score):
    if num in nums:
        repeats = nums.count(num)

        if repeats > 0:
            counts[num] += repeats
            repeats -= 1

#tuple to easily see the output 
for num, count in enumerate(nums):
    print(num, count)


sorted_nums = []
for i in range(len(counts)-1, -1, -1):
    count = counts[i]
    if count:
        sorted_nums.extend([i]*count)

# print(sorted_nums)

 



# for i in range(len(counts), 0, -1):

#     num = counts[i - 1]

#     if num > 0:

#     # import pdb

#     # pdb.set_trace()
#     # nums[index] = i
#     # index += 1
#     num -= 1
# print(num)

# print(nums)


# for i, index in enumerate(counts):

#     if counts[i] > 0:
#         print(index)

#         #     import pdb

#         # pdb.set_trace()
#         nums[index] = i
# print(nums)
# [0, 1, 1, 0, 1, 0, 0, 1, 0, 0]



# See if the score is in the range of numbers. IF it is, then iterate through the nubmer of times it's included

# nums = [4, 8, 4, 2]

# counts = []

# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# Create an array with values set to 0
# My index is the key in an array -- it is still a hash
# >>> counts = 100*[0]

# At postion 50 increment the value 1
# >>> counts[50] += 1

# >>> counts[20] += 1
# >>> counts[60] += 1
# >>> counts
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# >>> counts[60] += 1
# >>> counts
