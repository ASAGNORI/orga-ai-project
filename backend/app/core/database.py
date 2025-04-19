from supabase import create_client, Client
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.pool import QueuePool
from app.core.config_instance import settings
import logging
from tenacity import retry, stop_after_attempt, wait_exponential

logger = logging.getLogger(__name__)

# Configuração do pool de conexões
engine = create_engine(
    settings.DATABASE_URL,
    poolclass=QueuePool,
    pool_size=settings.DATABASE_POOL_SIZE,
    max_overflow=settings.DATABASE_MAX_OVERFLOW,
    pool_timeout=settings.DATABASE_POOL_TIMEOUT,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=4, max=10)
)
def get_supabase_client() -> Client:
    try:
        # Criar o cliente Supabase
        client = create_client(settings.SUPABASE_URL, settings.SUPABASE_ANON_KEY)
        return client
    except Exception as e:
        logger.error(f"Error creating Supabase client: {str(e)}")
        raise

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=4, max=10)
)
def test_db_connection():
    try:
        # Testar conexão com SQLAlchemy
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
            logger.info("Database connection test successful")
    except Exception as e:
        logger.error(f"Error testing database connection: {str(e)}")
        raise

# Testar conexão com o banco de dados
try:
    test_db_connection()
except Exception as e:
    logger.error(f"Failed to connect to database: {str(e)}")
    raise

# Inicializar cliente Supabase
try:
    supabase = get_supabase_client()
except Exception as e:
    logger.error(f"Failed to initialize Supabase client: {str(e)}")
    raise

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
