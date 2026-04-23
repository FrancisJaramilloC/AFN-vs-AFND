# Simulador AFD vs AFND

Este proyecto es un simulador web interactivo para comparar Autómatas Finitos Deterministas (AFD) y No Deterministas (AFND).

## Requisitos Previos
- Python 3.8+ instalado en tu sistema.
- Git (para el control de versiones).

## Instrucciones de Instalación y Ejecución

Sigue estos pasos en la terminal (PowerShell o CMD) desde la carpeta raíz del proyecto (`AFN-vs-AFND`):

### 1. Activar el Entorno Virtual
Primero debes activar el entorno virtual que contiene las dependencias aisladas.
```bash
# En Windows (PowerShell):
.\.venv\Scripts\Activate.ps1

# En CMD:
.\.venv\Scripts\activate.bat
```
*(Deberías ver `(.venv)` al inicio de tu línea de comandos indicando que está activo).*

### 2. Instalar Dependencias (Solo la primera vez)
Con el entorno activado, asegúrate de que todas las librerías estén instaladas:
```bash
pip install -r backend\requirements.txt
```

### 3. Ejecutar el Servidor Backend (FastAPI)
Una vez instaladas las dependencias y con el entorno virtual activo, ejecuta el servidor usando `uvicorn`:
```bash
uvicorn backend.main:app --reload
```
*Si todo sale bien, verás un mensaje diciendo `Application startup complete` y el servidor estará corriendo en `http://127.0.0.1:8000`.*

### 4. Abrir el Frontend
El frontend es completamente "Vanilla" (HTML/CSS/JS puro), por lo que **no necesitas un servidor de Node.js**.
Simplemente abre el archivo `frontend/index.html` haciendo doble clic sobre él en tu explorador de archivos, o ábrelo en tu navegador favorito.
- Otra opción si usas VS Code es usar la extensión **Live Server** dando clic derecho en `index.html` -> "Open with Live Server".

---

## Estructura del Proyecto

- `backend/`: Lógica en Python (FastAPI).
  - `core/automata.py`: Contiene el motor y las definiciones lógicas de los autómatas de cada ejercicio.
  - `api/routes.py`: Endpoints que el frontend consume.
- `frontend/`: Interfaz de usuario.
  - `index.html`: La vista principal.
  - `assets/`: Donde se guardan las imágenes exportadas de JFLAP.
  - `js/main.js`: Lógica visual para renderizar las evaluaciones.

## Metodología de Trabajo (Git Flow)
1. Antes de iniciar un nuevo ejercicio, asegúrate de estar en `develop`: `git checkout develop`
2. Crea una nueva rama para tu ejercicio: `git checkout -b feature/ejercicio-X`
3. Al terminar, súbela y realiza un Pull Request hacia `develop`.