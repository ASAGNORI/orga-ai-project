#!/bin/bash

# Ativar o ambiente virtual
source venv/bin/activate

# Instalar dependências se necessário
pip install -r requirements.txt

# Iniciar o servidor
cd app
uvicorn main:app --reload --host 0.0.0.0 --port 8000 