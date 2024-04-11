import time
import gradio_client
import sulkuGateway
import thisApp
import nodes

#Flux capacitor representa la fusión de los flujos de sulku y el programa a usar.
#Son acciones generales por lo que pueden aplicar para cualquier app subida en HF.
def do(sulkukey, name):
 
	#Obten cantidad de tokens dispobibles vía Sulku para ese usuario.
	tokens = sulkuGateway.getTokens(sulkukey)
	print("La cantidad de tokens recibida de getTokens es: ", tokens)

	#Basado en las propias reglas de ésta app, le dará o no acceso con un True o False.  
	acceso = thisApp.bizRules(tokens)

	print("El resultado de acceso es: ", acceso)
	print("Y el tipo de acceso es : ", type(acceso))
	time.sleep(8)

	#Si el acceso es True, entonces le permites hacer la acción de ésta app.
	if acceso is True:
		resultado = thisApp.getResult(name)
		print("ÉSte es el resultado accesado y obtenido: ", resultado)
	else: 
		resultado = 0
		print("No hay suficientes tokens para ejecutar la operación.")
      
	#Si se generó un resultado de AI entonces si hay que debitar el token correspondiente basado en la regla propia de la app.
	if resultado != 0:
		sulkuGateway.debitTokens(sulkukey, nodes.cuantos)
	else:
		"No se debita porque no hubo resultado."
		
	return tokens, resultado

if __name__ == "__main__":
    flux_capacitor()