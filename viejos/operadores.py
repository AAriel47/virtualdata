import os
os.system("cls" if os.name=="nt" else "clear")
b = list()
n = ""
try:
    a = input("ingrese un numero: ")
    print(f"numero {int(a)}")
except ValueError:
    print("valor no aceptado, se eliminaran las letras")
    input()
    i=0
    while(i<=(len(a))-1):
        b += a[i]
        i += 1
        print(b)
    for c in b:
        letra = c
        if (letra.isalpha()):
            print(f"letra {letra}")
        else:
            n += c
    m=int(n)
    print(f"tipo {type(m)} valor: {m}")



