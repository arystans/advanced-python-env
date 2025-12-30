def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

A, B, C, D = input().split()

n = int(A) * int(D) - int(B) * int(C)
m = int(B) * int(D)

g = gcd(abs(n), m)
print(n // g, "/", m // g)
