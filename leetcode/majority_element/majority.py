nums = [2, 2, 1, 1, 1, 2, 2]
import operator


def majority_element_approach_1(nums):
    numbers = {}

    for num in nums:
        numbers[num] = numbers.get(num, 0) + 1

    sorted_numbers = sorted(numbers.items(), key=operator.itemgetter(1), reverse=True)[
        0
    ][0]
    return sorted_numbers


def majority_element_approach_2(nums):
    nums.sort()
    return nums[len(nums) // 2]
