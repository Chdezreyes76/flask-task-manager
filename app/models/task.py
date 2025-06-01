"""
Contiene la clase Task, que representa el modelo de dominio de una tarea, 
así como los métodos para convertir entre objetos y diccionarios.
"""

class Task:
    """
    Modelo de dominio para una tarea.
    """
    def __init__(self, id, title, description, priority, effort_hours, status, assigned_to):
        self.id = id
        self.title = title
        self.description = description
        self.priority = priority
        self.effort_hours = effort_hours
        self.status = status
        self.assigned_to = assigned_to

    def to_dict(self):
        """Convierte la tarea a un diccionario."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "effort_hours": self.effort_hours,
            "status": self.status,
            "assigned_to": self.assigned_to
        }

    @classmethod
    def from_dict(cls, data):
        """Crea una instancia de Task a partir de un diccionario."""
        return cls(
            id=data.get("id"),
            title=data.get("title"),
            description=data.get("description"),
            priority=data.get("priority"),
            effort_hours=data.get("effort_hours"),
            status=data.get("status"),
            assigned_to=data.get("assigned_to")
        )
