from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import tasks, ai
from app.core.database import Base, get_engine, initialize_supabase
from app.core.models import User, Task, Goal, MindMap, Message
from .core.config import settings

app = FastAPI(
    title="AI Project API",
    description="API for AI Project with Ollama integration",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, especificar os domínios permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create database engine and initialize Supabase
engine = get_engine()

# Create all tables
Base.metadata.create_all(bind=engine)

# Initialize Supabase client
initialize_supabase()

# Routers
app.include_router(tasks.router, prefix="/api/v1/tasks")
app.include_router(ai.router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Welcome to AI Project API"}

@app.get("/api/v1/health")
async def health():
    return {"status": "ok"} 






 

