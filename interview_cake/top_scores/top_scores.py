

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

#See if the score is in the range of numbers. IF it is, then iterate through the nubmer of times it's included

# nums = [4, 8, 4, 2]

# counts = []

# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#Create an array with values set to 0
#My index is the key in an array -- it is still a hash
# >>> counts = 100*[0]

#At postion 50 increment the value 1 
# >>> counts[50] += 1

# >>> counts[20] += 1
# >>> counts[60] += 1
# >>> counts
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# >>> counts[60] += 1
# >>> counts







