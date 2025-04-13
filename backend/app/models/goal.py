from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class GoalBase(BaseModel):
    meta: str
    progresso: int = 0
    prazo: Optional[datetime] = None
    user_id: str

class GoalCreate(GoalBase):
    pass

class Goal(GoalBase):
    id: str
    created_at: datetime

    class Config:
        from_attributes = True 