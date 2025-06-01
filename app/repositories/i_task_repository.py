"""
Interfaz para los repositorios de tareas. Permite desacoplar la lógica de negocio de la persistencia.
"""
from abc import ABC, abstractmethod
from typing import List
from app.models.task import Task

class ITaskRepository(ABC):
    @abstractmethod
    def load_tasks(self) -> List[Task]:
        pass

    @abstractmethod
    def save_tasks(self, tasks: List[Task]):
        pass
