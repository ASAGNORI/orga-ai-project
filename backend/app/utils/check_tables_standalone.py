import os
import logging
from sqlalchemy import text, create_engine
from dotenv import load_dotenv

# Configuração do logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Carrega as variáveis de ambiente
env_file = os.getenv("ENV_FILE", ".env.local")
load_dotenv(env_file)

def get_database_url():
    """
    Obtém a URL do banco de dados do ambiente.
    """
    host = "localhost"
    port = os.getenv("POSTGRES_PORT", "54322")
    user = os.getenv("POSTGRES_USER", "postgres")
    password = os.getenv("POSTGRES_PASSWORD", "postgres")
    database = os.getenv("POSTGRES_DB", "postgres")
    
    return f"postgresql://{user}:{password}@{host}:{port}/{database}"

def check_table_exists(engine, table_name: str) -> bool:
    """
    Verifica se uma tabela existe no banco de dados usando SQLAlchemy.
    
    Args:
        engine: SQLAlchemy engine
        table_name (str): Nome da tabela a ser verificada
        
    Returns:
        bool: True se a tabela existe, False caso contrário
    """
    try:
        with engine.connect() as conn:
            # Consulta para verificar se a tabela existe
            result = conn.execute(text(
                """
                SELECT EXISTS (
                    SELECT FROM information_schema.tables 
                    WHERE table_schema = 'public' 
                    AND table_name = :table_name
                )
                """
            ), {"table_name": table_name})
            exists = result.scalar()
            
            if exists:
                # Se a tabela existe, vamos verificar sua estrutura
                columns = conn.execute(text(
                    """
                    SELECT column_name, data_type 
                    FROM information_schema.columns 
                    WHERE table_schema = 'public' 
                    AND table_name = :table_name
                    """
                ), {"table_name": table_name})
                
                logger.info(f"\nEstrutura da tabela {table_name}:")
                for column in columns:
                    logger.info(f"  - {column.column_name}: {column.data_type}")
            
            return exists
    except Exception as e:
        logger.error(f"Erro ao verificar tabela {table_name}: {str(e)}")
        return False

def main():
    """
    Função principal que executa a verificação das tabelas.
    """
    try:
        # Obtém a URL do banco de dados
        database_url = get_database_url()
        
        logger.info(f"Arquivo de ambiente: {env_file}")
        logger.info(f"Conectando ao banco de dados: {database_url}")
        
        engine = create_engine(database_url)
        
        # Lista de tabelas para verificar
        tables = [
            "users",
            "tasks",
            "goals",
            "focus_sessions",
            "mind_maps",
            "messages"
        ]
        
        logger.info("Iniciando verificação das tabelas...")
        results = {}
        
        for table_name in tables:
            exists = check_table_exists(engine, table_name)
            results[table_name] = exists
            status = "✅ Existe" if exists else "❌ Não existe"
            logger.info(f"\n{table_name}: {status}")
        
        logger.info("\nResumo da verificação:")
        for table_name, exists in results.items():
            status = "✅ Existe" if exists else "❌ Não existe"
            logger.info(f"{table_name}: {status}")
            
    except Exception as e:
        logger.error(f"Erro durante a verificação das tabelas: {str(e)}")

if __name__ == "__main__":
    main() 