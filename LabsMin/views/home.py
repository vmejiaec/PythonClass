import tkinter as tk

class Home:
    def __init__(self):
        self.nombre = "Pantalla principal"
        self.root = tk.Tk()
        self.root.title("Gestor de Tareas")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")
        
        # Variable para almacenar el ID de la tarea seleccionada
        self.selected_task_id = None
        self.delete_confirmation_pending = False

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
                                bg="#27ae60", fg="white", 
                                font=("Arial", 10, "bold"),
                                width=12)
        self.add_btn.pack(side=tk.LEFT, padx=5)
        
        self.update_btn = tk.Button(button_frame, text="✏️ Actualizar", 
                                   bg="#3498db", fg="white", 
                                   font=("Arial", 10, "bold"),
                                   width=12)
        self.update_btn.pack(side=tk.LEFT, padx=5)
        
        self.delete_btn = tk.Button(button_frame, text="🗑️ Eliminar",                                    
                                   bg="#e74c3c", fg="white", 
                                   font=("Arial", 10, "bold"),
                                   width=12)
        self.delete_btn.pack(side=tk.LEFT, padx=5)
        
        self.chart_btn = tk.Button(button_frame, text="📊 Gráfico Progreso", 
                                  
                                  bg="#9b59b6", fg="white", 
                                  font=("Arial", 10, "bold"),
                                  width=15)
        self.chart_btn.pack(side=tk.LEFT, padx=5)
        
        self.deadline_chart_btn = tk.Button(button_frame, text="📅 Gráfico Fechas", 
                                           
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