"""
Let's call an array A a mountain if the following properties hold:

A.length >= 3
There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

Example 1:

Input: [0,1,0]
Output: 1
"""

# Option 1:
def peak_mountain(A):
    return A.index(max(A))


# Option 2:
def peak_mountain(A):
    array_length = len(A)
    array_mid_point = array_length // 2

    peak = A[0]

    for i, number in enumerate(A):
        if A[i] > peak:
            peak = number
        else:
            continue
    return A.index(peak)
