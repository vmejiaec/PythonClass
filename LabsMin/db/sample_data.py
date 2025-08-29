"""
Script para agregar tareas de ejemplo a la base de datos
Ejecutar una sola vez para poblar la aplicación con datos de prueba
"""

from db.database import DatabaseManager
from datetime import datetime, timedelta

def add_sample_tasks():
    """Agrega tareas de ejemplo a la base de datos"""
    db = DatabaseManager()
    
    # Calcular fechas futuras
    today = datetime.now().date()
    future_dates = [
        (today + timedelta(days=3)).strftime("%Y-%m-%d"),
        (today + timedelta(days=7)).strftime("%Y-%m-%d"),
        (today + timedelta(days=14)).strftime("%Y-%m-%d"),
        (today + timedelta(days=30)).strftime("%Y-%m-%d"),
        (today + timedelta(days=-2)).strftime("%Y-%m-%d"),  # Tarea vencida
    ]
    
    # Tareas de ejemplo
    sample_tasks = [
        ("Estudiar Python y Tkinter", future_dates[0], 75),
        ("Desarrollar aplicación web", future_dates[1], 30),
        ("Preparar presentación final", future_dates[2], 10),
        ("Documentar proyecto", future_dates[3], 0),
        ("Entregar reporte mensual", future_dates[4], 90),  # Vencida
        ("Revisar código del equipo", future_dates[1], 60),
        ("Configurar servidor de producción", future_dates[2], 25),
        ("Actualizar documentación técnica", None, 50),  # Sin fecha límite
    ]
    
    print("Agregando tareas de ejemplo...")
    for name, due_date, progress in sample_tasks:
        db.add_task(name, due_date, progress)
        print(f"✅ Agregada: {name}")
    
    print(f"\n🎉 Se agregaron {len(sample_tasks)} tareas de ejemplo exitosamente!")
    print("Ahora puedes ejecutar 'python main.py' para ver las tareas en la aplicación.")

if __name__ == "__main__":
    add_sample_tasks()
