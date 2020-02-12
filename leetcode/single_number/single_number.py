
nums = [4,1,2,1,2]

def find_single_number(nums):
    unique_nums = {}

    sorted_nums = sorted(nums)
    i = 0

    for num in sorted_nums:
        unique_nums[num] = i
        i += 1    
    return unique_nums
        


print(find_single_number(nums))