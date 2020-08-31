"""
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.

"""


def get_smallest(nums):
    num_counter = {num: [] for num in nums}

    for curr_num, count in num_counter.items():
        for num in nums:
            if num < curr_num:
                count.append(num)

    return [len(num_counter[num]) for num in nums if num in num_counter]
