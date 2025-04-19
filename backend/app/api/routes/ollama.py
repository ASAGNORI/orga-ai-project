from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, Field
import requests
from app.core.config_instance import settings
import logging
from typing import Optional
from fastapi.security import APIKeyHeader
from datetime import datetime, timedelta
from collections import defaultdict

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()

# Rate limiting
RATE_LIMIT = 10  # requests per minute
rate_limit_store = defaultdict(list)

def check_rate_limit(api_key: str):
    now = datetime.now()
    minute_ago = now - timedelta(minutes=1)
    
    # Clean old requests
    rate_limit_store[api_key] = [t for t in rate_limit_store[api_key] if t > minute_ago]
    
    # Check rate limit
    if len(rate_limit_store[api_key]) >= RATE_LIMIT:
        raise HTTPException(
            status_code=429,
            detail="Rate limit exceeded. Please try again later."
        )
    
    # Add current request
    rate_limit_store[api_key].append(now)

class Message(BaseModel):
    input: str = Field(..., min_length=1, max_length=1000)
    model: str = Field(default="llama2", min_length=1, max_length=50)

@router.post("/generate")
async def generate_text(
    message: Message,
    api_key: str = Depends(APIKeyHeader(name="X-API-Key"))
):
    try:
        # Check rate limit
        check_rate_limit(api_key)
        
        # Validate API key
        if api_key != settings.OLLAMA_API_KEY:
            raise HTTPException(
                status_code=401,
                detail="Invalid API key"
            )
        
        response = requests.post(
            settings.OLLAMA_API_URL,
            json={
                "model": message.model,
                "prompt": message.input,
                "stream": False
            },
            timeout=30  # Add timeout
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        logger.error("Ollama API request timed out")
        raise HTTPException(
            status_code=504,
            detail="Request to Ollama API timed out"
        )
    except requests.exceptions.RequestException as e:
        logger.error(f"Error calling Ollama API: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Error generating text: {str(e)}"
        )
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="An unexpected error occurred"
        ) 