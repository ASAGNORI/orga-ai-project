from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import httpx
from app.core.config_instance import settings

router = APIRouter(prefix="/ai", tags=["ai"])

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[Message]
    model: str = "llama2"
    temperature: Optional[float] = 0.7
    max_tokens: Optional[int] = 1000

class GenerateRequest(BaseModel):
    prompt: str
    model: str = "llama2"
    temperature: Optional[float] = 0.7
    max_tokens: Optional[int] = 1000

@router.get("/models")
async def list_models():
    """Get list of available models from Ollama."""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{settings.OLLAMA_API_URL}/api/tags")
            if response.status_code == 200:
                return response.json()
            else:
                raise HTTPException(status_code=response.status_code, detail="Failed to fetch models")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/chat")
async def chat(request: ChatRequest):
    """Chat with an Ollama model."""
    try:
        async with httpx.AsyncClient() as client:
            payload = {
                "model": request.model,
                "messages": [{"role": msg.role, "content": msg.content} for msg in request.messages],
                "temperature": request.temperature,
                "max_tokens": request.max_tokens
            }
            response = await client.post(
                f"{settings.OLLAMA_API_URL}/api/chat",
                json=payload
            )
            if response.status_code == 200:
                return response.json()
            else:
                raise HTTPException(status_code=response.status_code, detail="Failed to generate chat response")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/generate")
async def generate(request: GenerateRequest):
    """Generate text using an Ollama model."""
    try:
        async with httpx.AsyncClient() as client:
            payload = {
                "model": request.model,
                "prompt": request.prompt,
                "temperature": request.temperature,
                "max_tokens": request.max_tokens
            }
            response = await client.post(
                f"{settings.OLLAMA_API_URL}/api/generate",
                json=payload
            )
            if response.status_code == 200:
                return response.json()
            else:
                raise HTTPException(status_code=response.status_code, detail="Failed to generate text")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/health")
async def health_check():
    """
    Check if the Ollama service is healthy.
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{settings.OLLAMA_API_URL}/api/health")
            if response.status_code == 200:
                return {"status": "healthy", "ollama": "connected"}
            else:
                return {"status": "healthy", "ollama": "disconnected"}
    except Exception:
        return {"status": "healthy", "ollama": "disconnected"} 