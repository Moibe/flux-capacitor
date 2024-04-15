import time
import nodes
import gradio_client

def saldoParaAccion(tokens):
  #Donde 1 es el cobro por acción, es decir, tiene capacidad por lo menos de realizar una acción.
   if tokens >= 1: 			
    return True

   else:
    print("Tokens insuficientes para realizar la operación, recargar más.")
    return False


def getResult(content): 

    print("El content que le estoy pasando a Moibe/Basico es: ", content)
    time.sleep(4)

    #Agregar aquí un validador en el que solo realice el trabajo si el nombre del trabajo es el adecuado para la api usada. 
    #Esto con el finn de evitar que se ponga un trabajo eesconocido para recibir menos cobro por la acción. 
    #Es decir, se valida el trabajo y el débito a través de ese string.

    if nodes.work == "picswap":
      print("Trabajo especificado correctamente, se realizará la acción: ")
      time.sleep(1)

      #Llamado a App que ejecuta la acción.
      client = gradio_client.Client(nodes.aplicacion, nodes.hf_token, verbose=False)
    
      result = client.predict(
          content,
          api_name="/predict"
      )
      #Revisa si la app en cuestión podría regresar algún resultado extraño además del esperado. Esto se revisa en la otra App.
      return result
    
    else: 
      print("El trabajo  no existe, especificar la variable Work correctamente.")
      #Regresa cero si el trabajo no se realizó por haber especificado incorrectamente el Work.
      return 0