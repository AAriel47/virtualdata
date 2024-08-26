import os
"""os.system('cls' if os.name == 'nt' else 'clear')
cuentaLetras = {}
palabra = input("Ingrese una palabra: ")
for letras in palabra:
    cuentaLetras[letras] = cuentaLetras.get(letras,0)+1
    #print(f"letras: {letras} cuentaletras: {cuentaLetras}")
    #input()
#print(f"letras: {cuentaLetras} cuentaletras: {cuentaLetras}")
print(cuentaLetras)
cun = [] 

cuentaLetras2 = cuentaLetras.items()
e = 0
for i in cuentaLetras2:
    cun.insert(e,i)
    e += 1
cun.sort()
print (cun)
"""

import os
os.system('cls' if os.name == 'nt' else 'clear')
cuentaLetras = {}
palabra = input("Ingrese una palabra: ")
for letras in palabra:
    cuentaLetras[letras] = cuentaLetras.get(letras,0)+1
    #print(f"letras: {letras} cuentaletras: {cuentaLetras}")
    #input()
#print(f"letras: {cuentaLetras} cuentaletras: {cuentaLetras}")
print(cuentaLetras)
cun = [0] * int(len(cuentaLetras))
#cun2 = list()
cuentaLetras2 = cuentaLetras.items()

e = 0
for i in cuentaLetras2:
    cun[e]=i
    #cun2 = cun + cun
    e += 1

#print("cun2", cun2)
cun.sort()

print (cun)
#el error de aca es por que genera dic y los almacena en un array y no lo puede ordenar
#prueba con ariel y luego con misss