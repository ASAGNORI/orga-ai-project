#!/bin/bash

# Exit on error
set -e

echo ""
echo "🚀 Setting up Orga AI Project development environment..."
echo "====================================================="

# Check for required tools
echo ""
echo "🔍 Checking required tools..."

# Check for Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.11 or higher."
    exit 1
else
    PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
    echo "✅ Python $PYTHON_VERSION is installed"
fi

# Check for Node.js
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed. Please install Node.js 18 or higher."
    exit 1
else
    NODE_VERSION=$(node --version | cut -d'v' -f2)
    echo "✅ Node.js $NODE_VERSION is installed"
fi

# Check for Docker
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker."
    exit 1
else
    DOCKER_VERSION=$(docker --version | cut -d' ' -f3 | cut -d',' -f1)
    echo "✅ Docker $DOCKER_VERSION is installed"
fi

# Check for Docker Compose
if ! command -v docker compose &> /dev/null; then
    echo "❌ Docker Compose is not installed. Please install Docker Compose."
    exit 1
else
    COMPOSE_VERSION=$(docker compose version --short)
    echo "✅ Docker Compose $COMPOSE_VERSION is installed"
fi

# Check for Ollama
if ! command -v ollama &> /dev/null; then
    echo "❌ Ollama is not installed. Please install Ollama."
    exit 1
else
    echo "✅ Ollama is installed"
    
    # Check if llama3 model is available
    if ollama list | grep -q "llama3"; then
        echo "✅ llama3 model is available"
    else
        echo "⚠️ llama3 model is not available. You can pull it with: ollama pull llama3"
    fi
fi

# Create Python virtual environment
echo ""
echo "🐍 Setting up Python virtual environment..."

# Check if venv exists
if [ ! -d ".venv" ]; then
    echo "Creating Python virtual environment..."
    python3 -m venv .venv
    echo "✅ Virtual environment created"
else
    echo "✅ Virtual environment already exists"
fi

# Activate virtual environment
echo "Activating virtual environment..."
source .venv/bin/activate

# Install Python dependencies
echo ""
echo "📦 Installing Python dependencies..."
pip install --upgrade pip
pip install -r backend/requirements.txt

# Install Node.js dependencies
echo ""
echo "📦 Installing Node.js dependencies..."
cd frontend
npm install
cd ..

# Create .env file if it doesn't exist
echo ""
echo "🔑 Setting up environment variables..."
if [ ! -f ".env" ]; then
    echo "Creating .env file from example..."
    cp .env.example .env
    echo "✅ .env file created. Please update it with your credentials."
else
    echo "✅ .env file already exists"
fi

# Make scripts executable
echo ""
echo "🔧 Making scripts executable..."
chmod +x scripts/start.sh
chmod +x scripts/setup.sh

echo ""
echo "✅ Setup complete! You can now start the project with:"
echo "  ./scripts/start.sh"
echo ""
echo "📚 Documentation:"
echo "  - Frontend: http://localhost:3000"
echo "  - Backend API: http://localhost:8000/docs"
echo "  - Supabase Studio: http://localhost:54321"
echo "  - N8N Dashboard: http://localhost:5678" 