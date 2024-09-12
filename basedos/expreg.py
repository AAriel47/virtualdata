import os
import re
os.system("cls" if os.name=="nt" else "clear")
import re

# Expresión regular corregida
pattern = r'(?:https?|ftp):\/\/(?:[a-zA-Z0-9\-]+\.)+[a-zA-Z]{2,}(?:\/[^\s]*)?'

# La URL a comprobar
#direc = 'http://example.com/path/to/resource'
direc = "https://google.com.argentina"

# Usar re.match con la expresión regular
#val = re.match(pattern, direc)
reg = re.compile(pattern)
val=reg.match(direc)
# Comprobar si se encontró una coincidencia
if val:
    print("Coincidencia encontrada:", val.group())
    #print("Coincidencia encontrada:", val.match(direc))
else:
    print("No se encontró ninguna coincidencia")
print(" ")

email= "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
email2="^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
