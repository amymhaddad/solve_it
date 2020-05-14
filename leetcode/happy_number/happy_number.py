
import math

# total = []

# last_num_sqd = int(math.pow((19 % 10), 2))
# remaining_nums = 19 // 10


def is_happy(num):
    total = []
   
    while len(total) <= len(list(str(num))):
        # import pdb; pdb.set_trace()
        
        last_num_sqd = int(math.pow((num % 10), 2))
        total.append(last_num_sqd)
        remaining_nums = num // 10
        num = remaining_nums

    

    if sum(total) < 10:
        return sum(total) == 1

print(is_happy(19))