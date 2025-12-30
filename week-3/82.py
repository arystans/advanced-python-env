def swap(arr):
    arr[0], arr[-1] = arr[-1], arr[0]
A = []
m = int(input("Length: "))
for i in range(m):
    A.append(int(input()))

print("Original:", A)
swap(A)
print("Result:", A)
