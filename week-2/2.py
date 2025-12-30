a = input().strip()
b = input().strip()
bb = b + b
m = len(b)
c = 0
for i in range(len(a) - m + 1):
    sub = a[i:i+m]
    if sub in bb:
        c += 1
print(c)
