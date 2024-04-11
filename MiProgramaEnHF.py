import time
import gradio_client
import sulkuApp
import thisApp

#Flux capacitor representa la fusión de los flujos de sulku y el programa a usar.
def flux_capacitor(sulkukey, name):

	#Obten cantidad de tokens dispobibles vía Sulku.
	tokens = sulkuApp.getTokens(sulkukey)

	#Aquí a apliará la regla en cuestión, por ejemplo si cuesta más de 1 token.
	#Para éste uso, solo cobra un token por llamada.
	# if int(tokens)>0: 			
	# 	resultado = thisApp.getResult(name)
	# else:
	# 	print("Tokens insuficientes para realizar la operación, recargar más.")
	# 	resultado = 0
 
	resultado = "OK GO"

	print("Resultado obtenido dentro de Flux_Capacitor de la api de Moibe/Basico:")
	print(tokens)
	time.sleep(2)

	return tokens, resultado

if __name__ == "__main__":
    flux_capacitor()