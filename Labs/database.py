import sqlite3
from datetime import datetime

class DatabaseManager:
    def __init__(self, db_name="tasks.db"):
        self.db_name = db_name
        self.init_database()
    
    def init_database(self):
        """Inicializa la base de datos y crea la tabla de tareas si no existe"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                due_date DATE,
                progress INTEGER DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def add_task(self, name, due_date, progress=0):
        """Agrega una nueva tarea a la base de datos"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO tasks (name, due_date, progress)
            VALUES (?, ?, ?)
        ''', (name, due_date, progress))
        
        conn.commit()
        conn.close()
    
    def get_all_tasks(self):
        """Obtiene todas las tareas de la base de datos"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM tasks ORDER BY due_date')
        tasks = cursor.fetchall()
        
        conn.close()
        return tasks
    
    def update_task(self, task_id, name, due_date, progress):
        """Actualiza una tarea existente"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute('''
            UPDATE tasks
            SET name = ?, due_date = ?, progress = ?
            WHERE id = ?
        ''', (name, due_date, progress, task_id))
        
        conn.commit()
        conn.close()
    
    def delete_task(self, task_id):
        """Elimina una tarea de la base de datos"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
        
        conn.commit()
        conn.close()
    
    def get_tasks_for_chart(self):
        """Obtiene datos para generar gráficos"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute('SELECT name, progress FROM tasks')
        tasks = cursor.fetchall()
        
        conn.close()
        return tasks
