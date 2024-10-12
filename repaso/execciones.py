import os
import sys
class micontrol(Exception):
    pass
    
def verificar(edad):
    if int(edad) < 18:
        #sys.exit()
        raise micontrol("eres menor de edad, espera un tiempo para apostar...".capitalize())
    return "ahora si puedes participar".upper()

try:
    os.system('cls' if os.name=='nt' else 'clear')
    mensaje=verificar(input("INGRESE SU EDAD: "))
    print(mensaje)
except micontrol as e:
    print(f"{"edad no validad: ".upper()} {e}")
    print()