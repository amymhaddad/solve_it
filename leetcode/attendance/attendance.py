"""
You are given a string representing an attendance record for a student. The record only contains the following three characters:
'A' : Absent.
'L' : Late.
'P' : Present.
A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

You need to return whether the student could be rewarded according to his attendance record.

Example 1:
Input: "PPALLP"
Output: True

"""


def check_record(record):

    A = 0
    left_ptr = 0

    while left_ptr < len(record):
        if record[left_ptr] == "P":
            left_ptr += 1
            continue

        if record[left_ptr] == "A":
            A += 1
            if A > 1:
                return False
            left_ptr += 1
            continue

        rt_ptr = left_ptr
        while rt_ptr < len(record) and record[rt_ptr] == "L":
            rt_ptr += 1
        total_absences = rt_ptr - left_ptr
        if total_absences > 2:
            return False
        left_ptr = rt_ptr

    return True
