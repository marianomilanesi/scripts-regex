import re

# Expresión regular para encontrar el nombre de usuario
pattern = r'^([^:]+)::'

# Conjunto para almacenar los nombres de usuario únicos
usuarios_unicos = set()

# Lee el archivo "hashes.txt" línea por línea
with open("/usr/share/responder/logs/<Path_archivo>", "r") as file:
    for line in file:
        match = re.search(pattern, line)
        if match:
            usuario = match.group(1)
            usuarios_unicos.add(usuario)

# Convierte el conjunto de usuarios únicos de nuevo a una lista
usuarios_unicos_lista = list(usuarios_unicos)

# Imprime la lista de usuarios únicos
for usuario in usuarios_unicos_lista:
    print("Nombre de usuario:", usuario)