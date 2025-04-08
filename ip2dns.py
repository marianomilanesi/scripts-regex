import re
import sys
import os

def extraer_hosts(nmap_output):
    resultados = []
    for linea in nmap_output.splitlines():
        if linea.startswith("Nmap scan report for"):
            resultados.append(linea.replace("Nmap scan report for ", "").strip())
    return resultados

def main():
    if len(sys.argv) != 2:
        print("❌ Uso incorrecto. Ejemplo:")
        print("   python3 ip2dns.py /ruta/al/archivo.nmap")
        return

    ruta_archivo = sys.argv[1]

    if not os.path.isfile(ruta_archivo):
        print(f"❌ El archivo no existe: {ruta_archivo}")
        return

    try:
        with open(ruta_archivo, "r", encoding="utf-8") as f:
            contenido = f.read()
    except Exception as e:
        print(f"⚠️ Ocurrió un error al abrir el archivo: {e}")
        return

    hosts = extraer_hosts(contenido)

    if not hosts:
        print("⚠️ No se encontraron líneas con 'Nmap scan report for'")
    else:
        print("\n✅ Hosts encontrados:\n")
        for h in hosts:
            print(h)

if __name__ == "__main__":
    main()

