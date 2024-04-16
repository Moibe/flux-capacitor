def obtener_clave_archivo():
    try:
        with open("key", "r") as archivo:
            clave = archivo.read().strip()
        return clave
    except FileNotFoundError:
        # Manejar el error de archivo no encontrado
        print("Error: El archivo de clave 'key' no se encontró.")
        return None
    except Exception as e:
        # Manejar otros errores genéricos
        print("Error inesperado al leer la clave del archivo:", e)
        return None
