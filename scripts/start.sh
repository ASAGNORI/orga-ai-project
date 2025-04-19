#!/bin/bash

# Ativa erro fatal se algo falhar
set -e

# Defaults
CHECK_OLLAMA=true
START_SUPABASE=true
START_BACKEND=true
START_FRONTEND=true
USE_DOCKER=true

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
    --no-docker)
      USE_DOCKER=false
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
      echo "  --no-docker        Roda os serviços fora do Docker"
      echo ""
      exit 0
      ;;
  esac
done

echo ""
echo "🚀 Iniciando o projeto Orga AI (modo Docker)..."
echo "==============================================="

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

# 1.5. Detectar se GPU está disponível e gerar override se necessário
GPU_AVAILABLE=false

if command -v nvidia-smi &> /dev/null; then
  if nvidia-smi -L | grep -q "GPU"; then
    GPU_AVAILABLE=true
    echo "💪 GPU disponível! Vamos usar runtime: nvidia com Docker."

    cat > docker/docker-compose.override.yml <<EOL
services:
  ollama:
    environment:
      - NVIDIA_VISIBLE_DEVICES=all
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: all
              capabilities: [gpu]
EOL

  else
    echo "⚠️ nvidia-smi está disponível, mas nenhuma GPU foi detectada."
  fi
else
  echo "🧊 Sem suporte a nvidia-smi. Rodando em CPU mesmo."
fi

# 2. Supabase
if [ "$START_SUPABASE" = true ]; then
  echo ""
  echo "🗃️ Supabase é gerenciado via Docker. Nenhuma ação do CLI necessária aqui."
fi

# 3. Iniciar serviços com Docker Compose
if [ "$USE_DOCKER" = true ]; then
  echo ""
  echo "📦 Iniciando todos os serviços (Docker)..."

  if [ -f docker/docker-compose.override.yml ]; then
    docker compose -f docker/docker-compose.yaml -f docker/docker-compose.override.yml -p orga_ai_project up -d --build
  else
    docker compose -f docker/docker-compose.yaml -p orga_ai_project up -d --build
  fi
else
  echo ""
  echo "⚙️ Modo sem Docker ainda não implementado neste script."
fi

echo ""
echo "✅ Projeto Orga AI rodando! Voa, foguete! 🚀🔥"
