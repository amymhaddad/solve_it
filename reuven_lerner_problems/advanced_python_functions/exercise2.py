"""
Write a function, combine_dicts, that takes any number of dicts as
arguments.  The output from the function is a new dict that merges
all of the keys and values together.  The values will always be in
a list, even if there is only one value.

The function takes a single keyword argument, maxvalues, an
integer indicating the maximum number of values that should be
associated with a key.  (Just take the first maxvalues
elements in a list.)

"""
# option 1
from collections import defaultdict


def combine_dicts(*dicts, maxvalue=0):
    combined = defaultdict(list)
    for dict in dicts:
        for k, v in dict.items():
            if not maxvalue or len(combined[k]) < maxvalue:
                combined[k].append(v)
            else:
                continue

    return combined


# Option 2
def combine_dicts2(*args, maxvalue=0):
    output = {}
    for dict in args:
        for k, v in dict.items():
            if k in output and len(output[k]) < maxvalue:
                output[k].append(v)
            else:
                output[k] = [v]
    return output


d1 = {"a": 1, "b": 2, "c": 3, "d": 4}
d2 = {"c": 10, "d": 20, "e": 30}
d3 = {"d": 200, "e": 300, "f": 400}

print(combine_dicts2(d1, d2, d3, maxvalue=2))
