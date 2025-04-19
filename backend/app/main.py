from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import tasks, ai
from app.core.database import Base, create_db_engine, initialize_supabase
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
engine = create_db_engine()
Base.metadata.create_all(bind=engine)
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






 

