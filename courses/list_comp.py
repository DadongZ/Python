"""
List comprehensions:
    [expr for val in collection]
    [expr for val in collection if <test>]
    [expr for val in collection if <test1> and <test2>]
"""

squares = [i**2 for i in range(1, 101)]
print(squares)

remainders5 =[i**2 % 5 for i in range(1, 21)]
print(remainders5)

movies =["Star wars", "Gandi", "Casablanca", "Shawshank Redemption",
        "Toy Story", "Gone with the Wind", "Citizen Kane", "It's a wonderful life",
        "The wizard of oz", "Gattaca", "Rear Window", "Ghostbusters", "To kill a mockingbird"]

gmovies = [title for title in movies if title.startswith("G")]
print(gmovies)

movies =[("Star wars", 1977), ("Citizen Kane", 1941), ("Spirited Away", 2001),
         ("It's a wonderful life", 1946), ("Gattaca", 1997)]

#pre2k = [m for m in movies if m[1]<2000]
pre2k = [title for (title, year) in movies if year < 2000]
print(pre2k)

V = [2, -3, 1]
V1 = 4*V
print(V1)

V2 = [i**2 for i in V]

print(V2)


#Cartesian product
A = [1, 3, 5, 7]
B = [2, 4, 6, 8]

AB = [ (a*b) for a in A for b in B]
print(AB)
