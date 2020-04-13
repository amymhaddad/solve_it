"""
You're now a baseball game point recorder.

Given a list of strings, each string can be one of the 4 following types:

Integer (one round's score): Directly represents the number of points you get in this round.
"+" (one round's score): Represents that the points you get in this round are the sum of the last two valid round's points.
"D" (one round's score): Represents that the points you get in this round are the doubled data of the last valid round's points.
"C" (an operation, which isn't a round's score): Represents the last valid round's points you get were invalid and should be removed.
Each round's operation is permanent and could have an impact on the round before and the round after.

You need to return the sum of the points you could get in all the rounds.
"""


class Stack:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return not bool(self._items)

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[-1]

    def size(self):
        return len(self._items)


def calPoints(scores):

    total_scores = Stack()

    for score in scores:
        try:
            if isinstance(int(score), int):
                total_scores.push(int(score))

        except ValueError:
            if score == "C":
                total_scores.pop()

            elif score == "D":

                recent_valid_score = total_scores.peek()
                total_scores.push(recent_valid_score + recent_valid_score)

            elif score == "+":
                second_to_last_valid_score = total_scores._items[-2]
                last_two_valid_scores = total_scores.peek() + (
                    second_to_last_valid_score
                )
                total_scores.push(last_two_valid_scores)
    return sum(total_scores._items)
