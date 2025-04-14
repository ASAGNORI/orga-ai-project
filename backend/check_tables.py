from app.core.supabase import supabase
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def check_messages_table():
    try:
        # Verificar se a tabela messages existe
        logger.info("Verificando se a tabela messages existe...")
        
        # Tentar inserir um registro de teste
        result = supabase.table("messages").select("*").limit(1).execute()
        logger.info(f"Tabela messages existe. Contagem: {len(result.data)}")
        
        # Verificar a estrutura da tabela
        logger.info("Estrutura da tabela messages:")
        for record in result.data:
            logger.info(f"Campos: {record.keys()}")
            break
            
    except Exception as e:
        logger.error(f"Erro ao verificar a tabela messages: {str(e)}")
        logger.info("Tentando criar a tabela messages...")
        
        try:
            # Criar a tabela messages
            supabase.rpc(
                "create_messages_table",
                {}
            ).execute()
            logger.info("Tabela messages criada com sucesso!")
        except Exception as create_error:
            logger.error(f"Erro ao criar a tabela messages: {str(create_error)}")
            logger.info("Tentando criar a tabela usando SQL direto...")
            
            try:
                # Criar a tabela usando SQL direto
                supabase.query("""
                CREATE TABLE IF NOT EXISTS messages (
                    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                    input TEXT NOT NULL,
                    response TEXT NOT NULL,
                    created_at TIMESTAMP WITH TIME ZONE DEFAULT now()
                );
                """).execute()
                logger.info("Tabela messages criada com sucesso usando SQL direto!")
            except Exception as sql_error:
                logger.error(f"Erro ao criar a tabela usando SQL direto: {str(sql_error)}")

if __name__ == "__main__":
    check_messages_table() 