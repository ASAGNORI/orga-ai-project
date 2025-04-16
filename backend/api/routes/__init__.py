# backend/api/routes/__init__.py 
from .task import router as task_router
from .reminder import router as reminder_router
from .ollama import router as ollama_router
from .history import router as history_router