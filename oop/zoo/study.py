
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

    # This method is invoked from the Zoo class. When it's caleed, I iterate through self.cage
    # For each animal in the cage, I get check the color (which was passed in from Zoo)
    # I return the animals that match the arg that's passed in
    #This works bc each Cage has an animal class, which inherits from the Species() class to get the attributes 
    def animals_by_color(self, color):
        return "\n".join([str(animal) for animal in self.cage if animal.color == color])

    def __repr__(self):
        output = f"Cage {self.id}:\n"
        output += "\n".join(
            [f"\t{i} {animal}" for i, animal in enumerate(self.cage, 1)]
        )
        return output


c1 = Cage(1)  # ID numbers
c1.add_animals(wolf, sheep1, sheep2)


c2 = Cage(2)
c2.add_animals(snake, parrot)


class Zoo(object):
    def __init__(self):
        self.total_cages = []

    def add_cages(self, *cages):
        for cage in cages:
            self.total_cages.append(cage)

    # Option 1: Get animals by color:
    # Iterate through self.total_cages in this class.
    # THEN on each iteration call the class of the same name in the Cage() class and pass in the color to that class
    def animals_by_color(self, color):
        return "\n".join(
            [
                # Note: instead of self, I use the curent iteration of my iteratble, one_cage
                one_cage.animals_by_color(color)
                for one_cage in self.total_cages
            ]
        )

    # Alt to to the above method
    # First, I iterate through self.total_cages from this class.
    # Second, I iterate through each cage in the Cage class and access its atribute, cage
    # for one_animal in one_cage.cage --> cage is the attribute in the Cage() class
    # Then I add my conditional
    # This method prevents me from having to make the extra method in the Cage class
    def animals_by_color2(self, color):
        return "\n".join(
            [
                str(one_animal)
                for one_cage in self.total_cages
                for one_animal in one_cage.cage
                if one_animal.color == color
            ]
        )

    def number_of_legs(self):
        return sum([animal.legs for cages in self.total_cages for animal in cages.cage])

    def __repr__(self):
        output = ""
        output += "".join(f"{cage}\n" for cage in self.total_cages)
        return output


z = Zoo()
z.add_cages(c1, c2)

print(z.animals_by_color2("black"))
print(z.number_of_legs())
