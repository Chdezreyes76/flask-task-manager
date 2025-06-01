
# 📘 Instrucciones del Entregable 1 — Proyecto Flask

## 🎯 Objetivos

Vamos a crear un proyecto de generación de tareas que se asignan a usuarios. En este entregable, el objetivo es comenzar con el desarrollo de la aplicación Flask con la arquitectura y la lógica de programación, que luego usaremos en los siguientes módulos. Para ello, crearás una aplicación con Flask, organizando toda la arquitectura del proyecto creando rutas que conecten con los controladores para devolver resultados asociados a través de un json.

---

## Pautas de elaboración

Crea una aplicación Flask que tenga rutas y controladores para la gestión de tareas de usuario. Los campos de tareas tendrán el siguiente interfaz:

### 📝 Estructura de la entidad Task

La entidad **Task** debe incluir los siguientes campos:

- `id`: Clave primaria (entero).
- `title`: Título de la tarea (texto corto).
- `description`: Descripción completa de la tarea (texto largo).
- `priority`: Prioridad (baja, media, alta, bloqueante).
- `effort_hours`: Número decimal, horas estimadas para completarla.
- `status`: Estado (pendiente, en progreso, en revisión, completada).
- `assigned_to`: Persona a la que se asigna la tarea (texto).

---

### 🔗 Endpoints requeridos

Implementar los siguientes endpoints:

- `POST /tasks`: Crear una nueva tarea.
- `GET /tasks`: Leer todas las tareas.
- `GET /tasks/<id>`: Leer una tarea específica.
- `PUT /tasks/<id>`: Actualizar una tarea existente.
- `DELETE /tasks/<id>`: Eliminar una tarea.

Todos los endpoints deben funcionar con formato **JSON**.

---

## 🏗️ Arquitectura y componentes

Deberás crear la arquitectura de ficheros del proyecto. Obviamente, puedes usar asistentes de generación de código por inteligencia artificial para ayudarte. Crearás el entorno virtual y la instalación de librerías, así como el fichero de requerimientos.

Crearás un fichero de rutas, donde darás de alta todas las rutas especificadas que llamarán a la clase TaskManager, que deberá gestionar el uso de tareas con el archivo json. También existirá un clase Task, que permitirá definir una tarea y convertirla en un diccionario para poder insertarla en un json.

El proyecto debe incluir:

### Clase `Task`
- Representa una tarea.
- Métodos:
  - `to_dict()`: Convierte la tarea a diccionario.
  - `from_dict()`: Crea una tarea desde un diccionario.

### Clase `TaskManager`
- Se encarga de la gestión de tareas usando un archivo `tasks.json`.
- Métodos estáticos:
  - `load_tasks()`: Carga tareas desde el archivo.
  - `save_tasks()`: Guarda tareas en el archivo.

### Flask API
 - GET/tasks --> Devuelve todas las tareas.
 - GET/tasks/<id> --> Devuelve una tarea específica.
 - POST/tasks --> Crea una nueva tarea.
 - PUT/tasks/<id> --> Actualiza una tarea existente.
 - DELETE/tasks/<id> --> Elimina una tarea.

---

## 📁 Entrega

El archivo de entrega debe ser un `.zip` con el siguiente formato de nombre:

```
m2_proyecto_nombre_apellido.zip
```

Debe contener:

- Carpeta del proyecto Flask
- Código fuente organizado
- Archivo `requirements.txt` con dependencias

---

## 📊 Rúbrica de Evaluación

| Componente              | Descripción                                                                  | Puntos | Peso |
|------------------------|-------------------------------------------------------------------------------|--------|------|
| Arquitectura del proyecto | Creación y organización del proyecto Flask                                    | 2.5    | 25%  |
| Clase Task               | Implementación de la clase Task con sus métodos                               | 2.5    | 25%  |
| Clase TaskManager        | Gestión de tareas y persistencia con archivo JSON                             | 2.5    | 25%  |
| Rutas / Endpoints        | Creación de endpoints RESTful que devuelvan datos en JSON                     | 2.5    | 25%  |

**Total: 10 puntos — 100%**

---

## ✅ Recomendaciones

- Se puede usar inteligencia artificial como asistente para generar partes del código.
- La validación, pruebas y documentación serán claves para futuras extensiones del proyecto.
