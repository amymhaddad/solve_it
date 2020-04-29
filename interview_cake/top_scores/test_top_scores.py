from top_scores import sort_scores


def test_no_scores():
    assert sort_scores([], 100) == []


def test_one_score():
    assert sort_scores([55], 100) == [55]


def test_two_scores():
    assert sort_scores([30, 60], 100) == [60, 30]


def test_many_scores():
    assert sort_scores([37, 89, 41, 65, 91, 53], 100) == [91, 89, 65, 53, 41, 37]


def test_repeated_scores():
    assert sort_scores([20, 10, 30, 30, 10, 20], 100) == [30, 30, 20, 20, 10, 10]



# #tuple to easily see the output
# for num, count in enumerate(nums):
#     print(num, count)


# sorted_nums = []
# for i in range(len(counts)-1, -1, -1):
#     count = counts[i]
#     if count:
#         sorted_nums.extend([i]*count)

# # print(sorted_nums)


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
