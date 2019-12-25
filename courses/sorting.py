earth_metals= ["Beryllium", "Magnesium", "Calcium", "Strontium", "Barium", "Radium"]
print(help(list.sort))
earth_metals.sort(reverse=True)
print(earth_metals)
#earth_metals= ("Beryllium", "Magnesium", "Calcium", "Strontium", "Barium", "Radium")
#earth_metals.sort() error due to tuple is immutable.


planets = [
    ("Mercury", 2440, 5.43, 0.395),
    ("Venus", 6052, 5.24, 0.723),
    ("Earth", 6378, 5.52, 1.000),
    ("Mars", 3396, 3.93, 1.530),
    ("Jupiter", 71492, 1.33, 5.210),
    ("Saturn", 60268, 0.69, 9.551),
    ("Uranus", 25559, 1.27, 19.213),
    ("Nepture", 24764, 1.64, 30.070)
    ]

size = lambda planet: planet[1]

planets.sort(key=size, reverse=True)
print(planets)

den = lambda x: x[2]

planets.sort(key=den, reverse=False)
print(planets)


print(sorted)

sorted_earth_metals = sorted(earth_metals)
print(sorted_earth_metals)
print(earth_metals)

print(sorted((3,9,5,3,3,5,6,7,5,4,7,4)))

