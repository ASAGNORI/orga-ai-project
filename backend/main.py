from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import reminder
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3001"],  # Frontend Next.js
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(reminder.router, prefix=settings.API_V1_STR)

@app.get("/")
async def root():
    return {"message": "Hello World"}