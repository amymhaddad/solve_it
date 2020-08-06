"""
Create a Scoop class -- each instance is one scoop of ice cream.
Then, create three instances of the class, put each instance into a list, and print the flavors.

"""


class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor


s1 = Scoop("chocolate")
s2 = Scoop("vanilla")
s3 = Scoop("coffee")

all_flavors = [s1, s2, s3]

for ice_cream in all_flavors:
    print(f"{ice_cream.flavor}")
