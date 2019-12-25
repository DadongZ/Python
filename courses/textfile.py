try:
    with open ("./data/guido_bio.txt") as fobj:
        bio = fobj.read()
except FileNotFoundError:
    bio = None

print(bio)


oceans = ["Pacific", "Atlantic", "Indian", "Southern", "Arctic"]

with open("./data/oceans.txt", "w") as f:
    for c in oceans:
        print(c, file=f)

with open("./data/oceans.txt", "a") as f: #a for append
    print(23*"=", file=f)
    print("There are five oceans on the planet", file=f)
