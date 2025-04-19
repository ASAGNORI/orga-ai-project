from pydantic_settings import BaseSettings
from typing import List, Optional, Callable
import os

class Settings(BaseSettings):
    # API
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Orga AI"
    APP_NAME: str = "OrgaAI Backend"
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000
    DEBUG: bool = False
    
    # Supabase
    SUPABASE_URL: str
    SUPABASE_ANON_KEY: str
    SUPABASE_SERVICE_ROLE_KEY: Optional[str] = None
    SUPABASE_DB_URL: Optional[str] = None
    SUPABASE_JWT_SECRET: Optional[str] = None
    
    # Database
    DATABASE_URL: str
    DATABASE_POOL_SIZE: int = 5
    DATABASE_MAX_OVERFLOW: int = 10
    DATABASE_POOL_TIMEOUT: int = 30
    
    # JWT
    JWT_SECRET: str
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    
    # CORS
    CORS_ORIGINS: List[str] = ["http://localhost:3000"]
    CORS_CREDENTIALS: bool = True
    ALLOWED_HOSTS: List[str] = ["localhost", "127.0.0.1"]
    
    # Ollama
    OLLAMA_API_URL: str = "http://host.docker.internal:11434"
    OLLAMA_API_KEY: Optional[str] = None
    OLLAMA_MODEL: str = "llama3"
    
    # Email
    SMTP_HOST: Optional[str] = None
    SMTP_PORT: Optional[int] = 587
    SMTP_USER: Optional[str] = None
    SMTP_PASSWORD: Optional[str] = None
    EMAIL_FROM: Optional[str] = None
    EMAIL_FROM_NAME: Optional[str] = None
    
    # N8N
    N8N_API_KEY: Optional[str] = None
    N8N_URL: Optional[str] = None
    
    # HANA
    HANA_HOST: Optional[str] = None
    HANA_PORT: Optional[int] = None
    HANA_USER: Optional[str] = None
    HANA_PASSWORD: Optional[str] = None
    HANA_SCHEMA: Optional[str] = None
    
    # Hugging Face
    HUGGINGFACE_API_KEY: Optional[str] = None
    
    class Config:
        case_sensitive = True
        env_file = os.getenv("ENV_FILE", ".env")
        env_file_encoding = "utf-8"
        extra = "allow"
    
    def get_current_user(self) -> Callable:
        return None

# Create an instance of Settings
settings = Settings()
