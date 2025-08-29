# Inicio del programa
print("Ingreso de tareas")
print()

# Sección de preparación de variables 
tareaNombre = "Consultar el manual de Python"
tareaPlazo = 15
tareaTiempo = 8
tareaPorcentajeEjecucion = 30
tareaAlerta = "Verde"
print()

# Sección de ingreso de datos
print("Ingreso de datos de la tarea")
tareaNombre = input(" - Nombre: ")
tareaPlazo = input(" - Plazo: ")
tareaTiempo = input(" - Timpo: ")
tareaPorcentajeEjecucion = input(" - Ejecución %: ")
tareaAlerta = input(" - Alerta : ")
print()

# Sección de presentación de datos

if len(tareaNombre) > 30:
    tareaNombre = tareaNombre[:27] + "..."

tareaPorcentajeEjecucion = tareaPorcentajeEjecucion + "%"

print("Tarea ingresada")
print ("           Tarea              |Plazo| % Ejec. | Tiempo | Alerta")
print("---------------------------------------------------------------------")
print(f"{tareaNombre:<30}|{tareaPlazo:^5}|{tareaPorcentajeEjecucion:^9}|{tareaTiempo:^8}|{tareaAlerta:^9}")

print()

