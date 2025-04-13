from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TaskBase(BaseModel):
    titulo: str
    descricao: Optional[str] = None
    status: str = "pending"
    prioridade: Optional[str] = None
    data: Optional[datetime] = None
    user_id: str

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: str
    created_at: datetime

    class Config:
        from_attributes = True 