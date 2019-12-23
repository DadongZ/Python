
def say_hi(name):
    print("Hello User " + name)

say_hi("Alex")

def cube(num):
    return num*num*num

results = cube(5)

print("The results is " + str(results))

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

print(max_num(num1, num2, num3))

