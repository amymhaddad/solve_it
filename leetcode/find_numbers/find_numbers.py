def findnumbers(nums):

    total_evens = 0
    for num in nums:
        digit_length = len(str(num))
        if int(digit_length) % 2 == 0:
            total_evens += 1
    return total_evens
