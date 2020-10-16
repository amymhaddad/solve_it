import requests, json, csv

url = "https://gist.githubusercontent.com/reuven/77edbb0292901f35019f17edb9794358/raw/2bf258763cdddd704f8ffd3ea9a3e81d25e2c6f6/cities.json"


def get_city_data(url, filename):
    response = requests.get(url)

    cities = response.json()

    with open(filename, "w") as csvfile:
        fieldnames = ["city", "state", "population", "rank"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter="\t")

        writer.writeheader()
        for each_city in cities:
            parsed_data = {
                "city": each_city["city"],
                "state": each_city["state"],
                "population": each_city["population"],
                "rank": each_city["rank"],
            }
            writer.writerow(parsed_data)


get_city_data(url, "cities.csv")
