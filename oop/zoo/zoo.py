class Species:
    def __init__(self):
        self.name = self.__class__.__name__.lower()

    def __repr__(self):
        return f"{self.color} {self.name} {self.legs}"


class Wolf(Species):
    def __init__(self, color):
        super().__init__()
        self.color = color
        self.legs = 4


class Sheep(Species):
    def __init__(self, color):
        super().__init__()
        self.color = color
        self.legs = 4


class Snake(Species):
    def __init__(self, color):
        super().__init__()
        self.color = color
        self.legs = 0


class Parrot(Species):
    def __init__(self, color):
        super().__init__()
        self.color = color
        self.legs = 2


class Cage(object):
    def __init__(self, id):
        self.cage = []
        self.id = id

    def add_animals(self, *animals):
        for animal in animals:
            self.cage.append(animal)

    # Option 1 - Goes along with animals_by_color() in class Zoo()
    def animals_by_color(self, color):
        return "\n".join([str(animal) for animal in self.cage if animal.color == color])

    def __repr__(self):

        output = f"Cage {self.id}\n"
        output += "\n".join(
            [f"\t{i} {animal}" for i, animal in enumerate(self.cage, 1)]
        )
        return output


class Zoo(object):
    def __init__(self):
        self.all_cages = []

    def add_cages(self, *cages):
        for cage in cages:
            self.all_cages.append(cage)

    # Option 1 - Goes along with animals_by_color() in class Cage()
    # Note: instead of self, I use the curent iteration of my iteratble, one_cage
    def animals_by_color(self, color):
        return "\n".join([animal.animals_by_color(color) for animal in self.all_cages])

    # Option 2 - animals_by_color() -- this option would replace option 1 above
    def animals_by_color(self, color):
        return "\n".join(
            [
                f"{one_animal}"
                for one_cage in self.all_cages
                for one_animal in one_cage.cage
                if one_animal.color == color
            ]
        )

    def number_of_legs(self):
        return sum(
            [int(animal.legs) for cage in self.all_cages for animal in cage.cage]
        )

    def __repr__(self):
        return "\n".join(f"{cages}" for cages in self.all_cages)


wolf = Wolf("black")  # species, color, # legs
sheep1 = Sheep("white")
sheep2 = Sheep("white")
snake = Snake("brown")
parrot = Parrot("black")

c1 = Cage(1)  # ID numbers
c1.add_animals(wolf, sheep1, sheep2)

c2 = Cage(2)
c2.add_animals(snake, parrot)

z = Zoo()
z.add_cages(c1, c2)
