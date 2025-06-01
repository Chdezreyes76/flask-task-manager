
# 🧭 Plan de Trabajo — Proyecto Flask: Entregable 1

Este documento detalla el plan de desarrollo para una aplicación Flask para la gestión de tareas, diseñado siguiendo principios de ingeniería de software avanzada: escalabilidad, mantenibilidad, alta cohesión y bajo acoplamiento. Incluye validación con Pydantic, pruebas con pytest, y soporte escalable hacia bases de datos como MySQL.

---

## 🧩 FASE 0: Preparación del entorno y diseño base

### 🎯 Objetivo
Establecer el entorno de desarrollo, estructura modular y asegurarse de que todas las dependencias se gestionan desde `requirements.txt`.

### ✅ Tareas

- Crear entorno virtual local.
- Instalar dependencias desde el archivo `requirements.txt`:
  ```bash
  pip install -r requirements.txt
  ```
- Estructurar el proyecto:
  ```
  proyecto/
  ├── app/
  │   ├── __init__.py
  │   ├── routes.py
  │   ├── models/
  │   │   └── task.py
  │   ├── schemas/
  │   │   └── task_schema.py
  │   ├── services/
  │   │   └── task_manager.py
  │   ├── data/
  │   │   └── tasks.json
  ├── tests/
  │   └── test_tasks.py
  ├── requirements.txt
  ├── run.py
  └── README.md
  ```
- Crear repositorio Git local e inicializar con:
  ```bash
  git init
  git add .
  git commit -m "Inicialización del proyecto Flask"
  ```
- Crear repositorio en GitHub y conectar:
  ```bash
  git remote add origin https://github.com/usuario/nombre-repo.git
  git push -u origin main
  ```

---

## 🧱 FASE 1: Modelo de dominio (`Task`) y validación (`TaskSchema`)

### 🎯 Objetivo
Separar la representación de los datos (`Task`) de su validación (`TaskSchema`).

### ✅ Tareas

- `Task` (en `models/task.py`) representa una tarea, con métodos `to_dict()` y `from_dict()`.
- `TaskSchema` (en `schemas/task_schema.py`) valida atributos, usando tipos literales y validaciones semánticas.
- El modelo `Task` no debe realizar validaciones: responsabilidad delegada a Pydantic.

---

## 🛠️ FASE 2: Capa de servicios (`TaskManager`) con arquitectura desacoplada

### 🎯 Objetivo
Centralizar la lógica de negocio y manipulación de tareas de forma desacoplada.

### ✅ Tareas

- Crear `TaskManager` con métodos: `get_all`, `get_by_id`, `create`, `update`, `delete`.
- Internamente, delegar persistencia a una clase tipo repositorio (ej. `JsonTaskRepository`).
- Diseñar con visión futura para implementar `SQLTaskRepository` sin alterar la interfaz pública.

---

## 🌐 FASE 3: Rutas y controladores Flask

### 🎯 Objetivo
Exponer endpoints RESTful delegando toda la lógica al servicio.

### ✅ Tareas

- Usar `Blueprints` para definir las rutas en `routes.py`.
- Implementar:
  - `GET /tasks`
  - `GET /tasks/<id>`
  - `POST /tasks`
  - `PUT /tasks/<id>`
  - `DELETE /tasks/<id>`
- Validar entradas con `TaskSchema`.
- Manejar errores con controladores de error globales y respuestas JSON.

---

## 🧪 FASE 4: Pruebas automatizadas con `pytest`

### 🎯 Objetivo
Asegurar el correcto funcionamiento de cada funcionalidad crítica.

### ✅ Tareas

- Crear pruebas para:
  - Crear, leer, actualizar, eliminar tareas.
  - Manejo de errores (ID inexistente, entradas inválidas).
- Usar `fixtures` para preparar y limpiar entorno de pruebas.
- Diseñar las pruebas para no depender del tipo de almacenamiento.

---

## ⚙️ FASE 5: Escalabilidad y futura migración a base de datos (MySQL)

### 🎯 Objetivo
Preparar el proyecto para una futura integración con bases de datos.

### ✅ Tareas

- Definir una interfaz `ITaskRepository`.
- `TaskManager` debe interactuar solo con dicha interfaz.
- Futura implementación de `SQLTaskRepository` con SQLAlchemy.
- No cambiar las rutas ni `TaskManager` al cambiar el backend.

---

## 📚 FASE 6: Documentación técnica (`README.md` y docstrings)

### 🎯 Objetivo
Documentar el sistema para facilitar uso, colaboración y mantenimiento.

### ✅ Tareas

- `README.md` con:
  - Descripción del proyecto
  - Instalación
  - Ejecución
  - Pruebas
  - Roadmap
- Agregar docstrings a:
  - Todas las clases y métodos públicos
  - Incluyendo descripción, tipos de parámetros y retornos
  - Errores esperados si aplica

---

## 📦 FASE FINAL: Empaquetado y entrega

### ✅ Tareas

- Verificar integridad del archivo `tasks.json`.
- Confirmar que el proyecto corre sin problemas desde cero.
- Comprimir como: `m2_proyecto_nombre_apellido.zip`.
- Incluir todo excepto carpetas virtuales (`venv`) o archivos personales.


---

## ✅ FASE EXTRA: Checklist de verificación final (VSCode)

### 🎯 Objetivo
Realizar una verificación exhaustiva del proyecto antes de la entrega, garantizando que se cumplan todos los puntos solicitados en las instrucciones y rúbricas.

### ✅ Checklist funcional en VSCode

Marca cada uno como ✓ al verificarlo en el proyecto.

- [ ] El proyecto está estructurado en carpetas (`models/`, `schemas/`, `services/`, `routes/`, `tests/`, etc.).
- [ ] Se utiliza un entorno virtual activado y no está incluido en el ZIP.
- [ ] Todas las dependencias están declaradas en `requirements.txt`.
- [ ] Se incluye un archivo `README.md` claro y completo.
- [ ] Existe un archivo `run.py` como punto de entrada de la aplicación Flask.
- [ ] La clase `Task` está implementada correctamente con los atributos definidos.
- [ ] La clase `Task` incluye métodos `to_dict()` y `from_dict()`.
- [ ] Se ha creado `TaskSchema` con Pydantic y valida correctamente entradas y salidas.
- [ ] La clase `TaskManager` gestiona tareas usando un archivo JSON y sigue SRP.
- [ ] Las rutas están definidas usando Flask y son RESTful (`GET`, `POST`, `PUT`, `DELETE`).
- [ ] Las rutas no contienen lógica de negocio (solo delegan).
- [ ] Los errores están correctamente gestionados y devuelven respuestas claras en JSON.
- [ ] Se ha ejecutado `pytest` y todas las pruebas pasan correctamente.
- [ ] Se ha comprobado el funcionamiento manual de la API (crear, leer, actualizar, eliminar).
- [ ] El proyecto está conectado a un repositorio Git (local y/o GitHub).
- [ ] Se puede migrar fácilmente a una base de datos relacional (MySQL) gracias a una arquitectura desacoplada.
- [ ] Se han utilizado `docstrings` en clases y métodos públicos.
- [ ] El proyecto ha sido comprimido como `m2_proyecto_nombre_apellido.zip` sin carpetas innecesarias.

---

✅ Si todo está marcado, ¡tu proyecto está listo para entregar!
