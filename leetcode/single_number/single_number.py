
nums = [4,1,2,1,2]

def find_single_number(nums):
    unique_nums = {}

    sorted_nums = sorted(nums)
    i = 0

    n = []
    for num in sorted_nums:
        next_num = sorted_nums[(i+ 1) % len(sorted_nums)]

        if sorted_nums[i] == next_num:
            # import pdb; pdb.set_trace()
            i += 1
            continue

        elif i == len(sorted_nums) -1:
            print(sorted_nums[i])

    
 

print(find_single_number(nums))
