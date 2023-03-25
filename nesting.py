capitals = {
    "France": "Paris",
    "Germany": "Berlin",
    "Netherlands": "Amsterdam",
    "Andorra": "Andorra la Vella",
    "Greece": "Athens",
    "Serbia": "Belgrade",
    "Switzerland": "Bern",
    "Slovakia": "Bratislava",
    "Belgium": "Brussels",
    "Romania": "Bucharest",
    "Hungary": "Budapest",
}

travel_log = [
    {
        "country":"France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country":"Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 7
    },
]

def add_new_country(country, total_visits, cities_visited):
    new_country = {}
    new_country["country"] = country
    new_country["cities_visited"] = cities_visited
    new_country["total_visits"] = total_visits
    travel_log.append(new_country)


add_new_country(country="Russia", total_visits=2, cities_visited=["Moscow", "Saint Petersburg"])

print(travel_log)

for item in travel_log:
    for key, value in item.items():
        print(key, value)