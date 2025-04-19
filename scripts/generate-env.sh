#!/bin/bash

# === Gera chaves seguras ===
JWT_SECRET=$(openssl rand -base64 32)
SUPABASE_ANON_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.$(openssl rand -base64 32 | tr -dc 'a-zA-Z0-9' | head -c 64)"
SUPABASE_SERVICE_ROLE_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.$(openssl rand -base64 32 | tr -dc 'a-zA-Z0-9' | head -c 64)"

# === Caminhos ===
BACKEND_ENV=./backend/.env
FRONTEND_ENV=./frontend/.env

echo "🛠️  Gerando arquivos .env para backend e frontend..."

# === Cria o .env do backend ===
cat > $BACKEND_ENV <<EOF
# === FastAPI ===
APP_NAME=OrgaAI Backend
APP_HOST=0.0.0.0
APP_PORT=8000
DEBUG=False

# === Supabase Local === 
SUPABASE_URL=http://localhost:54321
SUPABASE_ANON_KEY=$SUPABASE_ANON_KEY
SUPABASE_SERVICE_ROLE_KEY=$SUPABASE_SERVICE_ROLE_KEY
SUPABASE_DB_URL=postgresql://postgres:postgres@localhost:54321/postgres
DATABASE_CONNECTION_URI=postgresql://postgres:postgres@localhost:54321/postgres

# === Ollama ===
OLLAMA_API_URL=http://localhost:11434/api/generate

# === CORS e Hosts Permitidos ===
ALLOWED_HOSTS=["localhost","127.0.0.1","host.docker.internal"]
CORS_ORIGINS=["http://localhost:3000","http://127.0.0.1:3000"]

# === Segurança / Autenticação ===
JWT_SECRET=$JWT_SECRET
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60

# === E-mail (fake placeholder) ===
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=angelo.sagnori@gmail.com
SMTP_PASSWORD=senha_app_fake

# === N8N ===
N8N_API_KEY=chave_fake
N8N_URL=http://n8n:5678/
EOF

# === Cria o .env do frontend ===
cat > $FRONTEND_ENV <<EOF
# === FastAPI ===
APP_NAME=OrgaAI Frontend
APP_HOST=0.0.0.0
APP_PORT=3000
DEBUG=True

# === Supabase ===
SUPABASE_URL=http://host.docker.internal:54321
SUPABASE_KEY=$SUPABASE_ANON_KEY
SUPABASE_JWT_SECRET=$JWT_SECRET

# === Database ===
DATABASE_URL=postgresql://postgres:postgres@host.docker.internal:5432/postgres

# === CORS ===
CORS_ORIGINS=http://localhost:3000,http://frontend:3000

# === Var ===
REACT_APP_API_URL=http://localhost:8000
REACT_APP_GOOGLE_CLIENT_ID=your-google-client-id.apps.googleusercontent.com
REACT_APP_OAUTH_SECRET=your-google-client-secret

NEXT_PUBLIC_API_URL=http://backend:8000
NEXT_PUBLIC_SUPABASE_URL=http://supabase:54321
NEXT_PUBLIC_SUPABASE_ANON_KEY=$SUPABASE_ANON_KEY
EOF

echo "✅ Arquivos .env atualizados com sucesso!"
