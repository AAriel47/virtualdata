import limpiar
class Punto:
    pass

limpiar.limp()
blanco = Punto()
blanco.x=3.0
blanco.y=4.0
#print(f"{"("}{str(blanco.x)},{str(blanco.y)}{")"}")
def ver(p):
    print(f"{"("}{str(p.x)},{str(p.y)}{")"}")
    print(p.x)

ver(blanco)