from supabase import create_client, Client
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from .config import settings

# Initialize Supabase client with the simplest possible approach
try:
    supabase = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)
except Exception as e:
    print(f"Error initializing Supabase client: {e}")
    # Create a dummy client for development
    supabase = None

def get_supabase_client() -> Client:
    # Create client with minimal configuration
    return create_client(
        supabase_url=settings.SUPABASE_URL,
        supabase_key=settings.SUPABASE_KEY
    )

supabase = get_supabase_client() 


 