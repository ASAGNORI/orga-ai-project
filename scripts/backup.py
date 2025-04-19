import os
import json
import shutil
import logging
from datetime import datetime
from supabase import create_client, Client
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# Configuração de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 1. Supabase Client Setup
SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')

if not SUPABASE_URL or not SUPABASE_KEY:
    logger.error("Supabase URL ou KEY não configurados no ambiente!")
    exit(1)

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# 2. Google Drive Setup (Autenticação com arquivo de credenciais)
gauth = GoogleAuth()
gauth.LoadCredentialsFile("/path/to/credentials.json")  # Use um arquivo de credenciais para evitar fluxo interativo
if gauth.credentials is None:
    gauth.LocalWebserverAuth()  # Se não tiver credenciais, fazer o fluxo de autenticação
elif gauth.access_token_expired:
    gauth.Refresh()  # Caso o token de acesso tenha expirado
else:
    gauth.Authorize()  # Caso já tenha credenciais válidas

drive = GoogleDrive(gauth)

# 3. Create Backup Directory
backup_root = "/mnt/data/orgaaibackups"
today = datetime.now().strftime("%Y-%m-%d")
backup_folder = os.path.join(backup_root, today)
os.makedirs(backup_folder, exist_ok=True)

# 4. Backup Data from Supabase (all tables)
def backup_supabase():
    tables = ["users", "tasks", "goals", "focus_sessions", "mind_maps", "messages"]  # Adjust with your tables
    for table in tables:
        try:
            data = supabase.table(table).select("*").execute()
            with open(f"{backup_folder}/{table}_dump.json", "w") as f:
                json.dump(data.data, f)
            logger.info(f"Backup da tabela {table} concluído com sucesso.")
        except Exception as e:
            logger.error(f"Erro ao fazer backup da tabela {table}: {e}")

# 5. Backup Local Files (folders)
def backup_local_files():
    folders_to_backup = ["./data", "./models", "./config", ".env"]  # Add other important folders/files
    for folder in folders_to_backup:
        if os.path.exists(folder):
            try:
                if os.path.isdir(folder):
                    shutil.copytree(folder, os.path.join(backup_folder, os.path.basename(folder)))
                else:
                    shutil.copy(folder, os.path.join(backup_folder, os.path.basename(folder)))
                logger.info(f"Backup do diretório {folder} realizado com sucesso.")
            except Exception as e:
                logger.error(f"Erro ao fazer backup do diretório {folder}: {e}")

# 6. Upload Backup to Google Drive
def upload_to_drive():
    try:
        folder_drive = drive.CreateFolder(today)  # Create a folder in Google Drive for today's backup
        logger.info(f"Pasta criada no Google Drive: {folder_drive['id']}")
    except Exception as e:
        logger.error(f"Erro ao criar pasta no Google Drive: {e}")
        return

    try:
        # Uploading Supabase data
        for file_name in os.listdir(backup_folder):
            if file_name.endswith(".json"):
                file_drive = drive.CreateFile({"title": file_name, "parents": [{"id": folder_drive["id"]}]})
                file_drive.SetContentFile(os.path.join(backup_folder, file_name))
                file_drive.Upload()
                logger.info(f"Arquivo {file_name} enviado para o Google Drive.")
    
        # Uploading Local Files (all other backup files)
        for file_name in os.listdir(backup_folder):
            if not file_name.endswith(".json"):
                file_drive = drive.CreateFile({"title": file_name, "parents": [{"id": folder_drive["id"]}]})
                file_drive.SetContentFile(os.path.join(backup_folder, file_name))
                file_drive.Upload()
                logger.info(f"Arquivo {file_name} enviado para o Google Drive.")
    except Exception as e:
        logger.error(f"Erro ao fazer upload para o Google Drive: {e}")

# 7. Execute Backup
try:
    backup_supabase()  # Backup data from Supabase
    backup_local_files()  # Backup local files
    upload_to_drive()  # Upload everything to Google Drive
    logger.info("Backup concluído com sucesso!")
except Exception as e:
    logger.error(f"Erro geral no processo de backup: {e}")
