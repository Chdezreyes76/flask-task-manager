"""
Repositorio para la persistencia de tareas en un archivo JSON.
"""
import json
import os
from app.models.task import Task
from app.repositories.i_task_repository import ITaskRepository

class JsonTaskRepository(ITaskRepository):
    """
    Repositorio para la persistencia de tareas en un archivo JSON.
    """
    def __init__(self, filepath):
        self.filepath = filepath
        if not os.path.exists(self.filepath):
            with open(self.filepath, 'w', encoding='utf-8') as f:
                json.dump([], f)

    def load_tasks(self):
        with open(self.filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return [Task.from_dict(item) for item in data]

    def save_tasks(self, tasks):
        with open(self.filepath, 'w', encoding='utf-8') as f:
            json.dump([task.to_dict() for task in tasks], f, ensure_ascii=False, indent=2)
