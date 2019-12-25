def max_num(num1, num2, num3):
    """Find the max of three numbers you input"""
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

#num1 = float(input("Enter first number: "))
#num2 = float(input("Enter second number: "))
#num3 = float(input("Enter third number: "))

#print(max_num(num1, num2, num3))

def triangle_area(b, h):
    """Returns the area of a triangle with base b and height h."""
    return 0.5*b*h

print(triangle_area(10,18))


def cm(feet=0, inches=0):
    """Converts a length from feet and inches to centimeters."""
    inches_to_cm = inches * 2.54
    feet_to_cm = feet*12*2.54
    return inches_to_cm + feet_to_cm

print(cm(5,10))
print(cm(inches=90))


