import gradio_client

def getTokens(sulkukey): 

    #Llamado a Sulku
    client = gradio_client.Client("Moibe/sulku", hf_token="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", verbose=False)
        
    tokens = client.predict(
            sulkukey,
            api_name="/print"
    ) 

    print(f"Cuenta tiene {tokens} tokens.")

    return tokens