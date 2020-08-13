"""
Create a Bowl class.  We can put scoops in the bowl!

b = Bowl()
b.add_scoops(s1, s2)
b.add_scoops(s3)
b.flavors()  # returns a string of "chocolate, vanilla, coffee"

"""


class Scoop(object):
    def __init__(self, flavor):
        self.flavor = flavor


class Bowl(object):
    def __init__(self):
        self.total_scoops = []

    def add_scoops(self, *new_scoops):
        self.total_scoops += new_scoops

    def flavors(self):
        return ", ".join([ice_cream.flavor for ice_cream in self.total_scoops])


s1 = Scoop("chocolate")
s2 = Scoop("vanilla")
s3 = Scoop("coffee")

b = Bowl()

b.add_scoops(s1, s2)
b.add_scoops(s3)
print(b.flavors())

