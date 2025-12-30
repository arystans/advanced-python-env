import math

def circle_area(r):
    return math.pi * r * r

def rectangle_area(a, b):
    return a * b

def triangle_area(a, h):
    return 0.5 * a * h
def n_angle (n, a):
    return n*a*a * math.atan(180/n)/4
n = input("Enter shape: ")
if n == "circle":
    a = float(input("Enter radius: "))
    print("Circle:", circle_area(a))
elif n == "rectangle":
    a = float(input("Enter a side length: "))
    b = float(input("Enter a side width: "))
    print("Rectangle:", rectangle_area(a, b))
elif n == "triangle":
    a = float(input("Enter a side length: "))
    h = float(input("Enter a side width: "))
    print("Triangle:", triangle_area(a,h))

elif n == "n_angle":
    a = float(input("Enter a side length: "))
    n = int(input("Enter number of angles: "))
    print("Angles:", n_angle(n, a))


