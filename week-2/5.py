allowed = "ABCEHKMOPTXY"
n = int(input())
results = []
for _ in range(n):
    p = input().strip()
    ok = True
    if len(p) != 6:
        ok = False
    elif p[0] not in allowed:
        ok = False
    elif not p[1:4].isdigit():
        ok = False
    elif p[4] not in allowed or p[5] not in allowed:
        ok = False
    results.append("Yes" if ok else "No")

for res in results:
    print(res)

