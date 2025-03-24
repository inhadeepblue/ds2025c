def duplicate_city(cities):
    result_city = list()
    s = set()

    for city in cities:
        l1 = len(s)
        s.add(city)
        l2 = len(s)
        if l1 == l2:
            result_city.append(city)
    return result_city


cities = ['Suwon', 'Hwasung', 'Incheon', 'Incheon', 'Bucheon', 'Incheon', 'Seoul']
cities.append('Seoul')
cities.append('Anyang')
print(cities)
print(set(duplicate_city(cities)))