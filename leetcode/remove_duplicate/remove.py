def remove_duplicate(nums):

    unique = 0

    for i in range(len(nums)):
        if nums[i] != nums[unique]:
            unique += 1
            nums[unique] = nums[i]
    return unique + 1
