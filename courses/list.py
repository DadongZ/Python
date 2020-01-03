
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ['Janey', 'Oscar', 'Alex', 'Ryan', 'Brad', 'Cindy']

print(friends[0:3])

print(friends)
for i, friend in enumerate(friends):
    print(i, friend)

for x, y in zip(lucky_numbers, friends):
    print(x, y)

friends.extend(lucky_numbers)
friends.insert(1, 'John')
friends.remove("Janey")

print(friends)
lucky_numbers.sort()
print(lucky_numbers)

lucky_numbers.reverse()
print(lucky_numbers)
