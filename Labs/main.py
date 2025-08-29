import tkinter as tk
from tkinter import ttk
from datetime import datetime, date
from database import DatabaseManager
from charts import ChartGenerator

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")
        
        # Inicializar base de datos
        self.db = DatabaseManager()
        self.chart_generator = ChartGenerator(self.db)
        
        # Variable para almacenar el ID de la tarea seleccionada
        self.selected_task_id = None
        self.delete_confirmation_pending = False
        
        # Crear la interfaz
        self.create_widgets()
        self.load_tasks()
    
    def create_widgets(self):
        """Crea todos los widgets de la interfaz"""
        
        # Frame principal
        main_frame = tk.Frame(self.root, bg="#f0f0f0")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Título
        title_label = tk.Label(main_frame, text="📝 Gestor de Tareas", 
                              font=("Arial", 20, "bold"), 
                              bg="#f0f0f0", fg="#2c3e50")
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # Frame para entrada de datos
        input_frame = tk.LabelFrame(main_frame, text="Nueva Tarea", 
                                   font=("Arial", 12, "bold"),
                                   bg="#f0f0f0", fg="#34495e")
        input_frame.grid(row=1, column=0, columnspan=3, sticky="ew", pady=(0, 10))
        input_frame.columnconfigure(1, weight=1)
        
        # Nombre de la tarea
        tk.Label(input_frame, text="Nombre:", font=("Arial", 10), 
                bg="#f0f0f0").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.task_entry = tk.Entry(input_frame, font=("Arial", 10), width=40)
        self.task_entry.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
        
        # Fecha límite
        tk.Label(input_frame, text="Fecha límite (YYYY-MM-DD):", font=("Arial", 10), 
                bg="#f0f0f0").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.date_entry = tk.Entry(input_frame, font=("Arial", 10), width=40)
        self.date_entry.grid(row=1, column=1, sticky="ew", padx=5, pady=5)
        
        # Progreso
        tk.Label(input_frame, text="Progreso (%):", font=("Arial", 10), 
                bg="#f0f0f0").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.progress_var = tk.StringVar(value="0")
        self.progress_entry = tk.Entry(input_frame, textvariable=self.progress_var, 
                                      font=("Arial", 10), width=40)
        self.progress_entry.grid(row=2, column=1, sticky="ew", padx=5, pady=5)
        
        # Frame para botones de acción
        button_frame = tk.Frame(main_frame, bg="#f0f0f0")
        button_frame.grid(row=2, column=0, columnspan=3, pady=10)
        
        # Botones
        self.add_btn = tk.Button(button_frame, text="➕ Agregar", 
                                command=self.add_task,
                                bg="#27ae60", fg="white", 
                                font=("Arial", 10, "bold"),
                                width=12)
        self.add_btn.pack(side=tk.LEFT, padx=5)
        
        self.update_btn = tk.Button(button_frame, text="✏️ Actualizar", 
                                   command=self.update_task,
                                   bg="#3498db", fg="white", 
                                   font=("Arial", 10, "bold"),
                                   width=12)
        self.update_btn.pack(side=tk.LEFT, padx=5)
        
        self.delete_btn = tk.Button(button_frame, text="🗑️ Eliminar", 
                                   command=self.delete_task,
                                   bg="#e74c3c", fg="white", 
                                   font=("Arial", 10, "bold"),
                                   width=12)
        self.delete_btn.pack(side=tk.LEFT, padx=5)
        
        self.chart_btn = tk.Button(button_frame, text="📊 Gráfico Progreso", 
                                  command=self.show_progress_chart,
                                  bg="#9b59b6", fg="white", 
                                  font=("Arial", 10, "bold"),
                                  width=15)
        self.chart_btn.pack(side=tk.LEFT, padx=5)
        
        self.deadline_chart_btn = tk.Button(button_frame, text="📅 Gráfico Fechas", 
                                           command=self.show_deadline_chart,
                                           bg="#f39c12", fg="white", 
                                           font=("Arial", 10, "bold"),
                                           width=15)
        self.deadline_chart_btn.pack(side=tk.LEFT, padx=5)
        
        # Frame para la lista de tareas
        list_frame = tk.LabelFrame(main_frame, text="Lista de Tareas", 
                                  font=("Arial", 12, "bold"),
                                  bg="#f0f0f0", fg="#34495e")
        list_frame.grid(row=3, column=0, columnspan=3, sticky="nsew", pady=(10, 0))
        
        # Configurar expansión
        main_frame.rowconfigure(3, weight=1)
        main_frame.columnconfigure(0, weight=1)
        list_frame.rowconfigure(0, weight=1)
        list_frame.columnconfigure(0, weight=1)
        
        # Listbox con scrollbar
        listbox_frame = tk.Frame(list_frame, bg="#f0f0f0")
        listbox_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        listbox_frame.rowconfigure(0, weight=1)
        listbox_frame.columnconfigure(0, weight=1)
        
        self.task_listbox = tk.Listbox(listbox_frame, font=("Courier", 10),
                                      selectmode=tk.SINGLE, height=15)
        self.task_listbox.grid(row=0, column=0, sticky="nsew")
        
        # Scrollbar para el listbox
        scrollbar = tk.Scrollbar(listbox_frame, orient="vertical")
        scrollbar.grid(row=0, column=1, sticky="ns")
        
        self.task_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.task_listbox.yview)
        
        # Bind para selección en listbox
        self.task_listbox.bind('<<ListboxSelect>>', self.on_task_select)
        
        # Bind para Enter en el campo de entrada
        self.task_entry.bind('<Return>', lambda e: self.add_task())
        
        # Frame para notificaciones en la parte inferior
        self.notification_frame = tk.Frame(main_frame, bg="#f0f0f0", height=40)
        self.notification_frame.grid(row=4, column=0, columnspan=3, sticky="ew", pady=(10, 0))
        self.notification_frame.grid_remove()  # Ocultar inicialmente
        
        self.notification_label = tk.Label(self.notification_frame, 
                                          text="", 
                                          font=("Arial", 11, "bold"),
                                          fg="white",
                                          bg="#2ecc71",
                                          pady=8)
        self.notification_label.pack(fill=tk.X, padx=5, pady=5)
        
        # Frame para notificaciones en la parte inferior
        self.notification_frame = tk.Frame(main_frame, bg="#f0f0f0", height=40)
        self.notification_frame.grid(row=4, column=0, columnspan=3, sticky="ew", pady=(10, 0))
        self.notification_frame.grid_remove()  # Ocultar inicialmente
        
        self.notification_label = tk.Label(self.notification_frame, 
                                          text="", 
                                          font=("Arial", 11, "bold"),
                                          fg="white",
                                          bg="#2ecc71",
                                          pady=8)
        self.notification_label.pack(fill=tk.X, padx=5, pady=5)
    
    def calculate_days_left(self, due_date_str):
        """Calcula los días restantes para una fecha límite"""
        if not due_date_str:
            return "Sin fecha"
        
        try:
            due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
            today = date.today()
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
        self.task_listbox.delete(0, tk.END)
        tasks = self.db.get_all_tasks()
        
        if tasks:
            # Agregar encabezado
            header = "ID  | Nombre                            | Prog | Días restantes"
            separator = "-" * len(header)
            self.task_listbox.insert(tk.END, header)
            self.task_listbox.insert(tk.END, separator)
            
            for task in tasks:
                display_text = self.format_task_display(task)
                self.task_listbox.insert(tk.END, display_text)
        else:
            self.task_listbox.insert(tk.END, "No hay tareas registradas")
    
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
        selection = self.task_listbox.curselection()
        if selection:
            index = selection[0]
            # Saltar encabezado y separador
            if index >= 2:
                task_text = self.task_listbox.get(index)
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

def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
