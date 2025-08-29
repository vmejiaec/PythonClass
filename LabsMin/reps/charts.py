import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import Toplevel

class ChartGenerator:
    def __init__(self, database_manager):
        self.db = database_manager
    
    def show_progress_chart(self, parent_window):
        """Muestra un gráfico de barras con el progreso de las tareas"""
        tasks_data = self.db.get_tasks_for_chart()
        
        if not tasks_data:
            # Crear ventana temporal para mostrar mensaje
            temp_window = Toplevel(parent_window)
            temp_window.title("Sin Datos")
            temp_window.geometry("400x200")
            temp_window.configure(bg="#f39c12")
            
            # Mensaje centrado
            message_label = tk.Label(temp_window, 
                                   text="📊 No hay tareas para mostrar en el gráfico\n\nAgregue algunas tareas primero", 
                                   font=("Arial", 14, "bold"),
                                   bg="#f39c12", fg="white",
                                   justify=tk.CENTER)
            message_label.pack(expand=True)
            
            # Auto-cerrar después de 3 segundos
            temp_window.after(3000, temp_window.destroy)
            return
        
        # Crear nueva ventana para el gráfico
        chart_window = Toplevel(parent_window)
        chart_window.title("Progreso de Tareas")
        chart_window.geometry("800x600")
        
        # Preparar datos
        task_names = [task[0][:20] + "..." if len(task[0]) > 20 else task[0] for task in tasks_data]
        progress_values = [task[1] for task in tasks_data]
        
        # Crear figura de matplotlib
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Crear gráfico de barras
        bars = ax.bar(range(len(task_names)), progress_values, 
                     color=['green' if p == 100 else 'orange' if p >= 50 else 'red' for p in progress_values])
        
        # Configurar el gráfico
        ax.set_xlabel('Tareas')
        ax.set_ylabel('Progreso (%)')
        ax.set_title('Progreso de Tareas Pendientes')
        ax.set_xticks(range(len(task_names)))
        ax.set_xticklabels(task_names, rotation=45, ha='right')
        ax.set_ylim(0, 100)
        
        # Agregar valores en las barras
        for i, bar in enumerate(bars):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + 1,
                   f'{height}%', ha='center', va='bottom')
        
        plt.tight_layout()
        
        # Integrar matplotlib con Tkinter
        canvas = FigureCanvasTkAgg(fig, chart_window)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # Botón para cerrar
        close_btn = tk.Button(chart_window, text="Cerrar", 
                             command=chart_window.destroy,
                             bg="#ff6b6b", fg="white", font=("Arial", 12))
        close_btn.pack(pady=10)
    
    def show_deadline_chart(self, parent_window):
        """Muestra un gráfico circular con el estado de las fechas límite"""
        tasks_data = self.db.get_all_tasks()
        
        if not tasks_data:
            # Crear ventana temporal para mostrar mensaje
            temp_window = Toplevel(parent_window)
            temp_window.title("Sin Datos")
            temp_window.geometry("400x200")
            temp_window.configure(bg="#f39c12")
            
            # Mensaje centrado
            message_label = tk.Label(temp_window, 
                                   text="📅 No hay tareas para mostrar en el gráfico\n\nAgregue algunas tareas primero", 
                                   font=("Arial", 14, "bold"),
                                   bg="#f39c12", fg="white",
                                   justify=tk.CENTER)
            message_label.pack(expand=True)
            
            # Auto-cerrar después de 3 segundos
            temp_window.after(3000, temp_window.destroy)
            return
        
        from datetime import datetime, date
        
        # Categorizar tareas por estado de fecha límite
        today = date.today()
        overdue = 0
        due_soon = 0  # Próximos 7 días
        on_time = 0
        
        for task in tasks_data:
            if task[2]:  # Si tiene fecha límite
                try:
                    due_date = datetime.strptime(task[2], "%Y-%m-%d").date()
                    days_left = (due_date - today).days
                    
                    if days_left < 0:
                        overdue += 1
                    elif days_left <= 7:
                        due_soon += 1
                    else:
                        on_time += 1
                except:
                    on_time += 1
            else:
                on_time += 1
        
        # Crear nueva ventana para el gráfico
        chart_window = Toplevel(parent_window)
        chart_window.title("Estado de Fechas Límite")
        chart_window.geometry("800x600")
        
        # Crear figura de matplotlib
        fig, ax = plt.subplots(figsize=(8, 6))
        
        # Datos para el gráfico circular
        labels = ['Vencidas', 'Próximas (≤7 días)', 'A tiempo']
        sizes = [overdue, due_soon, on_time]
        colors = ['#ff6b6b', '#ffd93d', '#6bcf7f']
        
        # Filtrar categorías con valor 0
        filtered_data = [(label, size, color) for label, size, color in zip(labels, sizes, colors) if size > 0]
        
        if filtered_data:
            labels, sizes, colors = zip(*filtered_data)
            
            # Crear gráfico circular
            wedges, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%',
                                             startangle=90, textprops={'fontsize': 10})
            
            ax.set_title('Estado de Fechas Límite de Tareas', fontsize=14, fontweight='bold')
        else:
            ax.text(0.5, 0.5, 'No hay datos para mostrar', 
                   horizontalalignment='center', verticalalignment='center',
                   transform=ax.transAxes, fontsize=16)
        
        # Integrar matplotlib con Tkinter
        canvas = FigureCanvasTkAgg(fig, chart_window)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # Botón para cerrar
        close_btn = tk.Button(chart_window, text="Cerrar", 
                             command=chart_window.destroy,
                             bg="#ff6b6b", fg="white", font=("Arial", 12))
        close_btn.pack(pady=10)
