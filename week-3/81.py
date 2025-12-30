n = int(input("Enter n: "))

for i in range(1, n+1):
    digits = [int(d) for d in str(i)]
    if 0 in digits: continue
    elif digits and all(i % d == 0 for d in digits):
        print(i, end=" ")
