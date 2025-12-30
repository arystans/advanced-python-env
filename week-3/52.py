n = int(input())
s =""
for i in range(1,n):
    if n % i == 0:
        s += str(n//i) + " "
print(s, "1")