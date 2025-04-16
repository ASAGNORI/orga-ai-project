from fastapi import APIRouter

router = APIRouter()

@router.get("/tasks")
async def get_tasks():
    return {"tasks": ["task 1", "task 2"]}
