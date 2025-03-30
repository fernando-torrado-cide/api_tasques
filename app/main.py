from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import Base, engine, get_db
from app.crud import get_tasks, create_tasks, update_tasks, delete_tasks
from app.schemas import TaskCreate, TaskUpdate, TaskResponse

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Crear instancia de la aplicación
app = FastAPI()

# GET → Obtener todas las tareas
@app.get("/tasks", response_model=list[TaskResponse])
def read_tasks(db: Session = Depends(get_db)):
    return get_tasks(db)

# POST → Crear una nueva tarea
@app.post("/tasks", response_model=TaskResponse)
def add_task(task: TaskCreate, db: Session = Depends(get_db)):
    return create_tasks(db, task)

# PUT → Actualizar una tarea existente
@app.put("/tasks/{task_id}", response_model=TaskResponse)
def modify_task(task_id: int, task_update: TaskUpdate, db: Session = Depends(get_db)):
    updated_task = update_tasks(db, task_id, task_update)
    if not updated_task:
        raise HTTPException(status_code=404, detail="Tasca no trobada")
    return updated_task

# DELETE → Eliminar una tarea
@app.delete("/tasks/{task_id}")
def remove_task(task_id: int, db: Session = Depends(get_db)):
    deleted_task = delete_tasks(db, task_id)
    if not deleted_task:
        raise HTTPException(status_code=404, detail="Tasca no trobada")
    return {"message": "Tasca eliminada"}

