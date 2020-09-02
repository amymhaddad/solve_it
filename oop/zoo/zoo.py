# Key point: just create what you need
# Put all the stuff that's common to all classes into this parent class
# Use inheritance, since a wolf IS A species, and pass in what's different


class Animal(object):
    def __init__(self):
        self.animal = self.__class__.__name__.lower()

    def __repr__(self):
        return f"{self.color} {self.animal} {self.legs}"


class Wolf(Animal):
    def __init__(self, color):
        super().__init__()
        self.color = color
        self.legs = 4


class Sheep(Animal):
    def __init__(self, color):
        super().__init__()
        self.color = color
        self.legs = 4


class Snake(Animal):
    def __init__(self, color):
        super().__init__()
        self.color = color
        self.legs = 0


class Parrot(Animal):
    def __init__(self, color):
        super().__init__()
        self.color = color
        self.legs = 2


wolf = Wolf("black")  # species, color, # legs
sheep1 = Sheep("white")
sheep2 = Sheep("white")
snake = Snake("brown")
parrot = Parrot("black")


class Cage(object):
    def __init__(self, id):
        self.id = id
        self.cage = []

    def add_animals(self, *animals):
        for animal in animals:
            self.cage.append(animal)

    def __repr__(self):
        output = f"Cage {self.id}:\n"
        output += "\n".join(
            [f"\t{i} {animal}" for i, animal in enumerate(self.cage, 1)]
        )
        return output


c1 = Cage(1)  # ID numbers
c1.add_animals(wolf, sheep1, sheep2)
# print(c1)


c2 = Cage(2)
c2.add_animals(snake, parrot)

# print(c2)


class Zoo(object):
    def __init__(self):
        self.total_cages = []

    def add_cages(self, *cages):
        for cage in cages:
            self.total_cages.append(cage)

    def __repr__(self):
        output = ""
        output += "".join(f"{cage}\n" for cage in self.total_cages)

        # for cage in self.total_cages:
        #     output += str(cage)
        return output


z = Zoo()
z.add_cages(c1, c2)
print(z)
