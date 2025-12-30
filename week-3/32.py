n = input().split()
s = ""
for i in n:
    sorted(i)
    for a in sorted(i):
        s = s + a
    print(s)
    s = ""