"""
Your company built an in-house calendar tool called HiCal. You want to add a feature to see the times in a day when everyone is available.
To do this, you’ll need to know when any team is having a meeting. 
In HiCal, a meeting is stored as a tuple ↴ of integers (start_time, end_time). These integers represent the number of 30-minute blocks past 9:00am.

Write a function merge_ranges() that takes a list of multiple meeting time ranges and returns a list of condensed ranges.
"""


def organize_meeting_times(meeting_times):
    return sorted(meeting_times, key=lambda x: x[0])


sorted_meeting_times = organize_meeting_times(meeting_times)


def merge_ranges(sorted_meeting_times):

    times = []
    for numbers in sorted_meeting_times:
        for num in numbers:
            times.append(num)

    i = 1
    time = 0

    all_times = []
    while i <= len(times):

        if i == len(times) - 1:
            all_times.append(times[time])
            break

        if times[time] < times[i] and times[time] > times[i - 1]:
            all_times.append(times[i])
            time = i + 1
            i += 2

        elif times[time] < times[i]:
            all_times.append(times[time])
            time += 1
            i += 1
        else:
            i += 1

    return all_times


merged_ranges = merge_ranges(sorted_meeting_times)


def start_end_times_tuples(merged_ranges):

    start_end_times = []

    i = 0

    for num in merged_ranges:

        if i == len(merged_ranges):
            break

        pair = tuple(merged_ranges[i : i + 2])
        start_end_times.append(pair)

        i += 2
    return start_end_times


print(start_end_times_tuples(merged_ranges))
