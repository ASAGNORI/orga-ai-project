# backend/ai/reminder_agent.py

import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def analisar_texto_com_ia(texto_usuario: str) -> dict:
    prompt = f"""
    Você é um assistente pessoal inteligente. A seguinte mensagem foi recebida de um usuário:

    "{texto_usuario}"

    Analise e retorne um lembrete útil no seguinte formato JSON:
    {{
        "ação": "criar_lembrete" ou "ignorar",
        "mensagem": "mensagem do lembrete",
        "data": "YYYY-MM-DD" (data do evento, se possível)
    }}

    Se não for possível entender, responda:
    {{
        "ação": "ignorar"
    }}
    """

    response = requests.post(OLLAMA_URL, json={"model": "llama3", "prompt": prompt})
    return response.json()["response"]
