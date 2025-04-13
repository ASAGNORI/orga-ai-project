from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import users, tasks, goals
from app.core.database import Base, engine
from .core.config import settings
from .api.routes import tasks

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

# Routers
app.include_router(users.router, prefix="/api/users")
app.include_router(tasks.router, prefix="/api/tasks")
app.include_router(goals.router, prefix="/api/goals")

@app.get("/")
async def root():
    return {"message": "Orga AI API is running"} 






 

