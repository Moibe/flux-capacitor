def obtener_clave_archivo():
    try:
        with open("key", "r") as archivo:
            clave = archivo.read().strip()
        return clave
    except FileNotFoundError:
        # Manejar el error de archivo no encontrado
        print("Error 406: Key not found, you need a key file to run the app correctly.")
        return None
    except Exception as e:
        # Manejar otros errores genéricos
        print("Error 406: Unexpected error reading the key file:", e)
        return None
