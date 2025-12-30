import math

def hypo(a, b):
    return math.sqrt(a*a + b*b)

h1 = hypo(int(input("Enter the first number: ")), int(input("Enter the second number: ")))
h2 = hypo(int(input("Enter the first number: ")), int(input("Enter the second number: ")))
print("H1:", h1, "\nH2:", h2)

print(("Max: ", max(h1, h2)),
      ("Min: ", min(h1, h2)), )
