import subprocess

def get_sha256(path):
    """Hash SHA-256 para Linux/macOS usando sha256sum"""
    return subprocess.run(["sha256sum", path], capture_output=True, text=True).stdout.split()[0]

def get_sha256_windows(path):
    import os
    # Convierte la ruta a absoluta y reemplaza \ por /
    path = os.path.abspath(path).replace("\\", "/")
    try:
        result = subprocess.run(["certutil", "-hashfile", path, "SHA256"],
                                capture_output=True, text=True, check=True)
        lines = result.stdout.splitlines()
        # Filtramos la primera línea que contiene 'SHA256 hash of file ...'
        # y la última que dice 'CertUtil: -hashfile command completed successfully.'
        hash_line = [line for line in lines if all(c in "0123456789abcdefABCDEF" for c in line.replace(" ", ""))]
        return hash_line[0].replace(" ", "")
    except subprocess.CalledProcessError:
        print(f"Error calculando hash del archivo: {path}")
        exit(1)
    except IndexError:
        print(f"No se pudo extraer el hash de la salida de certutil para: {path}")
        exit(1)


def seleccionar_os():
    print("Selecciona tu sistema operativo:")
    print("1. Windows")
    print("2. Linux")
    while True:
        opcion = input("Introduce el número de tu sistema operativo: ")
        if opcion == "1":
            return "Windows"
        elif opcion == "2":
            return "Linux"
        else:
            print("Opción no válida. Intenta de nuevo.")

# Elegir el sistema operativo
sistema = seleccionar_os()

# Pide las rutas de los archivos a comparar
fileOG = input("Ruta del archivo original: ")
file2 = input("Ruta del archivo a contrastar: ") 

# Calcula los hashes según el OS
if sistema == "Windows":
    hashOG = get_sha256_windows(fileOG)
    hash2 = get_sha256_windows(file2)
else:
    hashOG = get_sha256(fileOG)
    hash2 = get_sha256(file2)

# Compara los hashes y determina el resultado
if hashOG == hash2:
    print("[+] Éxito! La verificación de integridad determina que el archivo NO ha sido modificado.")
else:
    print("/!\ La verificación de integridad determina que el archivo ha sido modificado.") 
