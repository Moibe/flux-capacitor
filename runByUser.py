import time
import MiProgramaEnHF 

def obtener_clave_archivo(ruta_archivo):
  
  with open(ruta_archivo, "r") as archivo:
    clave = archivo.read().strip()
  return clave

print("Init access sequence.")

name = "Moy"

# Ejemplo de uso
ruta_archivo = "key.key"
sulkukey = obtener_clave_archivo(ruta_archivo)
print("Ésta es la sulkukey que se obtuvo del archivo: ", sulkukey)
time.sleep(7)


tokens, result = MiProgramaEnHF.flux_capacitor(sulkukey, name)

print("Available tokens: ", tokens)
print("Éste es el resultado final total...", result)