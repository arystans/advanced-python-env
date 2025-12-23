s1 = input().strip()
s2 = input().strip()

if len(s1) != len(s2):
    print("NO")
else:
    ok = True
    for ch in s1:
        if s1.count(ch) != s2.count(ch):
            ok = False
            break
    print("YES" if ok else "NO")
