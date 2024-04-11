def obtener_clave_archivo(ruta_archivo):
  
  with open("key", "r") as archivo:
    clave = archivo.read().strip()
  return clave