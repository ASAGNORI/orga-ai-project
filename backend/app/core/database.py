from supabase import create_client, Client
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from sqlalchemy.pool import QueuePool
from sqlalchemy.exc import SQLAlchemyError
from app.core.config import settings
import logging
import tenacity
from typing import Generator, Optional
import os

logger = logging.getLogger(__name__)

# Initialize Base
Base = declarative_base()

def create_db_engine():
    """Create a SQLAlchemy engine based on environment."""
    try:
        # Use DATABASE_URL directly for local development
        database_url = settings.DATABASE_URL
        logger.info(f"Connecting to database with URL: {database_url}")
        
        engine = create_engine(
            database_url,
            pool_pre_ping=True,
            pool_size=settings.DATABASE_POOL_SIZE,
            max_overflow=settings.DATABASE_MAX_OVERFLOW,
            pool_timeout=settings.DATABASE_POOL_TIMEOUT
        )
        
        # Test the connection
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
            logger.info("Successfully connected to database")
            
        return engine
    except Exception as e:
        logger.error(f"Failed to create database engine: {str(e)}")
        raise

@tenacity.retry(
    stop=tenacity.stop_after_attempt(3),
    wait=tenacity.wait_exponential(multiplier=1, min=4, max=10),
    retry=tenacity.retry_if_exception_type(Exception),
    before=tenacity.before_log(logger, logging.INFO),
    after=tenacity.after_log(logger, logging.WARN),
)
def get_supabase_client() -> Client:
    """Get or create Supabase client with retry logic."""
    global _supabase_client
    
    if _supabase_client is None:
        try:
            logger.info("Initializing Supabase client...")
            _supabase_client = create_client(
                settings.SUPABASE_URL,
                settings.SUPABASE_ANON_KEY
            )
            # Test the connection
            _supabase_client.table('users').select("*").limit(1).execute()
            logger.info("Successfully connected to Supabase")
        except Exception as e:
            logger.error(f"Failed to initialize Supabase client: {str(e)}")
            raise
    
    return _supabase_client

def test_db_connection():
    """Test database connection."""
    try:
        db = SessionLocal()
        db.execute("SELECT 1")
        logger.info("Successfully connected to the database")
        return True
    except SQLAlchemyError as e:
        logger.error(f"Database connection test failed: {str(e)}")
        return False
    finally:
        db.close()

# Create engine instance
engine = create_db_engine()

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Initialize Supabase client
_supabase_client: Optional[Client] = None

def get_db() -> Generator[Session, None, None]:
    """Get database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def initialize_supabase():
    """Initialize Supabase client if not already initialized."""
    global _supabase_client
    if _supabase_client is None:
        _supabase_client = get_supabase_client()
    return _supabase_client

def get_supabase():
    """Get or initialize Supabase client."""
    if _supabase_client is None:
        return initialize_supabase()
    return _supabase_client
