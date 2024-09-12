import os
import sys
datos = [i for i in range(10) if i%2==0]
os.system("cls" if os.name=="nt" else "clear")
found = False
for val in datos:
    val = str(val)
    if "3" in val:
        found = True
        break

if not found:
    print(not found)
    print("no se encuentra")
valor = [i for i in range(11)]
for i, item in enumerate(valor):
    print(i, item)
nu = [i for i in range(1,11)]
paridad = list()

for i in nu:
    if i%2==0:
        paridad.append("par  : ")
        
    else:
        paridad.append("impar: ")

print (nu)
print(paridad)
os.system("cls" if os.name=="nt" else "clear")
for n, p in zip(nu,paridad):
    print(p, n)

valor = [i for i in range(18)]
paridad1 = ["Par:  " if i%2==0 else "Impar: " for i in valor]
e = 1
print()
for par, va in zip(paridad1, valor):
    print ("  ", par, va, end="")
    if e ==7:
        print()
        e = 0
    e += 1
print()
print("resuelto")
resul = ["{}{}".format(pa, nu) for pa, nu in zip(["Par:  " if i%2==0 else "Impar:" for i in range(17)],[i for i in range(17)])]
print(resul)
print("menu principal".zfill(80))
input("  Pulse enter...")
os.system("cls" if os.name=="nt" else "clear")
import io
io.StringIO.write()