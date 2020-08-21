"""
Take our existing Bowl class (for ice cream), and create a
subclass called BigBowl.  A BigBowl is just like a Bowl, except
that it has a maximum of 5 scoops, not 3.
"""


class Scoops(object):
    def __init__(self, flavor):
        self.flavor = flavor


class Bowl(object):
    max_scoops = 3

    def __init__(self):
        self.bowl = []

    def add(self, *scoops):
        self.bowl += scoops[: Bowl.max_scoops - len(self.bowl)]


class BigBowl(Bowl):
    max_scoops = 5

    def add(self, *scoops):

        self.bowl += scoops[: BigBowl.max_scoops - len(self.bowl)]


s1 = Scoops("chocolate")
s2 = Scoops("mint")
s3 = Scoops("strawberry")
s4 = Scoops("banana")


b1 = BigBowl()

b1.add(s1, s2, s3, s4)
print(b1.bowl)
