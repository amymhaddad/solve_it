nums = [6, 5, 4, 8]


from collections import deque, Counter

num_deque = deque(nums)


# i = 0


# while i <= len(nums) - 1:
#     num_deque.rotate(-i)
#     print(num_deque)

#     i += 1


# rotated_list = []
# for i, num in enumerate(nums):
#     rotated_index = (i + 1) % len(nums)
#     rotated_list.append(nums[rotated_index])
# print(rotated_list)

# num = 0
# while num <= len(nums):
#     print(num)
#     each_list = []
#     for i, num in enumerate(nums):
#         rotated_index = (i + 1) % len(nums)
#         each_list.append(nums[rotated_index])
#     num += 1
#     rotated_list.append(each_list)

# print(rotated_list)
i = 0

while i < len(nums):
    each_iteration = Counter()
    for num in num_deque:
        each_iteration[num]
    x = num_deque.popleft()
    num_deque.append(x)

    i += 1
    print(each_iteration)

