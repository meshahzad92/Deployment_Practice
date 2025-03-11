from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Task Model
class Task(BaseModel):
    id: int
    title: str
    description: str
    completed: bool = False

# Fake Database (temporary, we'll replace this with PostgreSQL later)
tasks_db = []

# Create a new task
@app.post("/tasks/", response_model=Task)
def create_task(task: Task):
    tasks_db.append(task)
    return task

# Get all tasks
@app.get("/tasks/", response_model=List[Task])
def get_tasks():
    return tasks_db

# Get a single task by ID
@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    for task in tasks_db:
        if task.id == task_id:
            return task
    return {"error": "Task not found"}

# Update a task
@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: Task):
    for index, task in enumerate(tasks_db):
        if task.id == task_id:
            tasks_db[index] = updated_task
            return updated_task
    return {"error": "Task not found"}

# Delete a task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    global tasks_db
    tasks_db = [task for task in tasks_db if task.id != task_id]
    return {"message": "Task deleted"}
