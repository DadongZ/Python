example = set()

print(help(example.add))

example.add(42)
example.add(False)
example.add(3.1415926)
example.add("Alex")

len(example)
print(example)

example.remove(False)
example.discard(False)

print(example)

example.clear()
print(example)

#intersection

odds =  set([1, 3, 5, 7, 9])
evens = set([2, 4, 6, 8, 10])
primes = set([2, 3, 5, 7])
composites = set([4, 6, 8, 9, 10])

print(odds.union(evens))
print(evens.union(odds))

evens.intersection(primes)

print(2 in primes)
