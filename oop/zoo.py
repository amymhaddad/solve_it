 




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

 
class Cage(object):
    total_animals = 0

    # @staticmethod
    # def increment_id():
    #     id = Cage.id_number
    #     Cage.id_number += 1 
    #     print("cage id", Cage.id_number)
    #     return id 


    def __init__(self, id):
        self.id = id 
        self.cage = []

    def add_animals(self, *animals):
        for animal in animals:
            # Cage.total_animals += 1
            self.cage.append(animal)
        return self.cage

    def __repr__(self):
        output = ''
        for animal in self.cage:
            Cage.total_animals += 1
            animal_details = f"{Cage.total_animals} {str(animal)} legs"
            output += animal_details + "\n"
        return output
        



wolf = Wolf('black' )            # species, color, # legs
sheep1 = Sheep('white')
sheep2 = Sheep('white')         
snake = Snake('brown')
parrot = Parrot('black')

# print(wolf)    #  black wolf, 4 legs
# print(sheep1)    #  white sheep, 4 legs
# print(sheep2)    #  white sheep, 4 legs

c1 = Cage(1)   # ID numbers
c1.add_animals(wolf, sheep1, sheep2)
print(c1)



#HERE:
c2 = Cage(2)
c2.add_animals(snake, parrot)
print(c2)