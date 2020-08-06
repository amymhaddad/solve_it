# Challenge: turn a list of dictionaries into a class. Create 3 instances of the class and loop through them.

computers = [
    {"brand": "Apple", "year": 2016},
    {"brand": "HP", "year": 2015},
    {"brand": "Lenovo", "year": 2010},
]

for one_computer in computers:
    print(f"{one_computer['brand']}, from {one_computer['year']}")


class Computers:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year


c1 = Computers("Apple", 2015)
c2 = Computers("Lenovo", 2019)
c3 = Computers("HP", 2017)

all_computers = [c1, c2, c3]

for one_computer in all_computers:
    print(f"{one_computer.brand}, from {one_computer.year}")
