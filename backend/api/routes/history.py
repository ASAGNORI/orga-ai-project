from fastapi import APIRouter, HTTPException
from app.core.supabase import supabase
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()

@router.get("/history")
async def get_history():
    try:
        logger.info("Buscando histórico de mensagens...")
        response = supabase.table("messages").select("*").order("created_at", desc=True).limit(20).execute()
        logger.info(f"Dados recebidos do Supabase: {response.data}")
        
        # Transformar os dados para o formato esperado pelo frontend
        formatted_data = []
        for item in response.data:
            formatted_data.append({
                "id": item.get("id", ""),
                "content": item.get("input", ""),
                "role": "user",
                "timestamp": item.get("created_at", "")
            })
            formatted_data.append({
                "id": f"{item.get('id', '')}-response",
                "content": item.get("response", ""),
                "role": "assistant",
                "timestamp": item.get("created_at", "")
            })
        
        logger.info(f"Dados formatados: {formatted_data}")
        return formatted_data
    except Exception as e:
        logger.error(f"Erro ao buscar histórico: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error fetching history: {str(e)}") 