#!/bin/bash

# Activate virtual environment if it exists
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Add the parent directory to PYTHONPATH
export PYTHONPATH=$PYTHONPATH:$(dirname $(pwd))

# Start the FastAPI server
uvicorn main:app --reload --host 0.0.0.0 --port 8000 