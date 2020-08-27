class Scoops(object):
    def __init__(self, flavor):
        self.flavor = flavor

    def __repr__(self):
        return f"Scoop of {self.flavor}"


class Bowl(object):
    max_scoops = 3

    def __init__(self):
        self.bowl = []

    def add_scoops(self, *scoops):
        self.bowl += scoops[: self.max_scoops - len(self.bowl)]

    def flavors(self):
        return ", ".join([scoop.flavor for scoop in self.bowl])

    def __len__(self):
        return len(self.bowl)

    def __repr__(self):
        output = "Bowl with: \n"
        output += "\n".join(
            [f"\t {i} {one_scoop}" for i, one_scoop in enumerate(self.bowl, 1)]
        )
        return output


class BigBowl(Bowl):
    max_scoops = 5


s1 = Scoops("chocolate")
s2 = Scoops("mint")
s3 = Scoops("strawberry")
s4 = Scoops("banana")
