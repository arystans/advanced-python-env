import math

(a, b, c, d, diag) = input().split()

s1 = (int(a) + int(b) + int(diag)) / 2
s2 = (int(c) + int(d) + int(diag)) / 2

area = math.sqrt(s1*(s1-int(a))*(s1-int(b))*(s1-int(diag))) + \
       math.sqrt(s2*(s2-int(c))*(s2-int(d))*(s2-int(diag)))
print(area)
