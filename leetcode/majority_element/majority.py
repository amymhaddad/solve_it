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


print(majority_element(nums))


def majority_element_approach_2(nums):
    sorted_nums = sorted(nums)

    count = 1
    num = 0
    i = 1

    number_counter = {}

    while i < len(sorted_nums):
        if sorted_nums[i] == sorted_nums[num]:
            count += 1
            i += 1
        else:
            number_counter[sorted_nums[num]] = count
            count = 1
            num = i
            i += 1
        number_counter[sorted_nums[num]] = count
    return sorted(number_counter, reverse=True)[0]


print(majority_element_approach_2(nums))
