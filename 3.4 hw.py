countries = []
while True:
    country = input("Enter a country's name (type 'Done' to finish): ")
    if country.lower() == 'done':
        break
    countries.append(country.capitalize())

countries.sort()

while countries:
    country = countries.pop(0)
    print(country)

cities = ["Portland", "San Francisco", "Houston", "Boston"]
states = ["Oregon", "California", "Texas", "Massachusetts"]
city_state = []
for i in range(len(cities)):
    city_state.append(cities[i] + ", " + states[i])

print(city_state)


days = ["monday", "wednesday", "thursday"]
days.insert(1, "tuesday")
days.append("friday")
days.extend(["saturday", "sunday"])

print(days)
