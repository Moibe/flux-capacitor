import time
import gradio_client

def getTokens(sulkukey):

    
    client = gradio_client.Client("Moibe/sulku", hf_token="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", verbose=False)
        
    tokens = client.predict(
            sulkukey,
            api_name="/getTokens"
    ) 

    print(f"Cuenta tiene {tokens} tokens.")    

    return tokens

def debitTokens(sulkukey, cuantos):
    
     
    client = gradio_client.Client("Moibe/sulku", hf_token="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", verbose=False)
        
    tokens = client.predict(
            sulkukey,
            cuantos,
            api_name="/debitTokens"
    ) 

    print(f"Cuenta tiene {tokens} tokens.")    

    return tokens
    