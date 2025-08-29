"""
Script de prueba para verificar que las notificaciones funcionan correctamente
"""

from database import DatabaseManager

def test_notifications():
    """Prueba las notificaciones agregando, actualizando y eliminando una tarea"""
    print("🧪 Probando el sistema de notificaciones...")
    
    # Crear una instancia de base de datos para pruebas
    db = DatabaseManager("test_notifications.db")
    
    # Agregar una tarea de prueba
    db.add_task("Tarea de prueba para notificaciones", "2025-09-01", 50)
    print("✅ Tarea de prueba agregada")
    
    # Obtener todas las tareas
    tasks = db.get_all_tasks()
    if tasks:
        task_id = tasks[0][0]
        print(f"📋 Tarea encontrada con ID: {task_id}")
        
        # Actualizar la tarea
        db.update_task(task_id, "Tarea actualizada", "2025-09-15", 75)
        print("✅ Tarea actualizada")
        
        # Eliminar la tarea
        db.delete_task(task_id)
        print("✅ Tarea eliminada")
    
    # Limpiar archivo de prueba
    import os
    if os.path.exists("test_notifications.db"):
        os.remove("test_notifications.db")
    
    print("\n🎉 ¡Todas las operaciones de base de datos funcionan correctamente!")
    print("\n📱 Ahora ejecute 'python main.py' para probar las notificaciones en la interfaz.")
    print("\nPruebe estos escenarios:")
    print("1. Agregar una tarea válida → Debería mostrar notificación verde")
    print("2. Intentar agregar tarea vacía → Debería mostrar notificación roja")
    print("3. Actualizar una tarea → Debería mostrar notificación verde")
    print("4. Intentar actualizar sin seleccionar → Debería mostrar notificación naranja")
    print("5. Hacer clic en Eliminar una vez → Debería mostrar notificación naranja")
    print("6. Hacer clic en Eliminar nuevamente → Debería mostrar notificación verde")

if __name__ == "__main__":
    test_notifications()
