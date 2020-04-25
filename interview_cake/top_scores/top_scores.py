

# unsorted_scores = [50, 20, 60, 20]


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

# nums = [4, 8, 4, 2]

# counts = []

# for i, num in enumerate(nums):
#     repeats = nums.count(num)
#     if num in counts:
#         continue
#     counts.insert(num-1, repeats)

# print(counts)








