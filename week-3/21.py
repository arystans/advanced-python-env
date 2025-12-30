import math

a = float(input("Enter a number: "))

def t(a):
    return math.sqrt(3) * a * a /4

def h(a):
    return 6 * t(a)

print(h(a))
