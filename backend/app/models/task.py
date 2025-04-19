from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import datetime
from enum import Enum

class TaskStatus(str, Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class TaskPriority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class TaskBase(BaseModel):
    titulo: str = Field(..., min_length=1, max_length=100)
    descricao: Optional[str] = Field(None, max_length=500)
    status: TaskStatus = Field(default=TaskStatus.PENDING)
    prioridade: Optional[TaskPriority] = None
    data: Optional[datetime] = None
    user_id: str = Field(..., min_length=1)

    @validator('data')
    def validate_date(cls, v):
        if v and v < datetime.now():
            raise ValueError('Data não pode ser no passado')
        return v

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": "1",
                "titulo": "Exemplo de tarefa",
                "descricao": "Descrição da tarefa",
                "status": "pending",
                "prioridade": "high",
                "data": "2024-04-17T10:00:00",
                "user_id": "user123",
                "created_at": "2024-04-17T09:00:00",
                "updated_at": "2024-04-17T09:00:00"
            }
        }
