

unsorted_scores = [50, 20, 60]


def sort_scores(unsorted_scores, highest_possible_score):
    top = 1
    bottom = 0

    if len(unsorted_scores) <= 1:
        return unsorted_scores 

    while top <= len(unsorted_scores):
        if bottom == top:
            break
            
        import pdb; pdb.set_trace()
        if unsorted_scores[bottom] > unsorted_scores[top]:
            top += 1
            
        elif unsorted_scores[bottom] < unsorted_scores[top]:
            unsorted_scores[bottom], unsorted_scores[top] = unsorted_scores[top], unsorted_scores[bottom]
            bottom += 1
            top += 1
    return unsorted_scores


# print(sort_scores([37, 89, 41, 65, 91, 53], 100))

nums = [4, 8, 4 ,2, 9, 9, 6, 2, 9]


count_scores = []
for num in nums:
    print(nums.count(num))

