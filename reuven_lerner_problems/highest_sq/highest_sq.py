"""
Find the highest square lower than a given number. 
Return the highest square and the number that produces the square.
"""


def highest_sq_lower_than_given_num(number):

    highest_sq = 0
    for num in range(number):
        square = num ** 2

        if square > number:
            break
        highest_sq = square
    return highest_sq, num


print(highest_sq_lower_than_given_num(500))
