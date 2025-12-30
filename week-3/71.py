def treugolnik(a, b):
    return a * b / 2

def bas(a, b):
    return a * b

X, Y, Z, T = input().split()

area = treugolnik(int(X), int(Y)) + bas(int(Z), int(T))
print(area)
