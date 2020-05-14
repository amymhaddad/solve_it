
import math

# total = []

# last_num_sqd = int(math.pow((19 % 10), 2))
# remaining_nums = 19 // 10


def is_happy(num):

    count = sum(1 for i in range(len(str(num))))

    total = []

    # while len(total) <= len(list(str(num))):
    while True:
       
        last_num_sqd = int(math.pow((num % 10), 2))
        total.append(last_num_sqd)
        remaining_nums = num // 10
           
        num = remaining_nums
        
        if len(total) == count:
            # import pdb; pdb.set_trace()
            iteration_total = sum(total)

            if iteration_total > 9:
                total = []
                num = iteration_total
                count = sum(1 for i in range(len(str(num))))
                continue
            else:
                return sum(total) == 1

print(is_happy(19))
 
    







nums_sqd = {
    1: 1**1, 
    2: 2**2, 
    3: 3**3, 
    4: 4**4,
    5: 5**5,
    6: 6**6,
    7: 7**7,
    8: 8**8, 
    9: 9**9, 
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
