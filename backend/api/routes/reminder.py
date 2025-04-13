# backend/api/routes/reminder.py

from fastapi import APIRouter, Request
from backend.ai.reminder_agent import analisar_texto_com_ia
import json

router = APIRouter()

@router.post("/reminder")
async def analisar_texto(request: Request):
    data = await request.json()
    texto = data.get("mensagem", "")
    resposta_raw = analisar_texto_com_ia(texto)

    try:
        resposta = json.loads(resposta_raw)
    except Exception:
        resposta = {"ação": "ignorar", "erro": "Erro ao processar resposta da IA"}

    return resposta
