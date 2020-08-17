"""
Modify the Bowl class, such that adding a new scoop to the bowl
will only work if you have fewer than 3 scoops.  In other words: max 3
scoops per bowl.

Adding a new scoop to a bowl that is already full will be silently
ignored.
"""

# Option 1 - Use a for loop to add scoops to the bowl
class Scoops(object):
    def __init__(self, flavor):
        self.flavor = flavor


class Bowl(object):
    def __init__(self):
        self.bowl = []

    def add_scoop(self, *scoops):
        for scoop in scoops:
            if len(self.bowl) >= 3:
                break
            else:
                self.bowl.append(scoop)


# Option 2 - Use class attribute
class Scoops(object):
    def __init__(self, flavor):
        self.flavor = flavor


class Bowl(object):

    max_scoops = 3

    def __init__(self):
        self.bowl = []

    def add_scoop(self, *scoops):
        for scoop in scoops:
            if len(self.bowl) >= Bowl.max_scoops:
                self.bowl.append(scoop)
                Bowl.max_scoops -= 1


# Option 3 - Use slice and class attribute
class Scoops(object):
    def __init__(self, flavor):
        self.flavor = flavor


class Bowl(object):

    max_scoops = 3

    def __init__(self):
        self.scoops = []

    def add_scoop(self, *scoops):
        self.scoops[: Bowl.max_scoops - len(self.scoops)]


s1 = Scoops("chocolate")
s2 = Scoops("mint")
s3 = Scoops("strawberry")
s4 = Scoops("kiwi")

b1 = Bowl()
b1.add_scoop(s1, s2)
b1.add_scoop(s3)
b1.add_scoop(s4)
print(b1.scoops)
print(b1.max_scoops)
