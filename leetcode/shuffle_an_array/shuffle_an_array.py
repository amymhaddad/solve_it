"""
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn]

"""


def shuffle(nums, num):

    if not nums:
        return []
    if len(nums) == 1:
        return [nums]

    shuffled_array = []

    x, y = 0, num

    while True:
        if y > len(nums) - 1:
            break
        else:
            shuffled_array.extend([nums[x], nums[y]])
            x += 1
            y += 1
    return shuffled_array
