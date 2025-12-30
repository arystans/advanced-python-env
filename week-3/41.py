def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

A, B, C, D = input().split()

n = int(A) * int(D)
m = int(B) * int(C)

g = gcd(abs(n), m)
print(n // g, "/", m // g)
