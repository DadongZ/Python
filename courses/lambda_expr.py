f = lambda x: 3*x + 1

print(f(2))

full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()

print(full_name("  alex", "Zhang"))


scifi_authors = ["Isaac Asimov", "Ray Bradbury", "Robert Heinlein",
                 "Arthus C. Clarke", "Frank Herbert", "Orson Scott Card",
                "Douglas Adams", "H. G. Wells", "Dadong Zhang"]


scifi_authors.sort(key=lambda name: name.split(" ")[-1].lower())

print(scifi_authors)

def build_quadratic_function(a, b, c):
    return lambda x: a*x**2 + b*x +c

out = []

i = 0
while i <=10:
    out.append(build_quadratic_function(2,4,-6)(i))
    i +=1

print(out)

