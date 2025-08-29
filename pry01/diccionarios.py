# ==========================================
# DICCIONARIOS EN PYTHON - GUÍA COMPLETA
# ==========================================

# ¿QUÉ SON LOS DICCIONARIOS?
# Los diccionarios son colecciones de pares CLAVE-VALOR
# Son mutables, ordenados (desde Python 3.7+) y no permiten claves duplicadas

print("=== ¿QUÉ SON LOS DICCIONARIOS? ===")
print("Un diccionario es una colección de pares CLAVE-VALOR")
print("Se definen con llaves {} y formato clave: valor")
print("Son como 'mapas' o 'tablas hash' en otros lenguajes")
print()

# 1. CREACIÓN DE DICCIONARIOS
print("=== 1. CREACIÓN DE DICCIONARIOS ===")

# Diccionario vacío
diccionario_vacio = {}
print("Diccionario vacío:", diccionario_vacio)

# También con dict()
otro_vacio = dict()
print("Otro vacío con dict():", otro_vacio)

# Diccionario con datos
persona = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Madrid",
    "activo": True
}
print("Persona:", persona)

# Diferentes formas de crear
# Con dict() y argumentos
empleado = dict(nombre="Carlos", puesto="Developer", salario=50000)
print("Empleado:", empleado)

# Con lista de tuplas
coordenadas = dict([("x", 10), ("y", 20), ("z", 30)])
print("Coordenadas:", coordenadas)

# Con zip()
claves = ["a", "b", "c"]
valores = [1, 2, 3]
abc_dict = dict(zip(claves, valores))
print("Con zip():", abc_dict)

# 2. ACCESO A VALORES
print("\n=== 2. ACCESO A VALORES ===")
estudiante = {
    "nombre": "María",
    "edad": 22,
    "carrera": "Ingeniería",
    "calificaciones": [8, 9, 7, 10]
}

print("Estudiante:", estudiante)

# Acceso directo por clave
print("Nombre:", estudiante["nombre"])
print("Edad:", estudiante["edad"])

# Acceso seguro con get()
print("Carrera:", estudiante.get("carrera"))
print("Teléfono:", estudiante.get("telefono"))  # No existe, retorna None
print("Teléfono con default:", estudiante.get("telefono", "No registrado"))

# 3. MODIFICAR Y AGREGAR ELEMENTOS
print("\n=== 3. MODIFICAR Y AGREGAR ===")
producto = {"nombre": "Laptop", "precio": 1000, "stock": 5}
print("Producto inicial:", producto)

# Modificar valor existente
producto["precio"] = 950
print("Después de cambiar precio:", producto)

# Agregar nueva clave-valor
producto["categoria"] = "Electrónicos"
print("Después de agregar categoría:", producto)

# Múltiples actualizaciones con update()
producto.update({"marca": "Dell", "garantia": "2 años"})
print("Después de update():", producto)

# 4. ELIMINAR ELEMENTOS
print("\n=== 4. ELIMINAR ELEMENTOS ===")
colores = {
    "rojo": "#FF0000",
    "verde": "#00FF00",
    "azul": "#0000FF",
    "amarillo": "#FFFF00"
}
print("Colores iniciales:", colores)

# del - elimina clave específica
del colores["amarillo"]
print("Después de del amarillo:", colores)

# pop() - elimina y retorna valor
color_eliminado = colores.pop("verde")
print(f"Color eliminado: {color_eliminado}, diccionario: {colores}")

# pop() con valor por defecto
color_inexistente = colores.pop("morado", "Color no encontrado")
print("Pop de color inexistente:", color_inexistente)

# popitem() - elimina último par clave-valor (desde Python 3.7+)
ultimo_elemento = colores.popitem()
print(f"Último elemento eliminado: {ultimo_elemento}, diccionario: {colores}")

# clear() - vacía el diccionario
colores_copia = colores.copy()
colores_copia.clear()
print("Después de clear():", colores_copia)

# 5. VERIFICAR EXISTENCIA
print("\n=== 5. VERIFICAR EXISTENCIA ===")
inventario = {
    "manzanas": 50,
    "bananas": 30,
    "naranjas": 25
}
print("Inventario:", inventario)

# Verificar si existe una clave
print("¿Hay manzanas?", "manzanas" in inventario)
print("¿Hay peras?", "peras" in inventario)

# Verificar si NO existe
print("¿No hay peras?", "peras" not in inventario)

# 6. MÉTODOS IMPORTANTES
print("\n=== 6. MÉTODOS IMPORTANTES ===")
configuracion = {
    "host": "localhost",
    "puerto": 8080,
    "debug": True,
    "version": "1.0"
}

print("Configuración:", configuracion)

# keys() - obtener todas las claves
claves = configuracion.keys()
print("Claves:", list(claves))

# values() - obtener todos los valores
valores = configuracion.values()
print("Valores:", list(valores))

# items() - obtener pares clave-valor
items = configuracion.items()
print("Items:", list(items))

# len() - número de elementos
print("Número de configuraciones:", len(configuracion))

# 7. ITERACIÓN SOBRE DICCIONARIOS
print("\n=== 7. ITERACIÓN ===")
puntuaciones = {
    "Ana": 95,
    "Carlos": 87,
    "María": 92,
    "Luis": 78
}

print("Puntuaciones:", puntuaciones)

# Iterar sobre claves
print("\nIterar sobre claves:")
for nombre in puntuaciones:
    print(f"  {nombre}")

# Iterar sobre valores
print("\nIterar sobre valores:")
for puntuacion in puntuaciones.values():
    print(f"  {puntuacion}")

# Iterar sobre claves y valores
print("\nIterar sobre clave-valor:")
for nombre, puntuacion in puntuaciones.items():
    print(f"  {nombre}: {puntuacion}")

# 8. DICCIONARIOS ANIDADOS
print("\n=== 8. DICCIONARIOS ANIDADOS ===")
empresa = {
    "nombre": "TechCorp",
    "empleados": {
        "desarrolladores": {
            "Ana": {"edad": 28, "lenguajes": ["Python", "JavaScript"]},
            "Carlos": {"edad": 32, "lenguajes": ["Java", "C++"]}
        },
        "diseñadores": {
            "María": {"edad": 26, "herramientas": ["Photoshop", "Figma"]}
        }
    },
    "ubicacion": {
        "ciudad": "Madrid",
        "direccion": "Calle Principal 123"
    }
}

print("Empresa:", empresa["nombre"])
print("Desarrollador Ana:", empresa["empleados"]["desarrolladores"]["Ana"])
print("Edad de Ana:", empresa["empleados"]["desarrolladores"]["Ana"]["edad"])
print("Ciudad:", empresa["ubicacion"]["ciudad"])

# 9. COMPRENSIÓN DE DICCIONARIOS (DICT COMPREHENSION)
print("\n=== 9. COMPRENSIÓN DE DICCIONARIOS ===")

# Básica - cuadrados
numeros = [1, 2, 3, 4, 5]
cuadrados = {x: x**2 for x in numeros}
print("Cuadrados:", cuadrados)

# Con condición - solo números pares
pares_cuadrados = {x: x**2 for x in numeros if x % 2 == 0}
print("Cuadrados de pares:", pares_cuadrados)

# Transformar otro diccionario
temperaturas_celsius = {"Madrid": 25, "Barcelona": 22, "Valencia": 28}
temperaturas_fahrenheit = {ciudad: (temp * 9/5) + 32 for ciudad, temp in temperaturas_celsius.items()}
print("Celsius:", temperaturas_celsius)
print("Fahrenheit:", temperaturas_fahrenheit)

# Crear diccionario desde listas
nombres = ["Ana", "Carlos", "María"]
edades = [25, 30, 28]
personas = {nombre: edad for nombre, edad in zip(nombres, edades)}
print("Personas:", personas)

# 10. COMBINAR DICCIONARIOS
print("\n=== 10. COMBINAR DICCIONARIOS ===")
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict3 = {"b": 20, "e": 5}  # "b" se sobrescribirá

print("Dict1:", dict1)
print("Dict2:", dict2)
print("Dict3:", dict3)

# Método update()
combinado1 = dict1.copy()
combinado1.update(dict2)
print("Dict1 + Dict2:", combinado1)

# Operador ** (unpacking)
combinado2 = {**dict1, **dict2, **dict3}
print("Combinación completa:", combinado2)

# Método | (Python 3.9+)
try:
    combinado3 = dict1 | dict2 | dict3
    print("Con operador |:", combinado3)
except TypeError:
    print("Operador | no disponible en esta versión de Python")

# 11. CASOS DE USO COMUNES
print("\n=== 11. CASOS DE USO COMUNES ===")

# Contador de elementos
texto = "python programming"
contador_letras = {}
for letra in texto:
    if letra != " ":
        contador_letras[letra] = contador_letras.get(letra, 0) + 1
print("Contador de letras:", contador_letras)

# Base de datos simple
base_datos_usuarios = {
    "user1": {
        "nombre": "Ana García",
        "email": "ana@email.com",
        "activo": True,
        "ultimo_acceso": "2025-08-28"
    },
    "user2": {
        "nombre": "Carlos López",
        "email": "carlos@email.com",
        "activo": False,
        "ultimo_acceso": "2025-08-20"
    }
}

print("\nBase de datos de usuarios:")
for user_id, datos in base_datos_usuarios.items():
    estado = "Activo" if datos["activo"] else "Inactivo"
    print(f"  {user_id}: {datos['nombre']} - {estado}")

# Configuración de aplicación
configuracion_app = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "myapp_db"
    },
    "api": {
        "version": "v1",
        "timeout": 30,
        "retries": 3
    },
    "features": {
        "debug_mode": False,
        "logging": True,
        "cache": True
    }
}

print("\nConfiguración de aplicación:")
print(f"DB Host: {configuracion_app['database']['host']}")
print(f"API Version: {configuracion_app['api']['version']}")
print(f"Debug Mode: {configuracion_app['features']['debug_mode']}")

# 12. MÉTODOS AVANZADOS
print("\n=== 12. MÉTODOS AVANZADOS ===")

# setdefault() - establece valor si la clave no existe
historial = {}
historial.setdefault("visitas", []).append("página1")
historial.setdefault("visitas", []).append("página2")
historial.setdefault("usuario", "anónimo")
print("Historial:", historial)

# fromkeys() - crear diccionario con claves y valor por defecto
claves_vacias = ["nombre", "edad", "email"]
formulario = dict.fromkeys(claves_vacias, "")
print("Formulario vacío:", formulario)

formulario_ceros = dict.fromkeys(["a", "b", "c"], 0)
print("Con ceros:", formulario_ceros)

# 13. DICCIONARIOS Y FUNCIONES
print("\n=== 13. DICCIONARIOS Y FUNCIONES ===")

def crear_perfil_usuario(**kwargs):
    """Función que acepta argumentos con nombre y crea un perfil"""
    perfil = {
        "nombre": kwargs.get("nombre", "Usuario"),
        "edad": kwargs.get("edad", 0),
        "activo": kwargs.get("activo", True)
    }
    return perfil

# Llamar la función
perfil1 = crear_perfil_usuario(nombre="Ana", edad=25)
perfil2 = crear_perfil_usuario(nombre="Carlos", edad=30, activo=False)

print("Perfil 1:", perfil1)
print("Perfil 2:", perfil2)

def procesar_datos(datos):
    """Función que procesa un diccionario de datos"""
    resultado = {}
    for clave, valor in datos.items():
        if isinstance(valor, str):
            resultado[clave] = valor.upper()
        elif isinstance(valor, (int, float)):
            resultado[clave] = valor * 2
        else:
            resultado[clave] = valor
    return resultado

datos_ejemplo = {"nombre": "ana", "edad": 25, "salario": 1000.5, "activo": True}
datos_procesados = procesar_datos(datos_ejemplo)
print("Datos originales:", datos_ejemplo)
print("Datos procesados:", datos_procesados)

# 14. ERRORES COMUNES
print("\n=== 14. ERRORES COMUNES ===")
print("❌ ERRORES QUE DEBES EVITAR:")

# Error 1: KeyError por clave inexistente
test_dict = {"a": 1, "b": 2}
print("• Acceso a clave inexistente:")
try:
    valor = test_dict["c"]  # Esto causará KeyError
except KeyError as e:
    print(f"  ERROR: {e}")
    print("  SOLUCIÓN: Usar get() -> test_dict.get('c', 'default')")

# Error 2: Claves no hashables
print("• Intentar usar lista como clave:")
try:
    bad_dict = {[1, 2]: "valor"}  # Las listas no son hashables
except TypeError as e:
    print(f"  ERROR: {e}")
    print("  SOLUCIÓN: Usar tupla -> {(1, 2): 'valor'}")

# Error 3: Modificar diccionario durante iteración
print("• Modificar durante iteración:")
print("  ❌ for k in dict: del dict[k]  # Puede causar errores")
print("  ✓ for k in list(dict.keys()): del dict[k]  # Seguro")

# 15. COMPARACIÓN CON OTRAS ESTRUCTURAS
print("\n=== 15. COMPARACIÓN CON OTRAS ESTRUCTURAS ===")
print("DICCIONARIOS vs LISTAS vs TUPLAS")
print("-" * 50)
print("CARACTERÍSTICA     | DICT     | LISTA    | TUPLA")
print("-" * 50)
print("Acceso por índice  | ❌       | ✓        | ✓")
print("Acceso por clave   | ✓        | ❌       | ❌")
print("Ordenado           | ✓(3.7+)  | ✓        | ✓")
print("Mutable            | ✓        | ✓        | ❌")
print("Duplicados         | ❌(clave)| ✓        | ✓")
print("Hashable           | ❌       | ❌       | ✓")
print("Búsqueda rápida    | ✓(O(1))  | ❌(O(n)) | ❌(O(n))")

# 16. RENDIMIENTO Y MEJORES PRÁCTICAS
print("\n=== 16. MEJORES PRÁCTICAS ===")
print("💡 CONSEJOS DE RENDIMIENTO:")
print("• Usa get() en lugar de [] para acceso seguro")
print("• Prefiere dict comprehension para transformaciones")
print("• Usa setdefault() para valores por defecto")
print("• Las claves deben ser inmutables (str, int, tuple)")
print("• Los diccionarios son ideales para búsquedas rápidas")

print("\n🎯 CUÁNDO USAR DICCIONARIOS:")
print("• Necesitas asociar claves únicas con valores")
print("• Requieres búsquedas rápidas por clave")
print("• Modelar entidades del mundo real (persona, producto)")
print("• Configuraciones y parámetros")
print("• Contadores y agrupaciones")
print("• Cache/memoización")

# EJEMPLOS PRÁCTICOS FINALES
print("\n=== EJEMPLOS PRÁCTICOS FINALES ===")

# Sistema de inventario
inventario_tienda = {
    "P001": {"nombre": "Laptop", "precio": 999.99, "stock": 10},
    "P002": {"nombre": "Mouse", "precio": 25.50, "stock": 50},
    "P003": {"nombre": "Teclado", "precio": 75.00, "stock": 30}
}

def mostrar_producto(codigo):
    if codigo in inventario_tienda:
        producto = inventario_tienda[codigo]
        print(f"Producto {codigo}: {producto['nombre']}")
        print(f"Precio: ${producto['precio']}")
        print(f"Stock: {producto['stock']} unidades")
    else:
        print(f"Producto {codigo} no encontrado")

print("Sistema de inventario:")
mostrar_producto("P001")
mostrar_producto("P999")

# Sistema de calificaciones
estudiantes_calificaciones = {
    "Ana": {"matematicas": 9, "ciencias": 8, "historia": 7},
    "Carlos": {"matematicas": 7, "ciencias": 9, "historia": 8},
    "María": {"matematicas": 10, "ciencias": 9, "historia": 9}
}

def calcular_promedio(estudiante):
    if estudiante in estudiantes_calificaciones:
        calificaciones = estudiantes_calificaciones[estudiante]
        promedio = sum(calificaciones.values()) / len(calificaciones)
        return round(promedio, 2)
    return None

print("\nPromedios de estudiantes:")
for estudiante in estudiantes_calificaciones:
    promedio = calcular_promedio(estudiante)
    print(f"{estudiante}: {promedio}")

# RESUMEN FINAL
print("\n" + "="*60)
print("RESUMEN: DICCIONARIOS EN PYTHON")
print("="*60)
print("🔑 CONCEPTO CLAVE: Pares CLAVE-VALOR")
print("📝 SINTAXIS: {clave: valor, clave2: valor2}")
print("🔄 MUTABLES: Se pueden modificar después de crear")
print("⚡ RÁPIDOS: Búsqueda O(1) por clave")
print("🎯 ÚNICOS: Las claves no se pueden repetir")
print("📋 ORDENADOS: Mantienen orden de inserción (Python 3.7+)")
print()
print("💪 SUPERPODERES:")
print("   • Acceso instantáneo por clave")
print("   • Estructura flexible para datos complejos")
print("   • Perfectos para mapeos y relaciones")
print("   • Base para muchas estructuras de datos avanzadas")
print()
print("🎖️ ¡DOMINA LOS DICCIONARIOS Y TENDRÁS UNA HERRAMIENTA")
print("   PODEROSA PARA CUALQUIER PROYECTO EN PYTHON!")