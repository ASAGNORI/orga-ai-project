from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uuid
import datetime
import os
import psycopg2
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Libera CORS para o frontend local
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ajuste para seu domínio em produção
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Banco de dados Supabase (Postgres)
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://usuario:senha@localhost:5432/seubanco")

# Modelos
class Task(BaseModel):
    id: Optional[str]
    user_id: str
    title: str
    description: Optional[str] = ""
    due_date: Optional[str] = None
    completed: bool = False

class Goal(BaseModel):
    id: Optional[str]
    user_id: str
    title: str
    deadline: Optional[str] = None
    progress: Optional[int] = 0

class User(BaseModel):
    id: Optional[str]
    name: str
    email: str

# Conexão com DB
def get_connection():
    return psycopg2.connect(DATABASE_URL)

@app.get("/")
def read_root():
    return {"msg": "API Viva 🎉"}

@app.post("/tasks")
def create_task(task: Task):
    conn = get_connection()
    cursor = conn.cursor()
    task_id = str(uuid.uuid4())
    cursor.execute(
        "INSERT INTO tasks (id, user_id, title, description, due_date, completed) VALUES (%s, %s, %s, %s, %s, %s)",
        (task_id, task.user_id, task.title, task.description, task.due_date, task.completed)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return {"id": task_id, "msg": "Tarefa criada com sucesso"}

@app.get("/tasks/{user_id}")
def list_tasks(user_id: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks WHERE user_id = %s", (user_id,))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

# Você pode continuar com endpoints de `goals` e `users` com base nesse padrão