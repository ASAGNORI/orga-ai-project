from pydantic_settings import BaseSettings
from typing import Optional

class HanaSettings(BaseSettings):
    HANA_HOST: str
    HANA_PORT: int
    HANA_USER: str
    HANA_PASSWORD: str
    HANA_SCHEMA: str
    HANA_SSL: bool = True
    HANA_CONNECTION_TIMEOUT: int = 30
    HANA_POOL_SIZE: int = 5
    HANA_MAX_OVERFLOW: int = 10

    class Config:
        env_file = ".env"
        case_sensitive = True

hana_settings = HanaSettings()

def get_hana_connection_string() -> str:
    """Generate HANA connection string from settings."""
    conn_str = f"host={hana_settings.HANA_HOST};port={hana_settings.HANA_PORT};"
    conn_str += f"user={hana_settings.HANA_USER};password={hana_settings.HANA_PASSWORD}"
    
    if hana_settings.HANA_SCHEMA:
        conn_str += f";schema={hana_settings.HANA_SCHEMA}"
    
    if hana_settings.HANA_SSL:
        conn_str += ";encrypt=true"
    
    return conn_str 