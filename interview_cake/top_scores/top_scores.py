"""
Write a function that takes:

a list of unsorted_scores
the highest_possible_score in the game
and returns a sorted list of scores in less than O(n log n) time.
"""


unsorted_scores = [3, 6]

# # Approach 1
# def sort_scores(unsorted_scores, highest_possible_score):

#     counts = {}

#     scores = ""

#     for num in unsorted_scores:
#         counts[num] = counts.get(num, 0) + 1

#     for num in range(highest_possible_score, 0, -1):
#         if num in counts:
#             while counts[num] != 0:
#                 scores += str(num) + " "
#                 counts[num] -= 1

#     return [scores]


def sort_scores(unsorted_scores, highest_possible_score):

    counts = {}

    index = 0

    sorted_scores = [0] * len(unsorted_scores)

    for num in unsorted_scores:
        counts[num] = counts.get(num, 0) + 1

    for num in range(highest_possible_score, 0, -1):

        if index == len(unsorted_scores):
            break
        else:
            if num in unsorted_scores:

                while counts[num] > 0:
                 
                    sorted_scores[index] = num
                    index += 1
                    counts[num] -= 1

    return sorted_scores


# print(sort_scores(unsorted_scores, 6))


# Approach 2


# def sort_scores(unsorted_scores, highest_possible_score):

#     counts = highest_possible_score * [0]

#     for num in range(0, highest_possible_score):
#         if num in unsorted_scores:
#             repeats = unsorted_scores.count(num)

#             if repeats > 0:
#                 counts[num] += repeats
#                 repeats -= 1

#     index = -1
#     for i, num in enumerate(counts):
#         if num:
#             while num > 0:
#                 unsorted_scores[index] = i
#                 num -= 1
#                 index -= 1
#     return unsorted_scores
