from fastapi import APIRouter, HTTPException, Depends
from typing import List
from ...models.task import Task, TaskCreate, TaskStatus
from ...core.database import get_supabase
import logging

logger = logging.getLogger(__name__)
router = APIRouter()

@router.post("/", response_model=Task)
async def create_task(task: TaskCreate):
    try:
        # Validate task status
        if task.status not in TaskStatus:
            raise HTTPException(status_code=400, detail="Invalid task status")
            
        supabase = get_supabase()
        result = supabase.table("tasks").insert(task.dict()).execute()
        if not result.data:
            raise HTTPException(status_code=500, detail="Failed to create task")
        return result.data[0]
    except Exception as e:
        logger.error(f"Error creating task: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/", response_model=List[Task])
async def get_tasks(user_id: str):
    try:
        supabase = get_supabase()
        result = supabase.table("tasks").select("*").eq("user_id", user_id).execute()
        if not result.data:
            return []
        return result.data
    except Exception as e:
        logger.error(f"Error fetching tasks: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/{task_id}", response_model=Task)
async def update_task(task_id: str, task: TaskCreate):
    try:
        # Validate task status
        if task.status not in TaskStatus:
            raise HTTPException(status_code=400, detail="Invalid task status")
            
        supabase = get_supabase()
        result = supabase.table("tasks").update(task.dict()).eq("id", task_id).execute()
        if not result.data:
            raise HTTPException(status_code=404, detail="Task not found")
        return result.data[0]
    except Exception as e:
        logger.error(f"Error updating task: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{task_id}")
async def delete_task(task_id: str):
    try:
        supabase = get_supabase()
        result = supabase.table("tasks").delete().eq("id", task_id).execute()
        if not result.data:
            raise HTTPException(status_code=404, detail="Task not found")
        return {"message": "Task deleted successfully"}
    except Exception as e:
        logger.error(f"Error deleting task: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e)) 