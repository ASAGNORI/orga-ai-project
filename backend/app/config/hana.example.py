from pydantic_settings import BaseSettings
from typing import Optional

class HanaSettings(BaseSettings):
    # HANA connection settings
    HANA_HOST: str = "localhost"
    HANA_PORT: int = 39015
    HANA_USER: str = "SYSTEM"
    HANA_PASSWORD: str = "your_password_here"
    HANA_SCHEMA: str = "YOUR_SCHEMA"
    
    # Connection options
    HANA_SSL: bool = True
    HANA_CONNECTION_TIMEOUT: int = 30
    
    # Connection pool settings
    HANA_POOL_SIZE: int = 5
    HANA_MAX_OVERFLOW: int = 10

    class Config:
        env_file = ".env"
        case_sensitive = True 