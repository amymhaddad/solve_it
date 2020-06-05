paths = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]

from collections import defaultdict


def dest_city(paths):
    city_placement = defaultdict(list)
    unique_cities = set()
    for cities in paths:
        for i, city in enumerate(cities):
            city_placement[i].append(city)
            unique_cities.add(city)

    destination_city = city_placement[1]
    starting_city = city_placement[0]

    for city in destination_city:
        if city not in starting_city:
            return city
