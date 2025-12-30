def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a = int(input())
b = int(input())
g = gcd(a, b)
lcm = a * b // g

print("GCD:", g,"\nLCM:", lcm)
