from collections import Counter

all_people = [
    {"name": "Reuven", "age": 48, "hobbies": ["Python", "cooking", "reading"]},
    {"name": "Atara", "age": 17, "hobbies": ["horses", "cooking", "art", "reading"]},
    {"name": "Shikma", "age": 15, "hobbies": ["Python", "piano", "cooking", "reading"]},
    {"name": "Amotz", "age": 13, "hobbies": ["biking", "cooking"]},
]


max_age = max([person["age"] for person in all_people])

# Function 1 - Return the average age of all people, or (optionally) all people under a given age.
def get_average_age(all_people, max_age=100):
    young_ages = [person["age"] for person in all_people if person["age"] < max_age]

    if young_ages:
        return sum(young_ages) // len(young_ages)
    else:
        return 0


# Function 2 - Return a set of the different hobbies enjoyed by people in our database.
def get_unique_hobbies(all_people):

    return {hobby for person in all_people for hobby in person["hobbies"]}


# Function 3 - Return a Counter object indicating how many people have each hobby -- that is, how many people are interested in Python, how many enjoy cooking, and so forth.
def get_hobby_count(all_people):

    return Counter(hobby for person in all_people for hobby in person["hobbies"])


# Function 4 - Return the n most common hobbies, as a list of strings.
def get_most_common_hobbies(all_people):
    return ", ".join(
        [hobby for hobby, count in get_hobby_count(all_people).most_common()]
    )
