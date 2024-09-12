import argparse

# 1. Crear un parser
parser = argparse.ArgumentParser(description="Este es un ejemplo de cómo usar argparse.")

# 2. Definir argumentos
parser.add_argument("nombre", type=str, help="Tu nombre")           # Argumento posicional
parser.add_argument("edad", type=int, help="Tu edad")               # Otro argumento posicional
parser.add_argument("-v", "--verbose", action="store_true", help="Mostrar más detalles")  # Argumento opcional

# 3. Parsear los argumentos
args = parser.parse_args()

# 4. Usar los argumentos
if args.verbose:
    print(f"Nombre: {args.nombre}")
    print(f"Edad: {args.edad}")
else:
    print(f"Hola, {args.nombre}. Tienes {args.edad} años.")
