import os
os.system("cls" if os.name=="nt" else "clear")
import math
import itertools
math.pow(2,3)
from array import array
#a = array("i",[i for i in range(10) if i%2==0])
a = [i for i in range(10) if i%2==0]
print ((a))
for e in a:
    print (e)
    if e > 4:
        break
else:
    print ("exitosss!!!")
    input()

print("hola como estas".startswith("hola"))
for i in range(10):
    print(i)
else:
    print("final exitosa")
os.system("cls" if os.name=="nt" else "clear")
opc = int(input("Ingrese un numero 1-3: "))
match opc:
    case 1:
        lis = [i for i in range(10) if i%2==0]
        print(lis)
        for i in range(len(lis)):
            print (i, lis[i])
    case 2:
        lis2 = [i for i in range(10,20) if i%2==0]
        print(lis2)
        while i < range(len(lis2)):
            print(1, lis2[i])
    case 3:
        print([i for i in range(30,40) if i%2==0])
    case _:
        print("opción no válida".upper())
for i in range(1, 6 + 1):
    for j in range(6, 0, -1):
        print(j if j <= i else " ", end = " ")
print()