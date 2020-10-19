"""
(1)

    Given this sort of dict (country:city-list):

	{'Israel': ['Jerusalem', 'Tel Aviv'],
	 'USA': ['Boston', 'New York', 'Chicago'],
	 'China': ['Beijing', 'Shanghai']}

    Use a nested list comprehension to produce a list of
    tuples that look like (city, country). Only include countries whose names are longer than 3 characters.

(2) Write a function sums_to_n that takes an argument n,
    and returns all two-element tuples that sum to n.

    sums_to_n(5)

    [(0,5), (1,4), (2,3), (4,1), (5,0)]

(3) Produce a list of the unique octets (from
    the IP addresses) in mini-access-log.

"""

# Exercise 1
locations = {
    "Israel": ["Jerusalem", "Tel Aviv"],
    "USA": ["Boston", "New York", "Chicago"],
    "China": ["Beijing", "Shanghai"],
}

all_locations = [
    (country, city)
    for country, cities in locations.items()
    if len(country) > 3
    for city in cities
]
# Exercise 2

number = 5
total = [(i, num) for i, num in enumerate(range(number, -1, -1))]

total2 = [
    (x, y) for x in range(number + 1) for y in range(number + 1) if x + y == number
]

# Exercise 3

unique = set(
    [
        line
        for lines in open("mini-access-log.txt")
        for line in lines.split()[0].split(".")
    ]
)
