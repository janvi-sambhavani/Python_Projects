from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI(title="Task Management API")

# ------------------------
# Data Models
# ------------------------n
class Task(BaseModel):
    id: int
    title: str
    owner: str
    status: str  # new, active, completed
    is_deleted: bool = False


class TaskCreate(BaseModel):
    title: str
    owner: str
    status: str = "new"


# ------------------------
# Sample Data
# ------------------------
tasks: List[Task] = [
    Task(id=1, title="Task 1", owner="janvi", status="new"),
    Task(id=2, title="Task 2", owner="janvi", status="active"),
    Task(id=3, title="Task 3", owner="janvi", status="completed"),
    Task(id=4, title="Task 4", owner="john", status="new"),
]


# ------------------------
# Root Route
# ------------------------
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI Task API"}


# ------------------------
# Dashboard
# ------------------------
@app.get("/dashboard")
def dashboard(username: str):
    user_tasks = [t for t in tasks if t.owner == username and not t.is_deleted]
    return {
        "total": len(user_tasks),
        "new": sum(1 for t in user_tasks if t.status == "new"),
        "active": sum(1 for t in user_tasks if t.status == "active"),
        "completed": sum(1 for t in user_tasks if t.status == "completed"),
    }


# ------------------------
# CRUD Operations
# ------------------------

# Get all tasks
@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return [t for t in tasks if not t.is_deleted]


# Get single task by ID
@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    for t in tasks:
        if t.id == task_id and not t.is_deleted:
            return t
    raise HTTPException(status_code=404, detail="Task not found")


# Create new task
@app.post("/tasks", response_model=Task)
def create_task(task: TaskCreate):
    new_id = max([t.id for t in tasks], default=0) + 1
    new_task = Task(id=new_id, **task.dict())
    tasks.append(new_task)
    return new_task


# Update task
@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: TaskCreate):
    for i, t in enumerate(tasks):
        if t.id == task_id and not t.is_deleted:
            tasks[i] = Task(id=task_id, **updated_task.dict())
            return tasks[i]
    raise HTTPException(status_code=404, detail="Task not found")


# Delete task (soft delete)
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for t in tasks:
        if t.id == task_id and not t.is_deleted:
            t.is_deleted = True
            return {"message": f"Task {task_id} deleted"}
    raise HTTPException(status_code=404, detail="Task not found")

