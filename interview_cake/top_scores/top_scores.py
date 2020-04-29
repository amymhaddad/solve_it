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


index = -1
for i, num in enumerate(counts):
    if num:
        while num > 0:
            nums[index] = i
            num -= 1
            index -= 1

print(nums)
