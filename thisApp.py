import time
import gradio_client

def bizRules(tokens):

  print("Estoy dentro de thisApp.bizRules...")
  time.sleep(1)
  print("Y la cantidad de tokens que recibí es: ", tokens)
  print("Y su tipo es: ", type(tokens))
  
  #Aquí a apliará la regla en cuestión, por ejemplo si cuesta más de 1 token.
  #Para éste uso, solo cobra un token por llamada.

  int_tokens = int(tokens)
  print("Después de la conversión, int_tokens es: ", int_tokens)
  print("Y tiee el tipo: ", type(int_tokens))

  if int_tokens > 0: 			
    print("Entre al IF")
    acceso = True
    print("El type de acceso es: ", type(acceso))
    print("Y su contenido es: ", acceso)
    
  else:
    print("Entre al else")
    print("Tokens insuficientes para realizar la operación, recargar más.")
    acceso = False

  print("Éste es el acceso que voy a returnar: ", acceso)
  time.sleep(4)
  
  return acceso

def getResult(name): 
    
    print("Estoy dentro de getResult()...")
    print("El name que le estoy pasando a Moibe/Basico es: ", name)
    time.sleep(5)

    #Llamado a App que ejecuta la acción.
    client = gradio_client.Client("Moibe/basico", hf_token="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", verbose=False)
	
    result = client.predict(
				name,
				api_name="/predict"
		)

    return result