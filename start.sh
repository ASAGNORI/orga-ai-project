# Restart complete project
# Para rodar via terminal: chmod +x start.sh
# Para rodar via terminal: ./start.sh

#!/bin/bash

# Ativa erro fatal se algo falhar
set -e

# Defaults
CHECK_OLLAMA=true
START_SUPABASE=true
START_BACKEND=true
START_FRONTEND=true

# Parse de argumentos
for arg in "$@"
do
  case $arg in
    --no-check)
      CHECK_OLLAMA=false
      shift
      ;;
    --frontend-only)
      START_BACKEND=false
      START_SUPABASE=false
      CHECK_OLLAMA=false
      shift
      ;;
    --backend-only)
      START_FRONTEND=false
      shift
      ;;
    --no-supabase)
      START_SUPABASE=false
      shift
      ;;
    --help)
      echo ""
      echo "✨ Script de inicialização do Orga AI"
      echo ""
      echo "Opções:"
      echo "  --no-check         Ignora checagem do Ollama"
      echo "  --frontend-only    Inicia apenas o frontend"
      echo "  --backend-only     Inicia apenas o backend e supabase"
      echo "  --no-supabase      Pula reinício do Supabase"
      echo ""
      exit 0
      ;;
  esac
done

echo ""
echo "🚀 Iniciando o projeto Orga AI..."
echo "=================================="

# 1. Checagem do Ollama
if [ "$CHECK_OLLAMA" = true ]; then
  echo ""
  echo "🧠 Verificando status do Ollama..."
  if ollama list >/dev/null 2>&1; then
      echo "✅ Ollama está rodando!"
  else
      echo "❌ Ollama não está rodando. Por favor, inicie com: ollama serve"
      exit 1
  fi
fi

# 2. Restart Supabase
if [ "$START_SUPABASE" = true ]; then
  echo ""
  echo "🗃️ Reiniciando Supabase local..."
  supabase stop && supabase start
fi

# 3. Iniciar Backend
if [ "$START_BACKEND" = true ]; then
  echo ""
  echo "🧩 Iniciando o backend..."
  if [ -d "backend" ]; then
      cd backend
      echo "📂 Diretório backend encontrado. Rodando Uvicorn..."
      uvicorn main:app --reload &
      cd ..
  else
      echo "❌ Diretório 'backend' não encontrado!"
      exit 1
  fi
fi

# 4. Iniciar Frontend
if [ "$START_FRONTEND" = true ]; then
  echo ""
  echo "🖥️ Iniciando o frontend..."
  if [ -d "frontend" ]; then
      cd frontend
      echo "📂 Diretório frontend encontrado. Rodando npm run dev..."
      npm run dev
  else
      echo "❌ Diretório 'frontend' não encontrado!"
      exit 1
  fi
fi

echo ""
echo "✅ Projeto Orga AI rodando! Vai com tudo! 💥"