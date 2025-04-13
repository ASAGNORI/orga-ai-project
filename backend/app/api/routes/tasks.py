from fastapi import APIRouter, HTTPException
from typing import List
from ...models.task import Task, TaskCreate
from ...core.database import supabase

router = APIRouter()

@router.post("/", response_model=Task)
async def create_task(task: TaskCreate):
    try:
        result = supabase.table("tasks").insert(task.dict()).execute()
        return result.data[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/", response_model=List[Task])
async def get_tasks(user_id: str):
    try:
        result = supabase.table("tasks").select("*").eq("user_id", user_id).execute()
        return result.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/{task_id}", response_model=Task)
async def update_task(task_id: str, task: TaskCreate):
    try:
        result = supabase.table("tasks").update(task.dict()).eq("id", task_id).execute()
        return result.data[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{task_id}")
async def delete_task(task_id: str):
    try:
        supabase.table("tasks").delete().eq("id", task_id).execute()
        return {"message": "Task deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 