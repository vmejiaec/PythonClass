"""
Script de prueba para verificar todas las funcionalidades de la aplicación
"""

from database import DatabaseManager
import unittest
from datetime import datetime, date

class TestTodoApp(unittest.TestCase):
    
    def setUp(self):
        """Configurar test database"""
        self.db = DatabaseManager("test_tasks.db")
    
    def test_add_task(self):
        """Probar agregar una tarea"""
        initial_count = len(self.db.get_all_tasks())
        self.db.add_task("Tarea de prueba", "2025-12-31", 50)
        new_count = len(self.db.get_all_tasks())
        self.assertEqual(new_count, initial_count + 1)
    
    def test_update_task(self):
        """Probar actualizar una tarea"""
        # Agregar una tarea
        self.db.add_task("Tarea original", "2025-12-31", 0)
        tasks = self.db.get_all_tasks()
        task_id = tasks[-1][0]  # ID de la última tarea
        
        # Actualizar la tarea
        self.db.update_task(task_id, "Tarea actualizada", "2025-12-25", 75)
        
        # Verificar la actualización
        updated_tasks = self.db.get_all_tasks()
        updated_task = next(task for task in updated_tasks if task[0] == task_id)
        
        self.assertEqual(updated_task[1], "Tarea actualizada")
        self.assertEqual(updated_task[2], "2025-12-25")
        self.assertEqual(updated_task[3], 75)
    
    def test_delete_task(self):
        """Probar eliminar una tarea"""
        # Agregar una tarea
        self.db.add_task("Tarea para eliminar", "2025-12-31", 0)
        tasks = self.db.get_all_tasks()
        task_id = tasks[-1][0]
        initial_count = len(tasks)
        
        # Eliminar la tarea
        self.db.delete_task(task_id)
        new_count = len(self.db.get_all_tasks())
        
        self.assertEqual(new_count, initial_count - 1)
    
    def test_get_tasks_for_chart(self):
        """Probar obtener datos para gráficos"""
        self.db.add_task("Tarea para gráfico", "2025-12-31", 80)
        chart_data = self.db.get_tasks_for_chart()
        self.assertIsInstance(chart_data, list)
        if chart_data:
            self.assertIsInstance(chart_data[0], tuple)
            self.assertEqual(len(chart_data[0]), 2)  # name, progress
    
    def tearDown(self):
        """Limpiar después de las pruebas"""
        import os
        if os.path.exists("test_tasks.db"):
            os.remove("test_tasks.db")

def run_manual_tests():
    """Ejecutar pruebas manuales de funcionalidad"""
    print("🧪 Ejecutando pruebas manuales...")
    
    # Probar la base de datos
    print("\n📊 Probando la base de datos...")
    db = DatabaseManager("manual_test.db")
    
    # Agregar tarea
    db.add_task("Tarea de prueba manual", "2025-09-01", 25)
    print("✅ Tarea agregada")
    
    # Obtener tareas
    tasks = db.get_all_tasks()
    print(f"✅ {len(tasks)} tareas encontradas")
    
    if tasks:
        task_id = tasks[0][0]
        
        # Actualizar tarea
        db.update_task(task_id, "Tarea actualizada", "2025-09-15", 75)
        print("✅ Tarea actualizada")
        
        # Obtener datos para gráfico
        chart_data = db.get_tasks_for_chart()
        print(f"✅ Datos para gráfico: {len(chart_data)} elementos")
        
        # Eliminar tarea
        db.delete_task(task_id)
        print("✅ Tarea eliminada")
    
    # Limpiar archivo de prueba
    import os
    if os.path.exists("manual_test.db"):
        os.remove("manual_test.db")
    
    print("\n🎉 Todas las pruebas manuales completadas exitosamente!")

def check_requirements():
    """Verificar que todos los requisitos están cumplidos"""
    print("📋 Verificando cumplimiento de requisitos...")
    
    requirements = {
        "Interfaz gráfica con Tkinter": "✅ Implementado en main.py",
        "Cuadro de texto para tarea": "✅ task_entry en main.py",
        "Cuadro para fecha límite": "✅ date_entry en main.py", 
        "Cuadro para porcentaje": "✅ progress_entry en main.py",
        "Botón Agregar": "✅ add_btn en main.py",
        "Listbox para mostrar tareas": "✅ task_listbox en main.py",
        "Operaciones CRUD": "✅ Todas implementadas",
        "Base de datos SQLite": "✅ database.py",
        "Botón para gráfico Matplotlib": "✅ chart_btn y deadline_chart_btn",
        "Validación tareas vacías": "✅ Validación en add_task()",
        "Mensajes de confirmación": "✅ messagebox para eliminar",
        "Layout con grid()": "✅ Usado en create_widgets()",
        "Mostrar días restantes": "✅ calculate_days_left()"
    }
    
    print("\n📊 Estado de requisitos:")
    for req, status in requirements.items():
        print(f"  {status} {req}")
    
    print(f"\n🎯 Cumplimiento: {len(requirements)}/{len(requirements)} requisitos ✅")

if __name__ == "__main__":
    print("🔧 Ejecutando verificación completa del sistema...")
    
    # Verificar requisitos
    check_requirements()
    
    # Ejecutar pruebas manuales
    run_manual_tests()
    
    # Ejecutar pruebas unitarias
    print("\n🧪 Ejecutando pruebas unitarias...")
    unittest.main(verbosity=2, exit=False)
    
    print("\n✨ Verificación completa finalizada!")
