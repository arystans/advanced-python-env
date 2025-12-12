N1 = int(input("First Number: "))
C = input("Operation: ")
N2 = int(input("Second Number: "))
if N2 != 0:
   print(eval(str(N1) + C + str(N2)))
else:
   print("nein")
