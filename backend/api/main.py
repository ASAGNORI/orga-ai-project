# backend/api/main.py
from backend.api.routes import reminder

app.include_router(reminder.router, prefix="/api")
