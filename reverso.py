import os
os.system("cls" if os.name=="nt" else "clear")
apellido = input("Ingrese un apellido:")
#apel=""
apel = reversed(apellido)
apelli=""
for a in apel:
    apelli += a
print(f"Apellido: {apelli}")
print(f"apel: {type(apel)}")
print("ale".index("a"))