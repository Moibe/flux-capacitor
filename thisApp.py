import gradio_client

def getResult(name): 

    #Llamado a App en cuestión.
    client = gradio_client.Client("Moibe/basico", hf_token="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", verbose=False)
	
    result = client.predict(
				name,
				api_name="/predict"
		)

    return result