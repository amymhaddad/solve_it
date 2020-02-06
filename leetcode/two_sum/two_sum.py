"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""

# option 1
def indices_approach_1(numbers, target):

    total_indices = []
    for i, num in enumerate(numbers):
        next_num = numbers[(i + 1) % len(numbers)]

        if num + next_num == target:
            total_indices.append(numbers.index(num))
            total_indices.append(numbers.index(next_num))

    return total_indices


# option 2
def indices_approach_2(numbers, target):
    total_indices = {}

    for i, number in enumerate(numbers):
        try:
            return [total_indices[target - number], i]

        except KeyError:
            total_indices[number] = i
    return None


# option 3
# Time complexity: O(n^2)
# Space complecity: O(1)
def indices_approach_3(numbers, target):
    total_indices = []
    for number in numbers:
        for num in range(1, number + 1):
            if num + number == target:
                total_indices.append(numbers.index(num))
                total_indices.append(numbers.index(number))
    return total_indices


# Option 4:
# Time complexity: O(n)
# Space complexity: O(n) // the space required depends on the number of items stored in the has table, which stored n elements
def indices_approach_4(numbers, target):

    total_indices = {}

    for i, num in enumerate(numbers):
        total_indices[num] = i

    for i, num in enumerate(numbers):
        complement = target - num
        if complement in total_indices:
            return [i, total_indices[complement]]


# Option 4:
# Time Complexity: O(n)
# Space Complexity: O(n)
def indices_approach_5(numbers, target):
    total_indices = {}

    for i, num in enumerate(numbers):
        total_indices[num] = i

        complement = target - num
        if complement in total_indices:
            return [total_indices[complement], i]
