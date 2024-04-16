import nodes
import tools
import flux_capacitor

print("Welcome...")
print("Initializing app and servers...")

#Punto de entrada para inicialización, aquí solo se obtiene la clave y se reciban las entradas con las que se trabajará.
access = tools.obtener_clave_archivo()
#name o el parámetro que desde vía local le vayas a dar a la api de HF que realiza la acción, puede ser string, numero, imagen, etc.
content = nodes.content

tokens_now, result = flux_capacitor.do(access, content)

print("Result obtained: ", result)