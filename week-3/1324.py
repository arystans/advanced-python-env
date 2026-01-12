def rangel (m,n):
    while m <= m + n:
        yield m # Генерирует значение (и)
        m += 1
k=int(input( "к= "))
c = rangel(0, k) #с=0.0
for i in rangel (0, k+2):
    z=next(c)/10 # следующее значение
    print(z," ", z*z)