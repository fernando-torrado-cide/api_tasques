from sqlalchemy.orm import Session
from models import Task
from schemas import TaskCreate, TaskUpdate




# Actualitzar una tasca
@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.get_json()
    with sqlite3.connect("tasks.db") as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE tasks SET title = ?, description = ?, done = ? WHERE id = ?",
                               (data["title"], data.get("description", ""), data["done"], task_id))
        conn.commit()
    return jsonify({"message": "Task updated"})


# Eliminar una tasca
@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    with sqlite3.connect("tasks.db") as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
    return jsonify({"message": "Task deleted"})
