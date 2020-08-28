nums = [6, 5, 4, 8]

k = 1
for i, num in enumerate(nums):
    y = nums[(i + k) % len(nums)]
    print(y)


from collections import deque

num_deque = deque([1, 2, 3, 4, 5])
num_deque.rotate(1)
print(num_deque)


def rotate(nums, k):
    nums_length = len(nums)

    rotated_array = [None] * nums_length

    for i, num in enumerate(nums):
        rotated_index = (i + k) % nums_length

        rotated_array[rotated_index] = num

    for i in range(nums_length):
        nums[i] = rotated_array[i]
   return nums

