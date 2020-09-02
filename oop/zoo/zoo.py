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


wolf = Wolf("black")
print(wolf)
