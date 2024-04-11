import time
import nodes
import flux_capacitor 

def obtener_clave_archivo(ruta_archivo):
  
  with open(ruta_archivo, "r") as archivo:
    clave = archivo.read().strip()
  return clave

print("Initializing...")
time.sleep(1)

ruta_archivo = "key"
sulkukey = obtener_clave_archivo(ruta_archivo)
name = nodes.name

tokens, result = flux_capacitor.do(sulkukey, name)

print("Available tokens now: ", tokens)
print("Éste es el resultado de la acción realizada:", result)