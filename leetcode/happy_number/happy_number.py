
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


def is_happy(n):
    count = sum(1 for i in range(len(str(n))))
    all_nums = list(map(int, str(n)))
    i = 0
    total = 0

    # use n to update on each iteration (set it to 100 to prevent hitting an endless loop)
    while i < 100:

        # cycle through each number in all_nums and index into dictionary to get each sq; add the value of each number to total

        # have a checker to see if total is < 10.  Is the number 1? If 1, then return True. If not then, False
        # IF total is > 10, then get the sq of each number in the next pair of numbres (ie, get 82)
            # set total to 0; set n to total; call all_nums (to get teh NEW list of nums)
        i += 1


print(is_happy(1111111))
 

# last_num_sqd = int(math.pow((n % 10), 2))
#         total.append(last_num_sqd)
#         remaining_nums = n // 10

#         n = remaining_nums

#         if len(total) == count:
#             iteration_total = sum(total)
#             if iteration_total >= 10:
#                 total = []
#                 n = iteration_total
#                 count = sum(1 for i in range(len(str(n))))

#             if iteration_total < 10:
#                 return iteration_total == 1
