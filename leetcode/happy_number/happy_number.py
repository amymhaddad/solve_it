"""
Write an algorithm to determine if a number n is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Return True if n is a happy number, and False if not.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""


nums_sqd = {
    1: 1 * 1,
    2: 2 * 2,
    3: 3 * 3,
    4: 4 * 4,
    5: 5 * 5,
    6: 6 * 6,
    7: 7 * 7,
    8: 8 * 8,
    9: 9 * 9,
    0: 0,
}


def is_happy(number):

    all_nums = list(map(int, str(number)))
    i = 0
    total = 0

    while i <= 6:
        for num in all_nums:
            total += nums_sqd[num]

        if total == 1:
            return True
        else:
            number = total
            total = 0
            all_nums = list(map(int, str(number)))
            i += 1
    return False


print(is_happy(19))
