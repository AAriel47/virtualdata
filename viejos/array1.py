import array
import os
import string

os.system("cls" if os.name=="nt" else "clear")
ma1  = [1, 2, 3,[7,8,9]]
ma2 = [1,2,3]
#ma1.sort(reverse=True)
print(ma2.sort())
ma2=range(1,5)
#ma2=[1,2,3,4,5,6,7,8]
print(ma1[3][2], ma1[0])
tuplas =(1,2,3,4)
tuplas2 = (0,)
tuplas = tuplas2 + (1,2,3,4)
tuplas3 = tuple("a",)
print("hola", type(tuplas), tuplas)
print(tuplas3)
a = (1,2)
b = (3,4)
a, b = b, a
print (a, b)

#numeros=[1,2,3,4,5,6,7,8,9,10]
#paridad = list(filter(lambda n: n%2==0,numeros))
"""n1=[]
n2=[1,2,3]
clonar = lambda m, n: [m.insert(0,i) for i in n]
clonar = lambda m, n: [m.insert(len(i),i) for i in n]
clonar(n1,n2)"""
#borrar = lambda n: n.clear()
#borrar(n1)
let = ["es", "una","casa"]
l=" ".join(let)
print(l)
letras = "la casa de los espíritus"
letram = letras.split(" ")