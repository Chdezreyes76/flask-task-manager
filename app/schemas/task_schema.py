"""
Define el esquema de validación TaskSchema usando Pydantic para validar los datos de las tareas.
"""

from pydantic import BaseModel, Field, field_validator
from typing import Literal, Optional


class TaskCreateSchema(BaseModel):
    """
    Esquema de validación para la creación de una tarea (sin id).

    Valida los atributos de una tarea y asegura que cumplen con los requisitos de tipo y formato.
    """

    title: str = Field(..., min_length=1, max_length=100, description="Título de la tarea")
    description: str = Field(..., min_length=1, description="Descripción de la tarea")
    priority: Literal['baja', 'media', 'alta', 'bloqueante'] = Field(..., description="Prioridad de la tarea")
    effort_hours: float = Field(..., gt=0, description="Horas estimadas de esfuerzo")
    status: Literal['pendiente', 'en progreso', 'en revisión', 'completada'] = Field(..., description="Estado de la tarea")
    assigned_to: str = Field(..., min_length=1, description="Persona asignada a la tarea")

    @field_validator('title', 'description', 'assigned_to')
    @classmethod
    def not_empty(cls, v):
        """
        Valida que los campos de texto no estén vacíos.

        Args:
            v (str): Valor del campo.
        Returns:
            str: Valor validado.
        Raises:
            ValueError: Si el campo está vacío.
        """
        if not v or not v.strip():
            raise ValueError('El campo no puede estar vacío')
        return v


class TaskSchema(TaskCreateSchema):
    """
    Esquema de validación para una tarea completa (incluye id).
    """

    id: int = Field(..., description="Identificador único de la tarea")
