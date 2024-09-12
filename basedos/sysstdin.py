import sys
mensaje =sys.stdin.read()
print(mensaje)
#solo se ejecutan desde consola
import sys
import io
men = io.stringIO()
sys.stdout=men
print("este mensaje se almacena en una variable")
resultado = men.getValue()
sys.stdout=sys.__stdout__
sys.stderr.write("esto es un error \n")
