# Key point: just create what you need
# Put all the stuff that's common to all classes into this parent class
class Species:
    def __init__(self, color):
        self.color = color
        # Get the name of the species without invoking another var via self.className.nameofclass
        self.name = self.__class__.__name__

    def __repr__(self):
        return f"{self.color} {self.species} {self.legs}"


# Use inheritance, since a wolf IS A species, and pass in what's different
class Wolf(Species):
    def __init__(self, color):
        super().__init__(color)
        self.species = "wolf"
        self.legs = 4


class Sheep(Species):
    def __init__(self, color):
        super().__init__(color)
        self.species = "sheep"
        self.legs = 4


class Snake(Species):
    def __init__(self, color):
        super().__init__(color)
        self.species = "snake"
        self.legs = 0


class Parrot(Species):
    def __init__(self, color):
        super().__init__(color)
        self.species = "parrot"
        self.legs = 2


class Cage(object):
    total_animals = 0

    def __init__(self, id):
        self.id = id
        self.cage = []

    def add_animals(self, *animals):
        for animal in animals:
            self.cage.append(animal)
        return self.cage

    def __repr__(self):

        output = f"Cage {self.id}\n"
        output += "\n".join(
            ["\t" + f"{i} {animal}" for i, animal in enumerate(self.cage, 1)]
        )
        return output
        # output = ""
        # for animal in self.cage:
        #     Cage.total_animals += 1
        #     animal_details = f"{Cage.total_animals} {str(animal)} legs"
        #     output += animal_details + "\n"
        # return output


class Zoo:
    def __init__(self):
        self.new_cage = []

    def add_cages(self, *cages):
        for cage in cages:
            self.new_cage.append(cage)

    # def get_animals_by_color(self, color):
    #     for animal in self.new_cage:
    #         print("HERE", animal)

    def __repr__(self):
        return "\n".join([str(cage) for cage in self.new_cage])


wolf = Wolf("black")  # species, color, # legs

sheep1 = Sheep("white")
sheep2 = Sheep("white")
snake = Snake("brown")
parrot = Parrot("black")

# print(wolf)  #  black wolf, 4 legs
# print(sheep1)  #  white sheep, 4 legs
# print(sheep2)  #  white sheep, 4 legs

c1 = Cage(1)  # ID numbers
c1.add_animals(wolf, sheep1, sheep2)

# print(c1)

c2 = Cage(2)
c2.add_animals(snake, parrot)

# print(c2)
z = Zoo()
z.add_cages(c1, c2)

print(z.get_animals_by_color("black"))
