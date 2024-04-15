import nodes
import theApp
import sulkuGateway

#Flux capacitor une la Autenticación y la App.
def do(access, content):

	#AUTENTICACIÓN#
 	#Obten cantidad de tokens dispobibles vía Sulku para ese usuario.
	resultado = sulkuGateway.getTokens(access)

	#Si el resultado es un entero, es token.
	if isinstance(resultado, int): 
		print("El númmero si es un entero.")
		tokens = resultado
		continuar = True
		print("La cantidad de tokens recibida de getTokens es: ", tokens)
	else: 
		print("Se recibió un mensaje:", resultado)
		continuar = False

	#ACCIÓN#
	#Habiendo suficientes tokens para la acción, realizarla.
	if continuar is True and theApp.saldoParaAccion(tokens):
		resultado = theApp.getResult(content)
		print("ÉSte es el resultado accesado y obtenido: ", resultado)
	else: 
		resultado = 0
		print("No hay suficientes tokens para ejecutar la operación.")
      
	#CHARGE TOKENS
	#Si se generó un resultado de AI entonces si hay que debitar el token correspondiente basado en la regla propia de la app.
	if resultado != 0:
		sulkuGateway.debitTokens(access)
	else:
		"No se debita porque no hubo resultado."
		
	return tokens, resultado