# ==========================================
# TUPLAS EN PYTHON - DATOS INMUTABLES
# ==========================================

# ¿QUÉ SON LAS TUPLAS?
# Las tuplas son colecciones ordenadas de elementos que NO SE PUEDEN MODIFICAR
# después de ser creadas. Esto las hace "inmutables".

print("=== ¿QUÉ SON LAS TUPLAS? ===")
print("Una tupla es una colección ordenada e INMUTABLE de elementos")
print("Se definen con paréntesis () y elementos separados por comas")
print()

# 1. CREACIÓN DE TUPLAS
print("=== 1. CREACIÓN DE TUPLAS ===")
# Tupla vacía
tupla_vacia = ()
print("Tupla vacía:", tupla_vacia)

# Tupla con elementos
coordenadas = (10, 20)
print("Coordenadas:", coordenadas)

# Tupla con un solo elemento (IMPORTANTE: necesita coma)
tupla_un_elemento = (42,)  # Sin la coma sería solo un paréntesis
print("Tupla con un elemento:", tupla_un_elemento)

# Sin paréntesis (también válido)
colores = "rojo", "verde", "azul"
print("Tupla sin paréntesis:", colores)

# Tupla mixta
persona = ("Juan", 25, True, 1.75)
print("Persona (mixta):", persona)

# Tupla anidada
matriz = ((1, 2), (3, 4), (5, 6))
print("Tupla anidada:", matriz)

# 2. ACCESO A ELEMENTOS
print("\n=== 2. ACCESO A ELEMENTOS ===")
frutas = ("manzana", "banana", "naranja", "uva")
print("Tupla de frutas:", frutas)
print("Primera fruta:", frutas[0])
print("Última fruta:", frutas[-1])
print("Segunda y tercera:", frutas[1:3])

# 3. ¿POR QUÉ SON INMUTABLES?
print("\n=== 3. ¿POR QUÉ SON INMUTABLES? ===")
numeros = (1, 2, 3, 4, 5)
print("Tupla original:", numeros)

print("\n¡INTENTEMOS MODIFICAR UNA TUPLA!")
try:
    numeros[0] = 100  # Esto causará un error
except TypeError as e:
    print(f"ERROR: {e}")
    print("No se puede modificar una tupla porque es INMUTABLE")

try:
    numeros.append(6)  # Esto también causará error
except AttributeError as e:
    print(f"ERROR: {e}")
    print("Las tuplas no tienen métodos para agregar elementos")

# 4. VENTAJAS DE LA INMUTABILIDAD
print("\n=== 4. VENTAJAS DE LA INMUTABILIDAD ===")
print("✓ SEGURIDAD: No se pueden modificar accidentalmente")
print("✓ RENDIMIENTO: Son más rápidas que las listas")
print("✓ HASH: Pueden ser claves en diccionarios")
print("✓ INTEGRIDAD: Garantizan que los datos no cambien")

# Ejemplo: Coordenadas que no deben cambiar
posicion_inicial = (0, 0)
print(f"Posición inicial: {posicion_inicial}")
print("Esta posición está protegida contra cambios accidentales")

# 5. OPERACIONES PERMITIDAS CON TUPLAS
print("\n=== 5. OPERACIONES PERMITIDAS ===")
dias_semana = ("lunes", "martes", "miércoles", "jueves", "viernes")

# Longitud
print("Número de días:", len(dias_semana))

# Verificar si existe un elemento
print("'lunes' está en la tupla:", "lunes" in dias_semana)
print("'sábado' está en la tupla:", "sábado" in dias_semana)

# Buscar índice
print("Índice de 'miércoles':", dias_semana.index("miércoles"))

# Contar ocurrencias
numeros_repetidos = (1, 2, 3, 2, 4, 2, 5)
print("La tupla:", numeros_repetidos)
print("Veces que aparece el 2:", numeros_repetidos.count(2))

# 6. DESEMPAQUETADO DE TUPLAS
print("\n=== 6. DESEMPAQUETADO DE TUPLAS ===")
punto = (10, 20)
x, y = punto  # Desempaquetado
print(f"Coordenada x: {x}, y: {y}")

# Desempaquetado con múltiples variables
empleado = ("Ana", "Desarrolladora", 30, 50000)
nombre, puesto, edad, salario = empleado
print(f"Empleado: {nombre}, {puesto}, {edad} años, ${salario}")

# Desempaquetado parcial con *
numeros = (1, 2, 3, 4, 5, 6)
primero, segundo, *resto = numeros
print(f"Primero: {primero}, Segundo: {segundo}, Resto: {resto}")

# 7. TUPLAS vs LISTAS - COMPARACIÓN
print("\n=== 7. TUPLAS vs LISTAS ===")
print("TUPLAS                    |  LISTAS")
print("--------------------------|---------------------------")
print("Inmutables (no cambian)   |  Mutables (se pueden cambiar)")
print("Paréntesis ()             |  Corchetes []")
print("Más rápidas               |  Más lentas")
print("Pueden ser claves dict    |  No pueden ser claves")
print("Menos métodos             |  Muchos métodos disponibles")

# Demostración de velocidad (conceptual)
import time
lista_grande = list(range(1000000))
tupla_grande = tuple(range(1000000))

# Acceso por índice - tuplas son más rápidas
start = time.time()
elemento = tupla_grande[500000]
tiempo_tupla = time.time() - start

start = time.time()
elemento = lista_grande[500000]
tiempo_lista = time.time() - start

print(f"\nAcceso a elemento 500,000:")
print(f"Tupla: {tiempo_tupla:.8f} segundos")
print(f"Lista: {tiempo_lista:.8f} segundos")

# 8. CASOS DE USO COMUNES
print("\n=== 8. CASOS DE USO COMUNES ===")

# Coordenadas geográficas
coordenadas_ciudades = {
    "Madrid": (40.4168, -3.7038),
    "Barcelona": (41.3851, 2.1734),
    "Valencia": (39.4699, -0.3763)
}
print("Coordenadas de ciudades:", coordenadas_ciudades)

# Configuraciones que no deben cambiar
CONFIG_DATABASE = ("localhost", 5432, "mydb", "readonly")
host, puerto, db, modo = CONFIG_DATABASE
print(f"Configuración DB: {host}:{puerto}/{db} ({modo})")

# Retorno múltiple de funciones
def obtener_estadisticas(numeros):
    return min(numeros), max(numeros), sum(numeros)/len(numeros)

datos = [10, 20, 30, 40, 50]
minimo, maximo, promedio = obtener_estadisticas(datos)
print(f"Estadísticas: Min={minimo}, Max={maximo}, Promedio={promedio}")

# RGB colores
COLOR_ROJO = (255, 0, 0)
COLOR_VERDE = (0, 255, 0)
COLOR_AZUL = (0, 0, 255)
print("Colores RGB:", COLOR_ROJO, COLOR_VERDE, COLOR_AZUL)

# 9. TUPLAS ANIDADAS Y COMPLEJAS
print("\n=== 9. TUPLAS ANIDADAS ===")
estudiantes = (
    ("Ana", (8, 9, 7)),      # Nombre y calificaciones
    ("Carlos", (6, 8, 9)),
    ("María", (10, 9, 8))
)

print("Estudiantes y calificaciones:")
for nombre, calificaciones in estudiantes:
    promedio = sum(calificaciones) / len(calificaciones)
    print(f"  {nombre}: {calificaciones} -> Promedio: {promedio:.1f}")

# 10. CONVERSIONES
print("\n=== 10. CONVERSIONES ===")
# Lista a tupla
mi_lista = [1, 2, 3, 4, 5]
mi_tupla = tuple(mi_lista)
print(f"Lista: {mi_lista} -> Tupla: {mi_tupla}")

# Tupla a lista
otra_tupla = (10, 20, 30)
otra_lista = list(otra_tupla)
print(f"Tupla: {otra_tupla} -> Lista: {otra_lista}")

# String a tupla
texto = "Python"
tupla_letras = tuple(texto)
print(f"String: '{texto}' -> Tupla: {tupla_letras}")

# 11. ERRORES COMUNES
print("\n=== 11. ERRORES COMUNES ===")
print("❌ ERRORES QUE DEBES EVITAR:")

# Error 1: Olvidar la coma en tupla de un elemento
print("• Tupla de un elemento SIN coma:")
no_es_tupla = (42)  # Esto es solo un número entre paréntesis
print(f"  {no_es_tupla} -> Tipo: {type(no_es_tupla)}")

print("• Tupla de un elemento CON coma:")
si_es_tupla = (42,)  # Esto SÍ es una tupla
print(f"  {si_es_tupla} -> Tipo: {type(si_es_tupla)}")

# Error 2: Intentar modificar
print("• No intentes modificar tuplas:")
print("  tupla[0] = nuevo_valor  # ❌ TypeError")

# Error 3: Confundir con listas
print("• Recuerda la diferencia:")
print("  lista = [1, 2, 3]    # ✓ Mutable")
print("  tupla = (1, 2, 3)    # ✓ Inmutable")

# 12. MÉTODOS DISPONIBLES
print("\n=== 12. MÉTODOS DISPONIBLES ===")
ejemplo_tupla = (1, 2, 3, 2, 4, 2, 5)
print(f"Tupla ejemplo: {ejemplo_tupla}")
print("Métodos disponibles:")
print(f"• count(2): {ejemplo_tupla.count(2)} - cuenta ocurrencias")
print(f"• index(3): {ejemplo_tupla.index(3)} - encuentra índice")
print("• len(): se usa como función len(tupla)")

# RESUMEN FINAL
print("\n" + "="*50)
print("RESUMEN: ¿POR QUÉ SON INMUTABLES LAS TUPLAS?")
print("="*50)
print("🔒 INMUTABILIDAD significa que una vez creada,")
print("   NO SE PUEDE modificar su contenido")
print()
print("💡 VENTAJAS:")
print("   • Protección contra cambios accidentales")
print("   • Mayor velocidad de acceso")
print("   • Pueden usarse como claves en diccionarios")
print("   • Garantizan integridad de datos")
print("   • Ideales para datos que no deben cambiar")
print()
print("🎯 USA TUPLAS CUANDO:")
print("   • Los datos no necesiten modificarse")
print("   • Quieras proteger la información")
print("   • Necesites coordenadas, configuraciones")
print("   • Retornes múltiples valores de funciones")
print()
print("🎯 USA LISTAS CUANDO:")
print("   • Necesites agregar/eliminar elementos")
print("   • Los datos cambien frecuentemente")
print("   • Requieras métodos como append, remove, etc.")