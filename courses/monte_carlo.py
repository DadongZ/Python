import random

def random_walk(n):
    """Return coordinates after 'n' block random walk"""
    x = 0
    y = 0

    for i in range(n):
        step = random.choice(['N', 'S', 'E', 'W'])
        if step == 'N':
            y = y + 1
        elif step == 'S':
            y = y -1
        elif step == 'E':
            x = x +1
        else:
            x = x -1
    return (x, y)

for i in range(25):
    walk = random_walk(10)
    print(walk, "Distance from home = ",
         abs(walk[0]) + abs(walk[1]))

def random_walk(n):
    """Return coordinates after 'n' block random walk"""
    x, y = 0, 0
    for i in range(n):
        (dx, dy) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        x += dx
        y += dy
    return (x, y)

for i in range(25):
    walk = random_walk(10)
    print(walk, "Distance from home = ",
         abs(walk[0]) + abs(walk[1]))


B = 10000
for walk_length in range(1, 31):
    no_transport = 0 #number of blocks 4 or less
    for i in range(B):
        (x, y) = random_walk(walk_length)
        distance = abs(x) + abs(y)
        if distance <= 4:
            no_transport += 1
    no_transport_percentage = float(no_transport/B)*100
    print("Walk size = ", walk_length, "/ % of no transport= ", no_transport_percentage)
