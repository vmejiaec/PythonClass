# Py-To-Do - Gestor de Tareas

Una aplicación gráfica en Python desarrollada con Tkinter para gestionar una lista de tareas pendientes (To-Do List) con base de datos SQLite y visualización de datos con Matplotlib.

## Características

✅ **Interfaz gráfica intuitiva** con Tkinter  
✅ **Base de datos SQLite** para persistencia de datos  
✅ **Operaciones CRUD completas** (Crear, Leer, Actualizar, Eliminar)  
✅ **Gestión de fechas límite** con cálculo automático de días restantes  
✅ **Control de progreso** por tarea (0-100%)  
✅ **Gráficos interactivos** con Matplotlib  
✅ **Validaciones de entrada** de datos  
✅ **Mensajes de confirmación** para operaciones críticas  

## Requisitos del Sistema

- Python 3.7 o superior
- Tkinter (incluido con Python)
- Matplotlib
- SQLite3 (incluido con Python)

## Instalación

1. Clone o descargue el proyecto
2. Instale las dependencias:
```bash
pip install matplotlib
```

## Uso

### Ejecutar la aplicación
```bash
python main.py
```

### Funcionalidades principales

#### 1. Agregar una tarea
- Escriba el nombre de la tarea en el campo "Nombre"
- Ingrese una fecha límite en formato YYYY-MM-DD (opcional)
- Establezca el porcentaje de progreso (0-100%)
- Haga clic en "➕ Agregar"

#### 2. Actualizar una tarea
- Seleccione una tarea de la lista
- Modifique los campos necesarios
- Haga clic en "✏️ Actualizar"

#### 3. Eliminar una tarea
- Seleccione una tarea de la lista
- Haga clic en "🗑️ Eliminar"
- Confirme la eliminación

#### 4. Ver gráficos
- **Gráfico de Progreso**: Muestra el progreso de todas las tareas en un gráfico de barras
- **Gráfico de Fechas**: Muestra el estado de las fechas límite en un gráfico circular

## Estructura del proyecto

```
📁 Py-To-Do/
├── 📄 main.py           # Aplicación principal con interfaz Tkinter
├── 📄 database.py       # Manejo de base de datos SQLite
├── 📄 charts.py         # Generación de gráficos con Matplotlib
├── 📄 requirements.txt  # Dependencias del proyecto
├── 📄 README.md         # Este archivo
└── 📄 tasks.db          # Base de datos SQLite (se crea automáticamente)
```

## Características técnicas

### Base de datos
- **Motor**: SQLite3
- **Tabla**: `tasks`
- **Campos**:
  - `id`: Identificador único (autoincremental)
  - `name`: Nombre de la tarea
  - `due_date`: Fecha límite
  - `progress`: Progreso (0-100%)
  - `created_at`: Fecha de creación

### Interfaz gráfica
- **Framework**: Tkinter
- **Layout**: Grid layout para organización
- **Widgets**: Entry, Listbox, Button, Label, LabelFrame
- **Validaciones**: Entrada de datos y formatos

### Visualización de datos
- **Biblioteca**: Matplotlib
- **Gráfico de barras**: Progreso por tarea
- **Gráfico circular**: Estado de fechas límite
- **Integración**: FigureCanvasTkAgg para mostrar en ventanas Tkinter

## Validaciones implementadas

- ✅ No se permiten tareas vacías
- ✅ Formato de fecha válido (YYYY-MM-DD)
- ✅ Progreso entre 0 y 100%
- ✅ Confirmación antes de eliminar tareas
- ✅ Selección de tarea requerida para actualizar/eliminar

## Cálculo de días restantes

La aplicación calcula automáticamente los días restantes para cada tarea:
- **Días positivos**: Días restantes hasta la fecha límite
- **"Vence hoy"**: Cuando la fecha límite es hoy
- **"Vencida (X días)"**: Cuando la fecha límite ya pasó
- **"Sin fecha"**: Cuando no hay fecha límite establecida

## Ejemplos de uso

### Ejemplo 1: Tarea académica
- **Nombre**: "Estudiar Python"
- **Fecha límite**: "2025-08-30"
- **Progreso**: "75%"

### Ejemplo 2: Proyecto de trabajo
- **Nombre**: "Desarrollar aplicación web"
- **Fecha límite**: "2025-09-15"
- **Progreso**: "30%"

## Troubleshooting

### Error: "No module named 'matplotlib'"
```bash
pip install matplotlib
```

### Error: Base de datos bloqueada
- Cierre completamente la aplicación
- Vuelva a ejecutar `python main.py`

### Problemas con fechas
- Use siempre el formato YYYY-MM-DD
- Ejemplo válido: 2025-12-31
- Ejemplo inválido: 31/12/2025

## Desarrollo futuro

Posibles mejoras:
- 🔄 Recordatorios automáticos
- 📧 Notificaciones por email
- 🏷️ Categorías de tareas
- 📱 Versión mobile
- 🌐 Sincronización en la nube
- 📋 Importar/exportar tareas

## Licencia

Este proyecto está desarrollado con fines educativos.

---
**Desarrollado con ❤️ usando Python, Tkinter, SQLite y Matplotlib**
