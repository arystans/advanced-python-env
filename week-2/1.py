s = input().strip()
c = 0
for i in range(len(s)-4):
    if s[i:i+5] == ">>-->":
        c += 1
    if s[i:i+5] == "<--<<":
        c += 1
print(c)
