import numpy
#import matplotlib


class hora:
    pass

def nuevah():
    horas = hora()
    horas.ho= 22
    horas.mi= 10
    horas.se = 30
    print(horas.ho, horas.mi)
    return horas
    
def imprimirh(men):
    print(men.ho, men.mi, men.se)

recibido= nuevah()
imprimirh(recibido)
