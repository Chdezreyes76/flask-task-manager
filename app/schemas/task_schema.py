"""
Define el esquema de validación TaskSchema usando Pydantic para validar los datos de las tareas.
"""

from pydantic import BaseModel, Field, field_validator
from typing import Literal


class TaskSchema(BaseModel):
    """
    Esquema de validación para una tarea usando Pydantic.
    """

    id: int = Field(..., description="Identificador único de la tarea")
    title: str = Field(..., min_length=1, max_length=100, description="Título de la tarea")
    description: str = Field(..., min_length=1, description="Descripción de la tarea")
    priority: Literal['baja', 'media', 'alta', 'bloqueante'] = Field(..., description="Prioridad de la tarea")
    effort_hours: float = Field(..., gt=0, description="Horas estimadas de esfuerzo")
    status: Literal['pendiente', 'en progreso', 'en revisión', 'completada'] = Field(..., description="Estado de la tarea")
    assigned_to: str = Field(..., min_length=1, description="Persona asignada a la tarea")

    @field_validator('title', 'description', 'assigned_to')
    @classmethod
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('El campo no puede estar vacío')
        return v
