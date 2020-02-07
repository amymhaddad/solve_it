# Option 1
def has_duplicates_approach_1(numbers):

    for i, num in enumerate(numbers):
        next_num = numbers[(i + 1) % len(numbers)]
        if num == next_num:
            return True
    return False


# Option 2
def has_duplicates_approach_2(numbers):
    return len(set(numbers)) != len(numbers)


# Option 3
def has_duplicates_approach_3(numbers):

    unique_numbers = {}

    for i, num in enumerate(numbers):
        if num in unique_numbers.keys():
            return True
        else:
            unique_numbers[num] = i
    return False


# Option 4
def has_duplicates_approach_4(numbers):
    sorted_nums = sorted(numbers)
    for i, num in enumerate(numbers):
        if num == sorted_nums[(i + 1) % len(numbers)]:
            return True
    return False
