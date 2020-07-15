"""
Implement "myrange", our own home-grown version of the built-in "range" function.

That is, I'd like you to implement:
* A function ("myrange2") that takes one, two, or three parameters and returns a list that looks like my above examples for Python 2's "range" functio.
* A generator function ("myrange3") that takes one, two, or three parameters and returns an iterator (well, a generator) that looks like my above examples for Python 3's "range" function.  Note that the printed representation doesn't have to look the same.

In both cases, it should be possible to take the output of calling our function and stick it into a "for" loop:
   for x in myrange2(10, 30, 3):
        print(x)

The above should print
   10 13 16 19 22 25 28

"""

# Function implentation
def myrange(stop, start=None, interval=1):

    if start is None:
        start = 0
    else:
        stop, start = start, stop

    total_numbers = []
    while start < stop:
        total_numbers.append(start)
        start += interval

    return total_numbers


# Generator implementation
def myrange_generator(stop, start=None, interval=1):
    if start is None:
        start = 0
    else:
        stop, start = start, stop

    while start < stop:
        yield start
        start += interval
