import nodes
import thisApp
import sulkuGateway

def do(access, name):
 
	#Obten cantidad de tokens dispobibles vía Sulku para ese usuario.
	tokens = sulkuGateway.getTokens(access)
	print("La cantidad de tokens recibida de getTokens es: ", tokens)

	#Basado en las propias reglas de ésta app, le dará o no acceso con un True o False.  
	acceso = thisApp.bizRules(tokens)

	#Si el acceso es True, entonces le permites hacer la acción de ésta app.
	if acceso is True:
		resultado = thisApp.getResult(name)
		print("ÉSte es el resultado accesado y obtenido: ", resultado)
	else: 
		resultado = 0
		print("No hay suficientes tokens para ejecutar la operación.")
      
	#Si se generó un resultado de AI entonces si hay que debitar el token correspondiente basado en la regla propia de la app.
	if resultado != 0:
		sulkuGateway.debitTokens(access)
	else:
		"No se debita porque no hubo resultado."
		
	return tokens, resultado