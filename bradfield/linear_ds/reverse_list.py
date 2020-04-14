"""
Write a function that uses a stack to return a reversed copy of a list.
"""
from stack import Stack

nums = [1, 2, 3]

# Option 1
def reverse_list_approach_1(nums):

    s = Stack()

    i = len(nums) - 1

    while i >= 0:
        s.push(nums[i])
        i -= 1
    return s._items


# Option 2:
def reverse_list_approach_2(nums):

    s_original = Stack()
    s_reversed = Stack()

    for num in nums:
        s_original.push(num)

    if s_reversed.is_empty():

        while not s_original.is_empty():
            last_num = s_original.pop()
            s_reversed.push(last_num)
    return s_reversed._items


print(reverse_list_approach_2(nums))
