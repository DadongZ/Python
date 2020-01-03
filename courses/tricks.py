
"""swap values"""

x, y = 10, -10
print('Before: x = %d, y=%d' %(x, y))

x, y = y, x
print('After: x = %d, y=%d' %(x, y))

"""check dictionary"""

ages = {
    'Mary': 31,
    'Alex': 9,
    'Halley': 17
}

age = ages.get('Dadong', 'Unknown')

print('Dadong is %s years old: ' % age)


"""check value in list"""

needle = 'd'
haystack = ['a', 'b', 'c']

#bad way
for letter in haystack:
    if needle == letter:
        print('Found')
        break
else:
    print('Not found!')

"""open text file"""

with open('./data/guido_bio.txt') as f:
    for line in f:
        print(line)
