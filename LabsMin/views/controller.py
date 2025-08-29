import datetime
import tkinter as tk

from db import DatabaseManager
from reps import ChartGenerator

class Controller:
    def __init__(self, view):
        self.nombre = "Controlador del Home"
        self.view = view
        # Configuración
        self.view.add_btn.config(command=self.add_task)
        self.view.update_btn.config(command=self.update_task)
        self.view.delete_btn.config(command=self.delete_task)
        self.view.chart_btn.config(command=self.show_progress_chart)
        self.view.deadline_chart_btn.config(command=self.show_deadline_chart)
        # Bind para selección en listbox
        self.view.task_listbox.bind('<<ListboxSelect>>', self.on_task_select)        
        # Bind para Enter en el campo de entrada
        self.view.task_entry.bind('<Return>', lambda e: self.add_task())
        # Inicializar base de datos
        self.db = DatabaseManager()
        # Inicializar reportes
        self.chart_generator = ChartGenerator(self.db)

    def calculate_days_left(self, due_date_str):
        """Calcula los días restantes para una fecha límite"""
        if not due_date_str:
            return "Sin fecha"
        
        try:
            due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
            today = datetime.date.today()
            days_left = (due_date - today).days
            
            if days_left < 0:
                return f"Vencida ({abs(days_left)} días)"
            elif days_left == 0:
                return "Vence hoy"
            else:
                return f"{days_left} días"
        except:
            return "Fecha inválida"
    
    def format_task_display(self, task):
        """Formatea una tarea para mostrar en el listbox"""
        task_id, name, due_date, progress, created_at = task
        days_left = self.calculate_days_left(due_date)
        
        # Formatear el texto con ancho fijo
        name_display = name[:30] + "..." if len(name) > 30 else name
        progress_display = f"{progress}%"
        
        return f"{task_id:3d} | {name_display:<33} | {progress_display:>4} | {days_left}"
    

    def load_tasks(self):
        """Carga todas las tareas en el listbox"""
        self.view.task_listbox.delete(0, tk.END)
        tasks = self.db.get_all_tasks()
        
        if tasks:
            # Agregar encabezado
            header = "ID  | Nombre                            | Prog | Días restantes"
            separator = "-" * len(header)
            self.view.task_listbox.insert(tk.END, header)
            self.view.task_listbox.insert(tk.END, separator)
            
            for task in tasks:
                display_text = self.format_task_display(task)
                self.view.task_listbox.insert(tk.END, display_text)
        else:
            self.view.task_listbox.insert(tk.END, "No hay tareas registradas")
    
    def show_notification(self, message, notification_type="success"):
        """Muestra una notificación en la parte inferior de la ventana"""
        # Colores según el tipo de notificación
        colors = {
            "success": "#2ecc71",    # Verde para éxito
            "error": "#e74c3c",      # Rojo para errores
            "warning": "#f39c12",    # Naranja para advertencias
            "info": "#3498db"        # Azul para información
        }
        
        # Configurar el mensaje y color
        self.notification_label.config(text=message, bg=colors.get(notification_type, "#2ecc71"))
        self.notification_frame.grid()  # Mostrar el frame
        
        # Auto-ocultar después de 3 segundos
        self.root.after(3000, self.hide_notification)
    
    def hide_notification(self):
        """Oculta la notificación"""
        self.notification_frame.grid_remove()
    
    def add_task(self):
        """Agrega una nueva tarea"""
        name = self.task_entry.get().strip()
        due_date = self.date_entry.get().strip()
        progress = self.progress_var.get().strip()
        
        # Validaciones
        if not name:
            self.show_notification("❌ El nombre de la tarea no puede estar vacío", "error")
            return
        
        if due_date:
            try:
                datetime.strptime(due_date, "%Y-%m-%d")
            except ValueError:
                self.show_notification("❌ Formato de fecha inválido. Use YYYY-MM-DD", "error")
                return
        
        try:
            progress_val = int(progress) if progress else 0
            if not (0 <= progress_val <= 100):
                self.show_notification("❌ El progreso debe estar entre 0 y 100", "error")
                return
        except ValueError:
            self.show_notification("❌ El progreso debe ser un número entero", "error")
            return
        
        # Agregar tarea a la base de datos
        self.db.add_task(name, due_date if due_date else None, progress_val)
        
        # Limpiar campos
        self.task_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
        self.progress_var.set("0")
        
        # Recargar lista
        self.load_tasks()
        self.show_notification("✅ Tarea agregada correctamente", "success")
    
    def on_task_select(self, event):
        """Maneja la selección de una tarea en el listbox"""
        selection = self.view.task_listbox.curselection()
        if selection:
            index = selection[0]
            # Saltar encabezado y separador
            if index >= 2:
                task_text = self.view.task_listbox.get(index)
                try:
                    # Extraer ID de la tarea
                    task_id = int(task_text.split("|")[0].strip())
                    self.selected_task_id = task_id
                    
                    # Cargar datos en los campos
                    tasks = self.db.get_all_tasks()
                    for task in tasks:
                        if task[0] == task_id:
                            self.task_entry.delete(0, tk.END)
                            self.task_entry.insert(0, task[1])
                            
                            self.date_entry.delete(0, tk.END)
                            if task[2]:
                                self.date_entry.insert(0, task[2])
                            
                            self.progress_var.set(str(task[3]))
                            break
                except:
                    self.selected_task_id = None
        else:
            # Si no hay selección, cancelar confirmación de eliminación pendiente
            self.delete_confirmation_pending = False
    
    def update_task(self):
        """Actualiza la tarea seleccionada"""
        if not self.selected_task_id:
            self.show_notification("⚠️ Seleccione una tarea para actualizar", "warning")
            return
        
        name = self.task_entry.get().strip()
        due_date = self.date_entry.get().strip()
        progress = self.progress_var.get().strip()
        
        # Validaciones
        if not name:
            self.show_notification("❌ El nombre de la tarea no puede estar vacío", "error")
            return
        
        if due_date:
            try:
                datetime.strptime(due_date, "%Y-%m-%d")
            except ValueError:
                self.show_notification("❌ Formato de fecha inválido. Use YYYY-MM-DD", "error")
                return
        
        try:
            progress_val = int(progress) if progress else 0
            if not (0 <= progress_val <= 100):
                self.show_notification("❌ El progreso debe estar entre 0 y 100", "error")
                return
        except ValueError:
            self.show_notification("❌ El progreso debe ser un número entero", "error")
            return
        
        # Actualizar en la base de datos
        self.db.update_task(self.selected_task_id, name, 
                           due_date if due_date else None, progress_val)
        
        # Limpiar campos
        self.task_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
        self.progress_var.set("0")
        self.selected_task_id = None
        
        # Recargar lista
        self.load_tasks()
        self.show_notification("✅ Tarea actualizada correctamente", "success")
    
    def delete_task(self):
        """Elimina la tarea seleccionada"""
        if not self.selected_task_id:
            self.show_notification("⚠️ Seleccione una tarea para eliminar", "warning")
            return
        
        # Sistema de doble clic para confirmar eliminación
        if not self.delete_confirmation_pending:
            self.delete_confirmation_pending = True
            self.show_notification("⚠️ Haga clic en 'Eliminar' nuevamente para confirmar", "warning")
            # Auto-cancelar la confirmación después de 5 segundos
            self.root.after(5000, self.cancel_delete_confirmation)
            return
        
        # Proceder con la eliminación
        self.db.delete_task(self.selected_task_id)
        
        # Limpiar campos
        self.task_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
        self.progress_var.set("0")
        self.selected_task_id = None
        self.delete_confirmation_pending = False
        
        # Recargar lista
        self.load_tasks()
        self.show_notification("✅ Tarea eliminada correctamente", "success")
    
    def cancel_delete_confirmation(self):
        """Cancela la confirmación de eliminación pendiente"""
        self.delete_confirmation_pending = False
    
    def show_progress_chart(self):
        """Muestra el gráfico de progreso"""
        self.chart_generator.show_progress_chart(self.root)
    
    def show_deadline_chart(self):
        """Muestra el gráfico de fechas límite"""
        self.chart_generator.show_deadline_chart(self.root)
