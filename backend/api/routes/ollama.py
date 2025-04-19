from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import requests
from app.core.database import get_supabase
from datetime import datetime
import logging
import traceback

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()

class Message(BaseModel):
    input: str
    model: str = "llama3"

@router.post("/generate")
async def generate_response(msg: Message):
    try:
        # Gerar resposta do Ollama
        payload = {
            "model": msg.model,
            "prompt": msg.input,
            "stream": False
        }
        logger.info(f"Enviando requisição para Ollama: {payload}")
        response = requests.post("http://localhost:11434/api/generate", json=payload)
        response.raise_for_status()
        data = response.json()
        logger.info(f"Resposta recebida do Ollama: {data}")

        # Salvar no Supabase
        try:
            supabase = get_supabase()
            supabase.table("messages").insert({
                "input": msg.input,
                "response": data["response"],
                "created_at": datetime.utcnow().isoformat()
            }).execute()
            logger.info("Mensagem salva no Supabase com sucesso")
        except Exception as e:
            logger.error(f"Erro ao salvar no Supabase: {str(e)}")
            # Continuar mesmo com erro no Supabase

        return data
    except requests.exceptions.RequestException as e:
        logger.error(f"Erro na comunicação com Ollama: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error communicating with Ollama: {str(e)}")
    except Exception as e:
        logger.error(f"Erro interno: {str(e)}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

# Alias para a rota /chat
@router.post("/chat")
async def chat_endpoint(msg: Message):
    logger.info(f"Recebida requisição na rota /chat: {msg}")
    try:
        # Abordagem simplificada para a rota /chat
        payload = {
            "model": msg.model,
            "prompt": msg.input,
            "stream": False
        }
        logger.info(f"Enviando requisição para Ollama: {payload}")
        
        # Verificar se o Ollama está rodando
        try:
            ollama_status = requests.get("http://localhost:11434/api/tags")
            logger.info(f"Ollama está rodando: {ollama_status.status_code}")
        except Exception as e:
            logger.error(f"Ollama não está acessível: {str(e)}")
            raise HTTPException(status_code=503, detail="Ollama service is not available")
        
        # Enviar requisição para o Ollama
        response = requests.post("http://localhost:11434/api/generate", json=payload)
        response.raise_for_status()
        data = response.json()
        logger.info(f"Resposta recebida do Ollama: {data}")
        
        # Salvar no Supabase
        try:
            supabase = get_supabase()
            supabase.table("messages").insert({
                "input": msg.input,
                "response": data["response"],
                "created_at": datetime.utcnow().isoformat()
            }).execute()
            logger.info("Mensagem salva no Supabase com sucesso")
        except Exception as e:
            logger.error(f"Erro ao salvar no Supabase: {str(e)}")
            # Continuar mesmo com erro no Supabase
        
        return data
    except Exception as e:
        logger.error(f"Erro na rota /chat: {str(e)}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=f"Error in chat endpoint: {str(e)}") 