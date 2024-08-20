import os
os.system("cls" if os.name=="nt" else "clear")
"""i = 1
while i < 7:
    print("\t", 2*i, "\t",)
    i += 1

---otro prog-------
i = 1
def multi(n):
    global i
    while i<n:
        print("\t", n*i, "\t", end="")
        i += 1

multi(int(input("Ingrese un número: ")))"""
#lim="os.system('cls' if os.name=='nt' else 'clear')"
#exec(lim)
#os.getcwd()
#os.chdir("ver")
#import importlib
#importlib.reload("azar.py")

def multi(n, mas):
    i = 1
    #print("multi", id(i))
    while i<=mas:
        #if i<=n:
        print(n*i, "\t", end="")
        i += 1

def cal(mas):
    i = 1
    #print("cal", id(i))
    while i<=mas:
        multi(i, i)
        #multi(i, mas)
        print()
        #input()
        i += 1


while (True):
    os.system("cls" if os.name=="nt" else "clear")
    try:
        cal(int(input("Ingrese un número: ")))
        break
    except ValueError:
        input("el valor ingresado no es valido, pulse enter...".upper())
        continue


