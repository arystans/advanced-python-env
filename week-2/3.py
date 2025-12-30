s = input().strip()
a, op, b, _, c = s
if a == 'x':
    b, c = int(b), int(c)
    x = c - b if op == '+' else c + b
elif b == 'x':
    a, c = int(a), int(c)
    x = c - a if op == '+' else a - c
else:  # c == 'x'
    a, b = int(a), int(b)
    x = a + b if op == '+' else a - b
print(x)
