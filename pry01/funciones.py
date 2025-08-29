# ==========================================
# FUNCIONES EN PYTHON - GUÍA COMPLETA
# ==========================================

# ¿QUÉ SON LAS FUNCIONES?
# Las funciones son bloques de código reutilizable que realizan una tarea específica
# Permiten organizar el código, evitar repetición y hacer programas más mantenibles

print("=== ¿QUÉ SON LAS FUNCIONES? ===")
print("📦 Bloques de código REUTILIZABLE")
print("🎯 Realizan una TAREA ESPECÍFICA")
print("🔄 Se pueden LLAMAR múltiples veces")
print("📋 Reciben PARÁMETROS y pueden RETORNAR valores")
print("🧩 Hacen el código más ORGANIZADO y MODULAR")
print()

# ==========================================
# PARTE 1: FUNCIONES BÁSICAS
# ==========================================

print("=" * 50)
print("PARTE 1: FUNCIONES BÁSICAS")
print("=" * 50)

# 1. FUNCIÓN SIN PARÁMETROS Y SIN RETORNO
print("\n=== 1. FUNCIÓN BÁSICA ===")
print("Sintaxis: def nombre_funcion():")

def saludar():
    """Función que saluda - sin parámetros, sin retorno"""
    print("¡Hola, bienvenido a Python!")
    print("Esta es mi primera función")

# Llamar la función
print("Llamando a saludar():")
saludar()

def mostrar_info():
    """Muestra información del programa"""
    print("\n--- Información del Programa ---")
    print("Nombre: Sistema de Aprendizaje")
    print("Versión: 1.0")
    print("Autor: Estudiante Python")
    print("--------------------------------")

mostrar_info()

# 2. FUNCIÓN CON PARÁMETROS
print("\n=== 2. FUNCIONES CON PARÁMETROS ===")

def saludar_persona(nombre):
    """Función que recibe un parámetro"""
    print(f"¡Hola {nombre}! ¿Cómo estás?")

# Llamar con diferentes valores
print("Llamando con diferentes parámetros:")
saludar_persona("Ana")
saludar_persona("Carlos")
saludar_persona("María")

def presentar_persona(nombre, edad, ciudad):
    """Función con múltiples parámetros"""
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad} años")
    print(f"Ciudad: {ciudad}")
    print("-" * 20)

print("\nPresentaciones:")
presentar_persona("Ana", 25, "Madrid")
presentar_persona("Carlos", 30, "Barcelona")

# 3. FUNCIONES CON RETORNO
print("\n=== 3. FUNCIONES CON RETORNO ===")

def sumar(a, b):
    """Función que retorna un valor"""
    resultado = a + b
    return resultado

# Usar el valor retornado
print("Ejemplos de retorno:")
suma1 = sumar(5, 3)
print(f"5 + 3 = {suma1}")

suma2 = sumar(10, 20)
print(f"10 + 20 = {suma2}")

# Usar directamente en otras operaciones
total = sumar(suma1, suma2)
print(f"Total: {total}")

def calcular_area_rectangulo(ancho, alto):
    """Calcula el área de un rectángulo"""
    area = ancho * alto
    return area

def calcular_perimetro_rectangulo(ancho, alto):
    """Calcula el perímetro de un rectángulo"""
    perimetro = 2 * (ancho + alto)
    return perimetro

# Ejemplo práctico
ancho_rectangulo = 5
alto_rectangulo = 3

area = calcular_area_rectangulo(ancho_rectangulo, alto_rectangulo)
perimetro = calcular_perimetro_rectangulo(ancho_rectangulo, alto_rectangulo)

print(f"\nRectángulo {ancho_rectangulo}x{alto_rectangulo}:")
print(f"Área: {area}")
print(f"Perímetro: {perimetro}")

# 4. MÚLTIPLES VALORES DE RETORNO
print("\n=== 4. MÚLTIPLES VALORES DE RETORNO ===")

def analizar_numero(numero):
    """Analiza un número y retorna múltiples características"""
    es_par = numero % 2 == 0
    es_positivo = numero > 0
    cuadrado = numero ** 2
    return es_par, es_positivo, cuadrado

# Desempaquetar los valores retornados
numero_test = 7
par, positivo, cuadrado = analizar_numero(numero_test)

print(f"Análisis del número {numero_test}:")
print(f"¿Es par? {par}")
print(f"¿Es positivo? {positivo}")
print(f"Su cuadrado: {cuadrado}")

def estadisticas_lista(numeros):
    """Calcula estadísticas de una lista"""
    if not numeros:  # Lista vacía
        return 0, 0, 0, 0
    
    total = sum(numeros)
    promedio = total / len(numeros)
    maximo = max(numeros)
    minimo = min(numeros)
    
    return total, promedio, maximo, minimo

# Ejemplo con lista
calificaciones = [85, 92, 78, 95, 87, 90]
suma, prom, max_val, min_val = estadisticas_lista(calificaciones)

print(f"\nEstadísticas de calificaciones {calificaciones}:")
print(f"Suma: {suma}")
print(f"Promedio: {prom:.2f}")
print(f"Máximo: {max_val}")
print(f"Mínimo: {min_val}")

# ==========================================
# PARTE 2: PARÁMETROS AVANZADOS
# ==========================================

print("\n" + "=" * 50)
print("PARTE 2: PARÁMETROS AVANZADOS")
print("=" * 50)

# 5. PARÁMETROS POR DEFECTO
print("\n=== 5. PARÁMETROS POR DEFECTO ===")

def crear_perfil(nombre, edad=18, ciudad="No especificada", activo=True):
    """Función con parámetros por defecto"""
    perfil = {
        "nombre": nombre,
        "edad": edad,
        "ciudad": ciudad,
        "activo": activo
    }
    return perfil

# Diferentes formas de llamar
print("Usando parámetros por defecto:")
perfil1 = crear_perfil("Ana")
print(f"Perfil 1: {perfil1}")

perfil2 = crear_perfil("Carlos", 25)
print(f"Perfil 2: {perfil2}")

perfil3 = crear_perfil("María", 30, "Madrid")
print(f"Perfil 3: {perfil3}")

perfil4 = crear_perfil("Luis", 28, "Barcelona", False)
print(f"Perfil 4: {perfil4}")

def configurar_servidor(host="localhost", puerto=8080, debug=False, ssl=False):
    """Configuración de servidor con valores por defecto"""
    config = {
        "host": host,
        "puerto": puerto,
        "debug": debug,
        "ssl": ssl
    }
    print(f"Servidor configurado: {config}")
    return config

print("\nConfiguraciones de servidor:")
configurar_servidor()  # Todo por defecto
configurar_servidor("192.168.1.1")  # Solo cambiar host
configurar_servidor(puerto=3000, debug=True)  # Cambiar específicos

# 6. ARGUMENTOS CON NOMBRE (KEYWORD ARGUMENTS)
print("\n=== 6. ARGUMENTOS CON NOMBRE ===")

def crear_usuario(nombre, email, edad, ciudad, activo):
    """Función que muestra el poder de los argumentos con nombre"""
    usuario = {
        "nombre": nombre,
        "email": email,
        "edad": edad,
        "ciudad": ciudad,
        "activo": activo
    }
    print(f"Usuario creado: {usuario}")
    return usuario

# Llamada con argumentos posicionales (orden importa)
print("Argumentos posicionales:")
crear_usuario("Ana", "ana@email.com", 25, "Madrid", True)

# Llamada con argumentos con nombre (orden no importa)
print("\nArgumentos con nombre:")
crear_usuario(
    edad=30,
    nombre="Carlos", 
    activo=False,
    ciudad="Barcelona",
    email="carlos@email.com"
)

# Mezcla de ambos (posicionales primero, luego con nombre)
print("\nMezcla de argumentos:")
crear_usuario("María", "maria@email.com", edad=28, activo=True, ciudad="Valencia")

# 7. *ARGS - ARGUMENTOS VARIABLES
print("\n=== 7. *ARGS - ARGUMENTOS VARIABLES ===")

def sumar_todos(*numeros):
    """Función que suma cualquier cantidad de números"""
    print(f"Números recibidos: {numeros}")
    total = sum(numeros)
    return total

# Llamar con diferentes cantidades de argumentos
print("Sumando diferentes cantidades:")
resultado1 = sumar_todos(1, 2, 3)
print(f"Suma de 1,2,3: {resultado1}")

resultado2 = sumar_todos(10, 20, 30, 40, 50)
print(f"Suma de 10,20,30,40,50: {resultado2}")

resultado3 = sumar_todos(100)
print(f"Suma de 100: {resultado3}")

def imprimir_informacion(titulo, *detalles):
    """Función que acepta un título y múltiples detalles"""
    print(f"\n=== {titulo.upper()} ===")
    for i, detalle in enumerate(detalles, 1):
        print(f"{i}. {detalle}")

# Ejemplos de uso
imprimir_informacion("Lenguajes de programación", "Python", "JavaScript", "Java", "C++")
imprimir_informacion("Frutas favoritas", "Manzana", "Banana", "Naranja")

# 8. **KWARGS - ARGUMENTOS CON NOMBRE VARIABLES
print("\n=== 8. **KWARGS - ARGUMENTOS CON NOMBRE VARIABLES ===")

def crear_configuracion(**opciones):
    """Función que acepta opciones de configuración variables"""
    print("Configuración creada:")
    for clave, valor in opciones.items():
        print(f"  {clave}: {valor}")
    return opciones

# Llamar con diferentes opciones
print("Configuración de base de datos:")
config_db = crear_configuracion(
    host="localhost",
    puerto=5432,
    database="myapp",
    usuario="admin",
    ssl=True
)

print("\nConfiguración de API:")
config_api = crear_configuracion(
    version="v1",
    timeout=30,
    retries=3,
    cache=True
)

def procesar_pedido(cliente, **detalles):
    """Procesa un pedido con detalles variables"""
    print(f"\nProcesando pedido para: {cliente}")
    print("Detalles del pedido:")
    
    for item, valor in detalles.items():
        print(f"  {item}: {valor}")
    
    # Calcular total si hay precios
    total = 0
    if "precio" in detalles:
        cantidad = detalles.get("cantidad", 1)
        total = detalles["precio"] * cantidad
        print(f"Total: ${total:.2f}")

# Ejemplos de pedidos
procesar_pedido("Ana", producto="Laptop", precio=999.99, cantidad=1, envio="express")
procesar_pedido("Carlos", servicio="Consultoría", horas=5, tarifa_hora=50.0)

# 9. COMBINANDO *ARGS Y **KWARGS
print("\n=== 9. COMBINANDO *ARGS Y **KWARGS ===")

def funcion_completa(requerido, por_defecto="default", *args, **kwargs):
    """Función que demuestra todos los tipos de parámetros"""
    print(f"Parámetro requerido: {requerido}")
    print(f"Parámetro por defecto: {por_defecto}")
    print(f"Argumentos adicionales (*args): {args}")
    print(f"Argumentos con nombre (**kwargs): {kwargs}")
    print("-" * 30)

# Diferentes formas de llamar
print("Ejemplos de función completa:")
funcion_completa("valor1")
funcion_completa("valor1", "valor2", "extra1", "extra2", opcion1="a", opcion2="b")

def logger(nivel, mensaje, *detalles, **metadatos):
    """Sistema de logging flexible"""
    print(f"[{nivel.upper()}] {mensaje}")
    
    if detalles:
        print("Detalles adicionales:")
        for detalle in detalles:
            print(f"  - {detalle}")
    
    if metadatos:
        print("Metadatos:")
        for clave, valor in metadatos.items():
            print(f"  {clave}: {valor}")
    print()

# Ejemplos de logging
logger("info", "Usuario conectado")
logger("warning", "Memoria baja", "Usar con precaución", "Considerar reinicio", 
       timestamp="2025-08-28", usuario="admin", ip="192.168.1.1")
logger("error", "Base de datos no disponible", "Reintentando conexión", 
       codigo_error=500, modulo="database")

# ==========================================
# PARTE 3: CONCEPTOS AVANZADOS
# ==========================================

print("\n" + "=" * 50)
print("PARTE 3: CONCEPTOS AVANZADOS")
print("=" * 50)

# 10. ÁMBITO DE VARIABLES (SCOPE)
print("\n=== 10. ÁMBITO DE VARIABLES ===")

# Variable global
contador_global = 0

def demostrar_scope():
    """Demuestra el ámbito de variables"""
    # Variable local
    contador_local = 10
    
    # Acceder a variable global (solo lectura)
    print(f"Variable global leída: {contador_global}")
    print(f"Variable local: {contador_local}")

def modificar_global():
    """Modifica variable global usando 'global'"""
    global contador_global
    contador_global += 1
    print(f"Variable global modificada: {contador_global}")

print("Demostrando ámbito:")
demostrar_scope()
modificar_global()
modificar_global()

# Variable global vs local con mismo nombre
numero = 100  # Global

def probar_variables():
    numero = 50  # Local (sombrea la global)
    print(f"Número local: {numero}")

def usar_global():
    global numero
    numero = 200  # Modifica la global
    print(f"Número global modificado: {numero}")

print(f"\nNúmero inicial (global): {numero}")
probar_variables()
print(f"Número después de función local: {numero}")
usar_global()
print(f"Número después de modificar global: {numero}")

# 11. FUNCIONES COMO OBJETOS
print("\n=== 11. FUNCIONES COMO OBJETOS ===")

def saludar_formal(nombre):
    return f"Buenos días, Sr./Sra. {nombre}"

def saludar_informal(nombre):
    return f"¡Hola {nombre}! ¿Qué tal?"

# Asignar función a variable
mi_saludo = saludar_formal
print("Función asignada a variable:")
print(mi_saludo("García"))

# Lista de funciones
tipos_saludo = [saludar_formal, saludar_informal]
nombre_persona = "Ana"

print(f"\nDiferentes saludos para {nombre_persona}:")
for i, funcion_saludo in enumerate(tipos_saludo):
    saludo = funcion_saludo(nombre_persona)
    print(f"{i+1}. {saludo}")

# Función que retorna otra función
def crear_multiplicador(factor):
    """Retorna una función que multiplica por el factor dado"""
    def multiplicar(numero):
        return numero * factor
    return multiplicar

# Crear diferentes multiplicadores
multiplicar_por_2 = crear_multiplicador(2)
multiplicar_por_10 = crear_multiplicador(10)

print("\nFunciones que retornan funciones:")
print(f"5 × 2 = {multiplicar_por_2(5)}")
print(f"5 × 10 = {multiplicar_por_10(5)}")

# 12. FUNCIONES LAMBDA (ANÓNIMAS)
print("\n=== 12. FUNCIONES LAMBDA ===")

# Lambda básica
cuadrado = lambda x: x ** 2
print(f"Cuadrado de 5: {cuadrado(5)}")

# Lambda con múltiples parámetros
suma = lambda a, b: a + b
print(f"Suma 3 + 7: {suma(3, 7)}")

# Lambda en operaciones de lista
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Usar con map()
cuadrados = list(map(lambda x: x**2, numeros))
print(f"Números: {numeros}")
print(f"Cuadrados: {cuadrados}")

# Usar con filter()
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(f"Números pares: {pares}")

# Usar con sorted()
palabras = ["python", "java", "c", "javascript", "go"]
palabras_por_longitud = sorted(palabras, key=lambda palabra: len(palabra))
print(f"Palabras ordenadas por longitud: {palabras_por_longitud}")

# 13. DECORADORES (INTRODUCCIÓN BÁSICA)
print("\n=== 13. DECORADORES BÁSICOS ===")

def cronometrar(func):
    """Decorador que mide el tiempo de ejecución"""
    def wrapper(*args, **kwargs):
        import time
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"Función '{func.__name__}' tardó {fin - inicio:.4f} segundos")
        return resultado
    return wrapper

@cronometrar
def operacion_lenta():
    """Función que simula una operación lenta"""
    import time
    time.sleep(0.1)  # Simular trabajo
    return "Operación completada"

print("Usando decorador:")
resultado = operacion_lenta()
print(f"Resultado: {resultado}")

# 14. DOCUMENTACIÓN DE FUNCIONES (DOCSTRINGS)
print("\n=== 14. DOCUMENTACIÓN DE FUNCIONES ===")

def calcular_imc(peso, altura):
    """
    Calcula el Índice de Masa Corporal (IMC).
    
    Args:
        peso (float): Peso en kilogramos
        altura (float): Altura en metros
    
    Returns:
        tuple: (imc, categoria) donde imc es float y categoria es string
    
    Examples:
        >>> calcular_imc(70, 1.75)
        (22.86, 'Peso normal')
    """
    imc = peso / (altura ** 2)
    
    if imc < 18.5:
        categoria = "Bajo peso"
    elif imc < 25:
        categoria = "Peso normal"
    elif imc < 30:
        categoria = "Sobrepeso"
    else:
        categoria = "Obesidad"
    
    return round(imc, 2), categoria

# Usar la función documentada
peso_persona = 70
altura_persona = 1.75
imc, categoria = calcular_imc(peso_persona, altura_persona)

print(f"IMC de persona ({peso_persona}kg, {altura_persona}m):")
print(f"IMC: {imc}")
print(f"Categoría: {categoria}")

# Acceder a la documentación
print(f"\nDocumentación de la función:")
print(calcular_imc.__doc__)

# ==========================================
# PARTE 4: CASOS PRÁCTICOS
# ==========================================

print("\n" + "=" * 50)
print("PARTE 4: CASOS PRÁCTICOS")
print("=" * 50)

# 15. SISTEMA DE GESTIÓN DE ESTUDIANTES
print("\n=== 15. SISTEMA DE GESTIÓN DE ESTUDIANTES ===")

def crear_estudiante(nombre, edad, carrera, calificaciones=None):
    """Crea un diccionario de estudiante"""
    if calificaciones is None:
        calificaciones = []
    
    return {
        "nombre": nombre,
        "edad": edad,
        "carrera": carrera,
        "calificaciones": calificaciones
    }

def agregar_calificacion(estudiante, calificacion):
    """Agrega una calificación al estudiante"""
    if 0 <= calificacion <= 100:
        estudiante["calificaciones"].append(calificacion)
        return True
    return False

def calcular_promedio(estudiante):
    """Calcula el promedio de calificaciones"""
    calificaciones = estudiante["calificaciones"]
    if not calificaciones:
        return 0
    return sum(calificaciones) / len(calificaciones)

def obtener_estado(estudiante):
    """Determina si el estudiante aprueba o no"""
    promedio = calcular_promedio(estudiante)
    return "Aprobado" if promedio >= 60 else "Reprobado"

def mostrar_estudiante(estudiante):
    """Muestra información completa del estudiante"""
    print(f"Nombre: {estudiante['nombre']}")
    print(f"Edad: {estudiante['edad']}")
    print(f"Carrera: {estudiante['carrera']}")
    print(f"Calificaciones: {estudiante['calificaciones']}")
    print(f"Promedio: {calcular_promedio(estudiante):.2f}")
    print(f"Estado: {obtener_estado(estudiante)}")
    print("-" * 30)

# Ejemplo de uso del sistema
print("Sistema de gestión de estudiantes:")

# Crear estudiantes
estudiante1 = crear_estudiante("Ana García", 20, "Ingeniería")
estudiante2 = crear_estudiante("Carlos López", 22, "Medicina")

# Agregar calificaciones
agregar_calificacion(estudiante1, 85)
agregar_calificacion(estudiante1, 90)
agregar_calificacion(estudiante1, 78)

agregar_calificacion(estudiante2, 95)
agregar_calificacion(estudiante2, 88)
agregar_calificacion(estudiante2, 92)

# Mostrar información
mostrar_estudiante(estudiante1)
mostrar_estudiante(estudiante2)

# 16. CALCULADORA AVANZADA
print("\n=== 16. CALCULADORA AVANZADA ===")

def sumar(a, b):
    """Suma dos números"""
    return a + b

def restar(a, b):
    """Resta dos números"""
    return a - b

def multiplicar(a, b):
    """Multiplica dos números"""
    return a * b

def dividir(a, b):
    """Divide dos números"""
    if b == 0:
        return "Error: División por cero"
    return a / b

def potencia(base, exponente):
    """Calcula la potencia"""
    return base ** exponente

def factorial(n):
    """Calcula el factorial de un número"""
    if n < 0:
        return "Error: Factorial de número negativo"
    if n == 0 or n == 1:
        return 1
    
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

def calculadora(operacion, *args):
    """Calculadora que acepta diferentes operaciones"""
    operaciones = {
        "suma": sumar,
        "resta": restar,
        "multiplicacion": multiplicar,
        "division": dividir,
        "potencia": potencia,
        "factorial": factorial
    }
    
    if operacion not in operaciones:
        return "Operación no válida"
    
    func = operaciones[operacion]
    
    try:
        if operacion == "factorial":
            if len(args) != 1:
                return "Factorial requiere exactamente un argumento"
            return func(args[0])
        else:
            if len(args) != 2:
                return "Esta operación requiere exactamente dos argumentos"
            return func(args[0], args[1])
    except Exception as e:
        return f"Error: {e}"

# Ejemplos de uso de la calculadora
print("Calculadora avanzada:")
print(f"Suma 10 + 5: {calculadora('suma', 10, 5)}")
print(f"División 20 / 4: {calculadora('division', 20, 4)}")
print(f"División 10 / 0: {calculadora('division', 10, 0)}")
print(f"Potencia 2^8: {calculadora('potencia', 2, 8)}")
print(f"Factorial 5: {calculadora('factorial', 5)}")

# ==========================================
# PARTE 5: MEJORES PRÁCTICAS Y ERRORES
# ==========================================

print("\n" + "=" * 50)
print("PARTE 5: MEJORES PRÁCTICAS")
print("=" * 50)

# 17. MEJORES PRÁCTICAS
print("\n=== 17. MEJORES PRÁCTICAS ===")
print("💡 CONSEJOS PARA ESCRIBIR BUENAS FUNCIONES:")
print()
print("✓ PRINCIPIO DE RESPONSABILIDAD ÚNICA:")
print("  • Cada función debe hacer UNA cosa bien")
print("  • Si tu función hace muchas cosas, divídela")

print("\n✓ NOMBRES DESCRIPTIVOS:")
print("  • ❌ def calc(a, b): ...")
print("  • ✅ def calcular_area_rectangulo(ancho, alto): ...")

print("\n✓ FUNCIONES PEQUEÑAS:")
print("  • Máximo 20-30 líneas")
print("  • Si es más larga, considera dividirla")

print("\n✓ DOCUMENTACIÓN:")
print("  • Siempre usa docstrings")
print("  • Explica qué hace, parámetros y retorno")

print("\n✓ VALORES POR DEFECTO:")
print("  • Usa None para listas/diccionarios por defecto")
print("  • ❌ def func(lista=[]): ...")
print("  • ✅ def func(lista=None): if lista is None: lista = []")

print("\n✓ MANEJO DE ERRORES:")
print("  • Valida parámetros de entrada")
print("  • Usa try/except cuando sea necesario")

# 18. ERRORES COMUNES
print("\n=== 18. ERRORES COMUNES ===")
print("❌ ERRORES QUE DEBES EVITAR:")

print("\n1. Valor por defecto mutable:")
# ❌ MAL
def mal_ejemplo(lista=[]):
    lista.append("nuevo")
    return lista

print("Problema con valor por defecto mutable:")
resultado1 = mal_ejemplo()
resultado2 = mal_ejemplo()
print(f"Primera llamada: {resultado1}")
print(f"Segunda llamada: {resultado2}")  # ¡Contiene elementos anteriores!

# ✅ BIEN
def buen_ejemplo(lista=None):
    if lista is None:
        lista = []
    lista.append("nuevo")
    return lista

print("\nSolución correcta:")
resultado3 = buen_ejemplo()
resultado4 = buen_ejemplo()
print(f"Primera llamada: {resultado3}")
print(f"Segunda llamada: {resultado4}")

print("\n2. No retornar valor cuando se necesita:")
print("   ❌ def procesar_datos(datos): datos.sort()  # No retorna nada")
print("   ✅ def procesar_datos(datos): return sorted(datos)")

print("\n3. Funciones muy largas y complejas:")
print("   ❌ Una función que hace 10 cosas diferentes")
print("   ✅ 10 funciones que hacen una cosa cada una")

print("\n4. Nombres confusos:")
print("   ❌ def proc(d, x, y): ...")
print("   ✅ def procesar_pedido(cliente, producto, cantidad): ...")

# RESUMEN FINAL
print("\n" + "="*70)
print("RESUMEN: FUNCIONES EN PYTHON")
print("="*70)

print("\n📦 ANATOMÍA DE UNA FUNCIÓN:")
print("def nombre_funcion(parametros):")
print("    \"\"\"Documentación\"\"\"")
print("    # código")
print("    return valor  # opcional")

print("\n🎯 TIPOS DE PARÁMETROS:")
print("┌─────────────────┬─────────────────────────────────────┐")
print("│ TIPO            │ EJEMPLO                             │")
print("├─────────────────┼─────────────────────────────────────┤")
print("│ Requeridos      │ def func(a, b):                     │")
print("│ Por defecto     │ def func(a, b=10):                  │")
print("│ *args          │ def func(*args):                    │")
print("│ **kwargs       │ def func(**kwargs):                 │")
print("│ Combinados      │ def func(a, b=10, *args, **kwargs): │")
print("└─────────────────┴─────────────────────────────────────┘")

print("\n🔄 CONCEPTOS CLAVE:")
print("• REUTILIZACIÓN: Escribe una vez, usa muchas veces")
print("• MODULARIDAD: Divide problemas complejos en partes")
print("• LEGIBILIDAD: Código más fácil de entender")
print("• MANTENIMIENTO: Cambios en un solo lugar")
print("• TESTING: Funciones son fáciles de probar")

print("\n💡 CUÁNDO CREAR UNA FUNCIÓN:")
print("• Código que se repite 2+ veces")
print("• Operación lógica específica")
print("• Código que puede reutilizarse")
print("• Para organizar código complejo")
print("• Para hacer el programa más legible")

print("\n🚀 ¡LAS FUNCIONES SON EL CORAZÓN DE LA PROGRAMACIÓN!")
print("   Domina las funciones y podrás crear programas")
print("   elegantes, organizados y mantenibles en Python.")