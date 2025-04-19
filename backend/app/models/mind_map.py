from pydantic import BaseModel, Field
from typing import Optional, List, Dict
from datetime import datetime

class MindMapNodeBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    content: Optional[str] = Field(None, max_length=500)
    parent_id: Optional[str] = None
    position_x: float = 0
    position_y: float = 0
    style: Optional[Dict] = None

class MindMapBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    user_id: str = Field(..., min_length=1)
    nodes: List[MindMapNodeBase] = []
    theme: Optional[str] = "default"
    is_public: bool = False
    tags: List[str] = []

class MindMapCreate(MindMapBase):
    pass

class MindMap(MindMapBase):
    id: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": "1",
                "title": "Projeto de Software",
                "description": "Mapa mental do projeto",
                "user_id": "user123",
                "nodes": [
                    {
                        "title": "Backend",
                        "content": "FastAPI + PostgreSQL",
                        "position_x": 0,
                        "position_y": 0
                    },
                    {
                        "title": "Frontend",
                        "content": "Next.js + TailwindCSS",
                        "position_x": 100,
                        "position_y": 0
                    }
                ],
                "theme": "professional",
                "is_public": True,
                "tags": ["projeto", "software"],
                "created_at": "2024-04-17T09:00:00",
                "updated_at": "2024-04-17T09:00:00"
            }
        } 