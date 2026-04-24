from fastapi import APIRouter, HTTPException
from database import get_connection
from schemas import TaskCreate, TaskUpdate

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.get("/")
def get_all_tasks():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks ORDER BY created_at DESC")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    tasks = []
    for row in rows:
        tasks.append({
            "id": row[0],
            "title": row[1],
            "description": row[2],
            "status": row[3],
            "created_at": str(row[4])
        })
    return tasks

@router.get("/{task_id}")
def get_task(task_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks WHERE id = %s", (task_id,))
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    if not row:
        raise HTTPException(status_code=404, detail="Task not found")
    return {
        "id": row[0],
        "title": row[1],
        "description": row[2],
        "status": row[3],
        "created_at": str(row[4])
    }

@router.post("/", status_code=201)
def create_task(task: TaskCreate):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tasks (title, description, status) VALUES (%s, %s, %s) RETURNING *",
        (task.title, task.description, task.status)
    )
    row = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return {
        "id": row[0],
        "title": row[1],
        "description": row[2],
        "status": row[3],
        "created_at": str(row[4])
    }

@router.put("/{task_id}")
def update_task(task_id: int, task: TaskUpdate):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks WHERE id = %s", (task_id,))
    existing = cursor.fetchone()
    if not existing:
        raise HTTPException(status_code=404, detail="Task not found")
    new_title = task.title if task.title is not None else existing[1]
    new_desc = task.description if task.description is not None else existing[2]
    new_status = task.status if task.status is not None else existing[3]
    cursor.execute(
        "UPDATE tasks SET title=%s, description=%s, status=%s WHERE id=%s RETURNING *",
        (new_title, new_desc, new_status, task_id)
    )
    row = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return {
        "id": row[0],
        "title": row[1],
        "description": row[2],
        "status": row[3],
        "created_at": str(row[4])
    }

@router.delete("/{task_id}")
def delete_task(task_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks WHERE id = %s", (task_id,))
    existing = cursor.fetchone()
    if not existing:
        raise HTTPException(status_code=404, detail="Task not found")
    cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": f"Task {task_id} deleted successfully"}
    