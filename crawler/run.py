import json
from country import allCountry
from city import allCities

cities = {}

for i in range(0, len(allCountry)):
    for j in range(i, i+1):
        cities[allCountry[i]] = allCities[j]

json_cities = json.dumps(cities, ensure_ascii=False).encode('utf8')

print(json_cities.decode())
