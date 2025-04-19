# Nome dos serviços
BACKEND_NAME=backend
FRONTEND_NAME=frontend
SUPABASE_NAME=supabase
N8N_NAME=n8n
OLLAMA_NAME=ollama

# Sobe tudo (docker-compose)
up:
	docker compose up --build

# Sobe os containers em segundo plano
up-bg:
	docker compose up -d

# Para os containers
down:
	docker compose down

# Executa o backup
backup:
	python ./scripts/backup.py

# Logs dos containers
logs:
	docker compose logs -f
