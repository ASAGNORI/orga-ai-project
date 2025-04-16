# Activate virtual environment if it exists
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Add the parent directory to PYTHONPATH
export PYTHONPATH=$PYTHONPATH:$(dirname $(pwd))

# Start the FastAPI server
echo ""
echo "🧩 Iniciando o backend com Uvicorn..."
cd backend || { echo "❌ Pasta 'backend' não encontrada!"; exit 1; }
uvicorn main:app --reload --host 0.0.0.0 --port 8000 
