import os
datos = list()
while (True):
    os.system("cls" if os.name=="nt" else "clear")
    try:
        # datos[len(datos):len(datos)] = input("ingrese un numero: ")
        datos.append(int(input(f"{"ingrese un numero:" .upper()}")))
        print(datos)
        input()
    except IndexError:
        print("fuera de rango")
        input()
        break
    except ValueError:
        input("dato no numérico, pulse enter...".upper())
        continue
    else:
        seguir = input("Desea seguir s/n: ").lower()
        match (seguir):
            case "n":
                input ("hasta luego, presione enter ...".upper())
                break
            case "no":
                input ("hasta luego, presione enter ...".upper())
                break
            case "s":
                continue
            case "si":
                continue
            case _:
                input("opción no válida, pulse enter...".upper())
    finally:
        
        valor = True if (int(input("ingrese un numero: "))%2 == 0) else False
        print(valor)
        matris = [i for i in range (13) if i%2==0]
        for i in matris:
            print ("valores de i: ",i, end=" ")
        else:
            print("\nfinalizo correctamente todo".upper())
        input()
        os.system("cls" if os.name=="nt" else "clear")

