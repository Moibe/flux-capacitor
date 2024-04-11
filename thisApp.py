import time
import gradio_client

def bizRules(tokens):

  print("Estoy dentro de thisApp.bizRules...")
  time.sleep(1)
  print("Y la cantidad de tokens que recibí es: ", tokens)
  print("Y su tipo es: ", type(tokens))
  
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
  
  return acceso

def getResult(name): 
    
    print("El name que le estoy pasando a Moibe/Basico es: ", name)
    time.sleep(5)

    #Agregar aquí un validador en el que solo realice el trabajo si el nobre del trabajo es el adecuado para la api usada. 
    #Esto con el finn de evitar que se ponga un trabajo eesconocido para recibir menos cobro por la acción. 
    #Es decir, se valida el trabajo y el débito a través de ese string.

    #Llamado a App que ejecuta la acción.
    client = gradio_client.Client("Moibe/basico", hf_token="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", verbose=False)
	
    result = client.predict(
				name,
				api_name="/predict"
		)

    return result