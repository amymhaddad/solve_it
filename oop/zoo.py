 




    # def __repr__(self):
    #     return f"{self.color} {self.legs} {self.species}"


# class Species(object):
#     def __init__(self, species, legs):
#         self.species = species
#         self.legs = legs 

class Wolf(object):
    def __init__(self, color):
        self.color = color
        self.species = "wolf"
        self.legs = 4
    
    def __repr__(self):
        return f"{self.color} {self.species} {self.legs}"
       
class Sheep(object):
    def __init__(self, color):
        self.color = color
        self.species = "sheep"
        self.legs = 4
    def __repr__(self):
        return f"{self.color} {self.species} {self.legs}"

class Snake(object):
    def __init__(self, color):
        self.color = color
        self.species = "snake"
        self.legs = 0

    def __repr__(self):
        return f"{self.color} {self.species} {self.legs}"

class Parrot(object):
    def __init__(self, color):
        self.color = color
        self.species = "parrot"
        self.legs = 2
    def __repr__(self):
        return f"{self.color} {self.species} {self.legs}"


wolf = Wolf('black' )            # species, color, # legs
sheep1 = Sheep('white')
sheep2 = Sheep('white')         
# snake = Snake('brown')
# parrot = Parrot('black')

print(wolf)    #  black wolf, 4 legs
print(sheep1)    #  white sheep, 4 legs
print(sheep2)    #  white sheep, 4 legs