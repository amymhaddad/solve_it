
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
