from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# TODO: els vostres test venen aqui

def test_update_task_success():
    nueva_tarea = {"title": "Tarea original", "description": "Descripción original"}
    response = client.post("/tasks", json=nueva_tarea)
    assert response.status_code == 200
    tarea_creada = response.json()
    task_id = tarea_creada["id"]

    datos_actualizados = {
        "title": "Tarea modificada",
        "description": "Descripción modificada",
        "completed": True
    }

    response = client.put(f"/tasks/{task_id}", json=datos_actualizados)
    assert response.status_code == 200
    tarea_actualizada = response.json()
    assert tarea_actualizada["title"] == "Tarea modificada"
    assert tarea_actualizada["description"] == "Descripción modificada"
    assert tarea_actualizada["completed"] is True


def test_delete_task_success():
    nueva_tarea = {"title": "Tarea a eliminar", "description": "Descripción"}
    response = client.post("/tasks", json=nueva_tarea)
    assert response.status_code == 200
    tarea_creada = response.json()
    task_id = tarea_creada["id"]

    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 200
    mensaje = response.json()
    assert mensaje["message"] == "Tasca eliminada"
