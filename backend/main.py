import requests 
from fastapi import FastAPI
from fastapi import APIRouter
from fastapi.middleware.cors import CORSMiddleware
from api.routes import reminder, ollama, history, task
from app.core.config import settings
from api.routes import task
from supabase import create_client
from pydantic import BaseModel

router = APIRouter()

class ChatInput(BaseModel):
    input: str
    model: str = "llama3"

@router.post("/chat")
async def chat_endpoint(data: ChatInput):
    payload = {
        "model": data.model,
        "prompt": data.input,
        "stream": False
    }

    response = requests.post("http://localhost:11434/api/generate", json=payload)

    if response.status_code == 200:
        result = response.json()
        return {"response": result.get("response", "Sem resposta")}
    else:
        return {"response": "Erro na IA"}

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3001", "http://localhost:3002"],  # Frontend Next.js
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(reminder.router, prefix=settings.API_V1_STR)
app.include_router(ollama.router, prefix=settings.API_V1_STR)
app.include_router(history.router, prefix=settings.API_V1_STR)
app.include_router(task.router, prefix=settings.API_V1_STR)

@app.get("/")
async def root():
    return {"message": "Hello World"}