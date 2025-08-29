# Aplicación Py-To-Do 

Crear una aplicación gráfica en Python utilizando Tkinter que permita gestionar una lista de tareas pendientes (To-Do List).

## Interfaz gráfica mínima:

- Una ventana principal con título “Gestor de Tareas”.
- Un cuadro de texto (Entry) para escribir el nombre de una tarea.
- Un cuadro para ingresar una fecha límite
- Un cuadro para ingresar un porcentaje de avance
- Un botón “Agregar” para añadir la tarea a la lista.
- Un Listbox para mostrar las tareas agregadas.

## Operaciones CRUD:

- Crear: Permitir agregar una nueva tarea desde el cuadro de texto.
- Leer: Mostrar todas las tareas en el Listbox.
- Actualizar: Seleccionar una tarea de la lista, modificar su nombre en el cuadro de texto y guardar el cambio con un botón “Actualizar”.
- Eliminar: Seleccionar una tarea de la lista y eliminarla con un botón “Eliminar”.

## Requisitos

- La base de datos en SQLite
- Incluir un botón para llamar a un gráfico con Matplotlib 
- Validar que no se agreguen tareas vacías.
- Mostrar mensajes de confirmación al eliminar tareas.
- Usar pack() o grid() para organizar bien los elementos en la ventana.
- La lista de tareas agregadas debe presentar los días que faltan para que venza la tarea

## Ejemplo de flujo de la aplicación

- El usuario escribe “Estudiar Python” en el cuadro de texto y pulsa Agregar.
- La tarea aparece en el Listbox.
- Selecciona la tarea, cambia el texto en el cuadro a “Estudiar Tkinter”, pulsa Actualizar y se refleja en la lista.
- Finalmente, selecciona la tarea y pulsa Eliminar para borrarla.


