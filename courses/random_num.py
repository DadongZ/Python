
print("WARNING: using os.urandom or SystemRandom for secure random numbers.")

import random

print(dir(random))

print([random.random() for i in range(1, 11)])

#random number between 3 and 7
print([random.random()*4+3 for i in range(1, 11)])

print([random.uniform(3,7) for i in range(1, 11)])

#normal distribution
print([random.normalvariate(0,1) for i in range(1, 11)])

#random integer
print([random.randint(1,6) for i in range(1, 11)])

#random choice
print([random.choice(["Rock", "Scissors", "Paper"]) for i in range(1, 11)])
