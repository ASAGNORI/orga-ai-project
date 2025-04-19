#!/bin/bash

# Exit on error
set -e

# Defaults
START_SUPABASE=true
START_BACKEND=true
START_FRONTEND=true
USE_DOCKER=true

# Parse arguments
for arg in "$@"
do
  case $arg in
    --frontend-only)
      START_BACKEND=false
      START_SUPABASE=false
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
      echo "✨ Orga AI Project Startup Script"
      echo ""
      echo "Options:"
      echo "  --frontend-only    Start only the frontend"
      echo "  --backend-only     Start only the backend and supabase"
      echo "  --no-supabase      Skip Supabase startup"
      echo "  --no-docker        Run services without Docker"
      echo ""
      exit 0
      ;;
  esac
done

echo ""
echo "🚀 Starting Orga AI Project..."
echo "============================="

# Check for required environment variables
if [ ! -f .env ]; then
    echo "❌ .env file not found. Please create one from .env.example"
    exit 1
fi

# Check for required API keys
if [ -z "$HUGGINGFACE_API_KEY" ]; then
    echo "⚠️ HUGGINGFACE_API_KEY not set in .env"
fi

if [ -z "$HANA_HOST" ] || [ -z "$HANA_USER" ] || [ -z "$HANA_PASSWORD" ]; then
    echo "⚠️ HANA database credentials not fully configured in .env"
fi

# Start services with Docker Compose
if [ "$USE_DOCKER" = true ]; then
    echo ""
    echo "📦 Starting services with Docker Compose..."

    # Build and start services
    docker compose up -d --build

    # Check if services are running
    echo ""
    echo "🔍 Checking service status..."
    
    if docker compose ps | grep -q "frontend.*Up"; then
        echo "✅ Frontend is running at http://localhost:3000"
    fi
    
    if docker compose ps | grep -q "backend.*Up"; then
        echo "✅ Backend is running at http://localhost:8000"
    fi
    
    if docker compose ps | grep -q "supabase.*Up"; then
        echo "✅ Supabase is running at http://localhost:54321"
    fi
    
    if docker compose ps | grep -q "n8n.*Up"; then
        echo "✅ N8N is running at http://localhost:5678"
    fi
else
    echo ""
    echo "⚙️ Non-Docker mode not implemented yet"
    exit 1
fi

echo ""
echo "✅ Orga AI Project is running! 🚀"
echo ""
echo "📚 Documentation:"
echo "  - Frontend: http://localhost:3000"
echo "  - Backend API: http://localhost:8000/docs"
echo "  - Supabase Studio: http://localhost:54321"
echo "  - N8N Dashboard: http://localhost:5678"
