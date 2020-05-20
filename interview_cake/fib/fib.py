"""
Write a function fib() that takes an integer nn and returns the nnth Fibonacci ↴ number.
"""
# Approach 1:


class Fib:
    def __init__(self):
        self.fib_dict = {}

    def get_fib(self, num):

        if num in [0, 1]:
            return num

        elif num in self.fib_dict:
            return self.fib_dict[num]

        else:
            result = self.get_fib(num - 1) + self.get_fib(num - 2)
            self.fib_dict[num] = result
        return result


# Approach 2:
def fib_approach_2(num):
    if num <= 1:
        return num

    else:
        return fib_approach_2(num - 1) + fib_approach_2(num - 2)
