
import math

def area(r):
    """Area of a circle with radius 'r'."""
    return math.pi * (r**2)

raddi = [2, 3, 5.6, 0.3, 11]

##using map
areas = list(map(area, raddi))


##

temps = [("Durham", 10), ("New York", 2), ("Miami", 21), ("Atlanta", 15)]

c_to_f = lambda data: (data[0], 9/5*data[1]+32)


print(list(map(c_to_f, temps)))


##filter


import statistics

data = [1.3, 2.4, 5.6, 0.3, 2.1, 5.7, 11, 0.4]

avg = statistics.mean(data)

print(list(filter(lambda x: x > avg, data)))

countries = ["", "China", "Argentina", "", "", "Chile", "Colombia", "USA"]

print(list(filter(None, countries)))


##reduce

from functools import reduce

data = [2, 3, 5, 7, 11, 4]

out = reduce(lambda x, y: x*y, data)
print(out)



