ef all_eq(lst):
    max_len = 0
    for s in lst:
        if len(s) > max_len:
            max_len = len(s)
    r = []
    for s in lst:
        r.append(s + "_" * (max_len - len(s)))
    return r

n = input()
lst = []
for i in range(int(n)):
    lst.append(input())
all_eq(lst)
