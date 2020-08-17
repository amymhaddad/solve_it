from collections import Counter


def intersect(nums1, nums2):

    if len(nums1) == 0 or len(nums2) == 0:
        return []

    count_nums1 = Counter(nums1)

    result = []
    for num in nums2:
        shared_number = num in count_nums1 and count_nums1[num] > 0
        if shared_number:
            result.append(num)
            count_nums1[num] -= 1
    return result
