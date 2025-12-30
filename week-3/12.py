results = []
s = 0
for a in range(0,3):
    n = input("Enter numbers: ").split()
    results.append(n)
for arr in results:
    for n in arr:
        s = s + int(n)
    avg = s / len(arr)
    print("Array:", arr, "Sum:", s, "Average:", avg)
    s,avg = 0,0