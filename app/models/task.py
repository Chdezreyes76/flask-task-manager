"""
Contiene la clase Task, que representa el modelo de dominio de una tarea, 
así como los métodos para convertir entre objetos y diccionarios.
"""

class Task:
    """
    Representa una tarea del sistema.

    Atributos:
        id (int): Identificador único de la tarea.
        title (str): Título de la tarea.
        description (str): Descripción detallada de la tarea.
        priority (str): Prioridad de la tarea ('baja', 'media', 'alta', 'bloqueante').
        effort_hours (float): Horas estimadas de esfuerzo.
        status (str): Estado de la tarea ('pendiente', 'en progreso', 'en revisión', 'completada').
        assigned_to (str): Persona asignada a la tarea.
    """
    def __init__(self, id=None, title=None, description=None, priority=None, effort_hours=None, status=None, assigned_to=None):
        """
        Inicializa una nueva instancia de Task.

        Args:
            id (int): Identificador único de la tarea.
            title (str): Título de la tarea.
            description (str): Descripción detallada de la tarea.
            priority (str): Prioridad de la tarea.
            effort_hours (float): Horas estimadas de esfuerzo.
            status (str): Estado de la tarea.
            assigned_to (str): Persona asignada a la tarea.
        """
        self.id = id
        self.title = title
        self.description = description
        self.priority = priority
        self.effort_hours = effort_hours
        self.status = status
        self.assigned_to = assigned_to

    def to_dict(self):
        """
        Convierte la tarea a un diccionario.

        Returns:
            dict: Representación de la tarea como diccionario.
        """
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
        """
        Crea una instancia de Task a partir de un diccionario.

        Args:
            data (dict): Diccionario con los datos de la tarea.
        Returns:
            Task: Instancia de la clase Task.
        """
        return cls(
            id=data.get("id"),
            title=data.get("title"),
            description=data.get("description"),
            priority=data.get("priority"),
            effort_hours=data.get("effort_hours"),
            status=data.get("status"),
            assigned_to=data.get("assigned_to")
        )
