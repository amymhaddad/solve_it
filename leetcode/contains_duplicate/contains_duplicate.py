# Option 1
def has_duplicates_approach_1(nums):
    all_nums = {}
    for num in nums:
        all_nums[num] = all_nums.get(num, 0) + 1

    for k, v in all_nums.items():
        if v > 1:
            return True
    return False


# Option 2
def has_duplicates_approach_2(numbers):
    return len(set(numbers)) != len(numbers)
