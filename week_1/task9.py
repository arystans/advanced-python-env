n = int(input())
a,p = 0,0
for i in str(n):
    p += 1
    if p < 4:
        a += int(i)
    else: a -=int(i)
if a == 0:
    print("YES")
else:
    print("NO")
