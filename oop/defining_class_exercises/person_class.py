"""
Person class -- name, e-mail address, and phone number

Create several people, and iterate over them in a list
and print their names (similar to a phone book)

Change the e-mail address of one person, and show
that it has changed by printing your list a second time
"""


class Person:
    def __init__(self, name, email, phone_number):
        self.name = name
        self.email = email
        self.phone_number = phone_number


p1 = Person("bob", "bob@example.com", "123-45-6789")
p2 = Person("henry", "henry@example.com", "333-44-8989")
p3 = Person("jerry", "jerry@example.com", "121-55-6789")

all_people = [p1, p2, p3]

for person in all_people:
    print(f"{person.name}")

p2.email = "henry_james@example.com"
for person in all_people:
    print(f"{person.name}: {person.email}")
