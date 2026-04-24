from fastapi import FastAPI
from database import create_tables
from routers import tasks

app = FastAPI(
    title="Task Manager API",
    description="A REST API for managing tasks built with FastAPI and PostgreSQL",
    version="1.0.0"
)

create_tables()
app.include_router(tasks.router)

@app.get("/")
def root():
    return {"message": "Task Manager API is running!"}