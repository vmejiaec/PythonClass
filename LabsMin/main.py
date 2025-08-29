from db import DatabaseManager
from reps import ChartGenerator
from views import Controller, Home

class TodoApp:
    def __init__(self):
        # Crear la interfaz
        self.home = Home()        
        self.home.create_widgets()       
        self.controller = Controller(self.home)
        self.controller.load_tasks()
    

def main():    
    app = TodoApp()
    app.home.root.mainloop()

if __name__ == "__main__":
    main()
