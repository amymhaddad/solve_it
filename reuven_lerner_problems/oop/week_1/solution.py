# structure dictionary top to bottom
from collections import OrderedDict


def collect_places():
    """
    Expect: nothing
    Modify: nothing
    Return: a dictionary that includes user input for countries and cities the user has visited
    """

    locations = {}

    while True:
        user_locations = input("Tell me where you went: ")

        if not user_locations:
            break

        try:
            city, country = user_locations.split(",")[0], user_locations.split(",")[1]

        except IndexError:
            print("That's not a legal city, country combination")

        else:
            if country in locations:
                if city in locations[country]:
                    locations[country][city] += 1
                else:
                    locations[country][city] = 1
            else:
                locations[country] = {city: 1}

    return locations


destinations = collect_places()


def order_destinations(destinations):
    """
    Expect: nested dictionary 
    Modify: sort the dictionary by country, then by city
    Return: a sorted dictionary
    """

    country_city = {}
    countries = OrderedDict(sorted(destinations.items()))

    for country, cities in countries.items():
        country_city[country] = OrderedDict(sorted(cities.items(), key=lambda x: x[0]))
    return country_city


sorted_destinations = order_destinations(destinations)


def report(sorted_destinations):
    """
    Expect: a nested, sorted dictionary organized by countries, then cities
    Modify: nothing
    Return: a string that reports the country name and each city
    If the city has been visited more than once, then return the number of times the city has been visited.
    """

    report = ""
    for country, cities in sorted_destinations.items():
        report += country + "\n"
        for city, count in cities.items():
            if count > 1:
                report += f"\t{city}({count})\n"
            else:
                report += f"\t{city}\n"

    return report


print(report(sorted_destinations))
