import os
import requests

def generate_text(input_text: str) -> dict:
    payload = {
        "model": os.getenv("OLLAMA_MODEL", "llama3"),
        "prompt": input_text,
        "temperature": float(os.getenv("OLLAMA_TEMP", 0.7)),
        "max_tokens": int(os.getenv("OLLAMA_MAX_TOKENS", 1024)),
        "stream": False
    }

    endpoint = os.getenv("OLLAMA_API_URL", "http://localhost:11434/api/generate")
    response = requests.post(endpoint, json=payload)
    return response.json()