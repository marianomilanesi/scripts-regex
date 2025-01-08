import base64

# Leer contraseñas o usuarios desde un archivo
def read_file(file_path):
    try:
        with open(file_path, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print(f"Error: El archivo '{file_path}' no existe.")
        exit(1)

# Generar combinaciones codificadas en Base64
def generate_base64_combinations(users, passwords, output_file):
    base64_combinations = []
    for user in users:
        for password in passwords:
            combo = f"{user}:{password}"  # Formato usuario:contraseña
            encoded_combo = base64.b64encode(combo.encode()).decode()  # Codificar en Base64
            base64_combinations.append(encoded_combo)
    
    # Guardar las combinaciones en el archivo de salida
    with open(output_file, "w") as file:
        file.write("\n".join(base64_combinations))

    print(f"Combinaciones generadas y guardadas en: {output_file}")

# Solicitar los archivos al usuario
print("Por favor, ingresa los nombres de los archivos:")

user_file = input("Archivo de usuarios (uno por línea): ").strip()
password_file = input("Archivo de contraseñas (una por línea): ").strip()
output_file = input("Archivo de salida (donde se guardarán las combinaciones): ").strip()

# Leer los datos de los archivos
users = read_file(user_file)
passwords = read_file(password_file)

# Generar y guardar combinaciones
generate_base64_combinations(users, passwords, output_file)
