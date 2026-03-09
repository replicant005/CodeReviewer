import requests
# calling the llm running on ollama
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen2.5-coder"


# we will be using this function for tools which have to call the llm 
def call_llm(prompt: str):

    response = requests.post(
        OLLAMA_URL,
        # we rewquire JSON to parse python dictionary
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        }
    )

    data = response.json()
    print("OLLAMA RAW RESPONSE:", data)


    
    return data.get("response", str(data))