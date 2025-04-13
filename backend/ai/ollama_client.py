
# backend/ai/ollama_client.py

import requests

def consultar_ollama(pergunta):
    payload = {
        "model": "llama3",
        "prompt": pergunta
    }
    resposta = requests.post("http://localhost:11434/api/generate", json=payload, stream=False)
    return resposta.json()["response"]

# Teste
if __name__ == "__main__":
    print(consultar_ollama("Crie um lembrete para estudar inglês no sábado"))
