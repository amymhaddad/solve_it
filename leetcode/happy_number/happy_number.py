import math


#check process -- should this be recursive?


def is_happy(n):
    count = sum(1 for i in range(len(str(n))))

    total = []
    while True:

        last_num_sqd = int(math.pow((n % 10), 2))
        total.append(last_num_sqd)
        remaining_nums = n // 10

        n = remaining_nums

        if len(total) == count:
            iteration_total = sum(total)
            if iteration_total >= 10:
                total = []
                n = iteration_total
                count = sum(1 for i in range(len(str(n))))
                continue
            if iteration_total < 10:
                return iteration_total == 1


print(is_happy(1111111))

# all_nums = list(map(int, str(n)))
# same_num = all(num == all_nums[0] for num in all_nums)
# if same_num == True and all_nums[0] == 1:
#     return True
 






#Alt with dict
nums_sqd = {
    1: 1 ** 1,
    2: 2 ** 2,
    3: 3 ** 3,
    4: 4 ** 4,
    5: 5 ** 5,
    6: 6 ** 6,
    7: 7 ** 7,
    8: 8 ** 8,
    9: 9 ** 9,
    0: 1,
}


def is_happy_v2(num):
    total = []
    result = num

    if result < 10:
        return nums_sqd[result] == 1

    else:
        last_num = num % 10
        remaining_nums = num // 10
        total.append(nums_sqd[last_num])
        num = remaining_nums

        return is_happy(remaining_nums) + nums_sqd[last_num]
