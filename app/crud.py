from sqlalchemy.orm import Session
from app.models import Task
from app.schemas import TaskCreate, TaskUpdate

def get_tasks(db: Session):
    """
    Fetch all tasks from the database.
    """
    return db.query(Task).all()

def create_tasks(db: Session, task: TaskCreate):
    """
    Create a new task in the database.
    """
    new_task = Task(**task.dict())  # Convert TaskCreate Pydantic model to a Task model.
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

def update_tasks(db: Session, task_id: int, task_update: TaskUpdate):
    """
    Update an existing task.
    """
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        for key, value in task_update.dict(exclude_unset=True).items():
            setattr(task, key, value)
        db.commit()
        db.refresh(task)
        return task
    return None

def delete_tasks(db: Session, task_id: int):
    """
    Delete a task from the database.
    """
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
        return task
    return None
