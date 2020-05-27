"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""


def climb_stairs(num):

    if num <= 2:
        return num

    count_stairs = [0] * num

    count_stairs[0] = 1
    count_stairs[1] = 2

    for i in range(2, num):
        count_stairs[i] = count_stairs[i - 2] + count_stairs[i - 1]

    return count_stairs[-1]
