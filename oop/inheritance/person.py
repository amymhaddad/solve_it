"""
Create a Person class, and add a subclass, called
VerbosePerson.  This class works the same way as Person, except that
the "greet" method doesn't just return "Hello, NAME" but rather
something longer than that.
"""


class Person(object):
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}"


class VerbosePerson(Person):
    def greet(self):
        return f"Hello, {self.name} and welcome"


p1 = Person("Amy")
print(p1.greet())

p2 = VerbosePerson("Hanna")
print(p2.greet())
