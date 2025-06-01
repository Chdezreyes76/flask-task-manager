"""
Implementa la clase TaskManager, responsable de la lógica de negocio y la gestión de tareas,
incluyendo la persistencia en archivo JSON.
"""
import os
from app.models.task import Task
from app.repositories.i_task_repository import ITaskRepository
from app.repositories.json_task_repository import JsonTaskRepository

class TaskManager:
    """
    Servicio para la gestión de tareas, desacoplado de la persistencia.
    """
    def __init__(self, repository: ITaskRepository = None):
        if repository is None:
            data_path = os.path.join(os.path.dirname(__file__), '../data/tasks.json')
            repository = JsonTaskRepository(os.path.abspath(data_path))
        self.repository = repository

    def get_all(self):
        return self.repository.load_tasks()

    def get_by_id(self, task_id):
        tasks = self.repository.load_tasks()
        for task in tasks:
            if task.id == task_id:
                return task
        return None

    def create(self, task):
        tasks = self.repository.load_tasks()
        tasks.append(task)
        self.repository.save_tasks(tasks)
        return task

    def update(self, task_id, updated_task):
        tasks = self.repository.load_tasks()
        for idx, task in enumerate(tasks):
            if task.id == task_id:
                tasks[idx] = updated_task
                self.repository.save_tasks(tasks)
                return updated_task
        return None

    def delete(self, task_id):
        tasks = self.repository.load_tasks()
        new_tasks = [task for task in tasks if task.id != task_id]
        if len(new_tasks) == len(tasks):
            return False
        self.repository.save_tasks(new_tasks)
        return True
