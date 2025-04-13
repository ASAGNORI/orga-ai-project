from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # API
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Orga AI"
    
    # Supabase
    SUPABASE_URL: str = "http://127.0.0.1:54321"
    SUPABASE_KEY: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZS1kZW1vIiwicm9sZSI6ImFub24iLCJleHAiOjE5ODM4MTI5OTZ9.CRXP1A7WOeoJeXxjNni43kdQwgnWNReilDMblYTn_I0"
    
    # Ollama
    OLLAMA_API_URL: str = "http://localhost:11434/api/generate"
    
    class Config:
        case_sensitive = True
        env_file = ".env"

settings = Settings() 
