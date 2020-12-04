"""
(1) Write a function ("report_card") that produces a generic report
    card for a student. (The return value will be a string that can be
    printed for all to see.)  The function will take one mandatory
    positional argument, the name of the student.

    The keyword arguments will represent the names of the different
    courses that the student has taken.  Each course will have a
    different name, and the value associated with each keyword
    argument will be the student's grade.

    The returned string should print the name of the student, as well
    as courses they took, individual grades in those courses, and then
    their average grade.

    For example, invoking:

    report_card('Eve', English=95, Math=90, History=75, Science=86)

    will return a string like the following:

    Eve:
        English 95
        Math    90
        History 75
        Science 86
        Average 86.5

    Note that you don't need the formatting to look just like this.
"""


def report_card(name, **kwargs):
    total = 0
    result = ""

    result += f"{name}:\n"
    for k, v in kwargs.items():
        result += f"\t{k:<10} {v}\n"
        total += int(v)

    result += f"\tAverage {total / len(kwargs)}"
    return result


print(report_card("Eve", English=95, Math=90, History=75, Science=86))
