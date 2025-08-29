# ==========================================
# ESTRUCTURAS DE DECISIÓN Y REPETICIÓN EN PYTHON
# ==========================================

# Las estructuras de control permiten dirigir el flujo de ejecución del programa
# - DECISIÓN: if, elif, else (ejecutar código según condiciones)
# - REPETICIÓN: for, while (repetir código múltiples veces)

print("=== ESTRUCTURAS DE CONTROL EN PYTHON ===")
print("Controlan el FLUJO de ejecución del programa")
print("📋 DECISIÓN: if, elif, else")
print("🔄 REPETICIÓN: for, while")
print()

# ==========================================
# PARTE 1: ESTRUCTURAS DE DECISIÓN
# ==========================================

print("=" * 50)
print("PARTE 1: ESTRUCTURAS DE DECISIÓN")
print("=" * 50)

# 1. ESTRUCTURA IF BÁSICA
print("\n=== 1. ESTRUCTURA IF BÁSICA ===")
print("Ejecuta código SOLO si una condición es verdadera")

edad = 18
print(f"Edad: {edad}")

if edad >= 18:
    print("✓ Eres mayor de edad")
    print("  Puedes votar")

print("Esta línea siempre se ejecuta")

# Ejemplo práctico
temperatura = 25
print(f"\nTemperatura: {temperatura}°C")

if temperatura > 30:
    print("🔥 Hace mucho calor")

if temperatura < 10:
    print("🥶 Hace mucho frío")

# 2. ESTRUCTURA IF-ELSE
print("\n=== 2. ESTRUCTURA IF-ELSE ===")
print("Ejecuta un código si es verdadero, otro si es falso")

numero = 7
print(f"Número: {numero}")

if numero % 2 == 0:
    print("El número es PAR")
else:
    print("El número es IMPAR")

# Ejemplo práctico: Sistema de acceso
usuario = "admin"
contraseña = "12345"

print(f"\nUsuario: {usuario}, Contraseña: {contraseña}")

if usuario == "admin" and contraseña == "12345":
    print("✓ Acceso CONCEDIDO")
    print("  Bienvenido al sistema")
else:
    print("❌ Acceso DENEGADO")
    print("  Credenciales incorrectas")

# 3. ESTRUCTURA IF-ELIF-ELSE
print("\n=== 3. ESTRUCTURA IF-ELIF-ELSE ===")
print("Permite múltiples condiciones")

calificacion = 85
print(f"Calificación: {calificacion}")

if calificacion >= 90:
    letra = "A"
    comentario = "Excelente"
elif calificacion >= 80:
    letra = "B"
    comentario = "Muy bueno"
elif calificacion >= 70:
    letra = "C"
    comentario = "Bueno"
elif calificacion >= 60:
    letra = "D"
    comentario = "Suficiente"
else:
    letra = "F"
    comentario = "Insuficiente"

print(f"Resultado: {letra} - {comentario}")

# Ejemplo práctico: Calculadora de IMC
peso = 70  # kg
altura = 1.75  # metros
imc = peso / (altura ** 2)

print(f"\nPeso: {peso}kg, Altura: {altura}m")
print(f"IMC: {imc:.2f}")

if imc < 18.5:
    categoria = "Bajo peso"
elif imc < 25:
    categoria = "Peso normal"
elif imc < 30:
    categoria = "Sobrepeso"
else:
    categoria = "Obesidad"

print(f"Categoría: {categoria}")

# 4. OPERADORES DE COMPARACIÓN
print("\n=== 4. OPERADORES DE COMPARACIÓN ===")
a, b = 10, 5
print(f"a = {a}, b = {b}")
print("Operador | Resultado | Descripción")
print("---------|-----------|-------------")
print(f"a == b   | {a == b}     | Igual")
print(f"a != b   | {a != b}      | Diferente")
print(f"a > b    | {a > b}      | Mayor que")
print(f"a < b    | {a < b}     | Menor que")
print(f"a >= b   | {a >= b}     | Mayor o igual")
print(f"a <= b   | {a <= b}     | Menor o igual")

# 5. OPERADORES LÓGICOS
print("\n=== 5. OPERADORES LÓGICOS ===")
lluvia = True
paraguas = False
print(f"Lluvia: {lluvia}, Tengo paraguas: {paraguas}")

# AND - ambas condiciones deben ser verdaderas
if lluvia and paraguas:
    print("✓ Puedo salir sin mojarme")
elif lluvia and not paraguas:
    print("❌ Mejor me quedo en casa")
else:
    print("✓ Puedo salir tranquilo")

# OR - al menos una condición debe ser verdadera
dia_libre = True
dinero = False
print(f"\nDía libre: {dia_libre}, Tengo dinero: {dinero}")

if dia_libre or dinero:
    print("✓ Puedo considerar salir")
else:
    print("❌ Mejor me quedo en casa")

# NOT - invierte el valor booleano
conectado = False
print(f"\nConectado: {conectado}")
if not conectado:
    print("❌ Sin conexión a internet")

# 6. OPERADORES DE MEMBRESÍA
print("\n=== 6. OPERADORES DE MEMBRESÍA ===")
frutas = ["manzana", "banana", "naranja"]
fruta_elegida = "banana"

print(f"Frutas disponibles: {frutas}")
print(f"Fruta elegida: {fruta_elegida}")

if fruta_elegida in frutas:
    print("✓ Fruta disponible")
else:
    print("❌ Fruta no disponible")

# Ejemplo con strings
email = "usuario@gmail.com"
if "@" in email and "." in email:
    print(f"✓ {email} parece un email válido")
else:
    print(f"❌ {email} no parece un email válido")

# 7. IF TERNARIO (CONDICIONAL)
print("\n=== 7. IF TERNARIO ===")
print("Forma compacta: valor_si_verdadero if condicion else valor_si_falso")

edad_persona = 20
estado = "Mayor" if edad_persona >= 18 else "Menor"
print(f"Edad: {edad_persona} -> Estado: {estado}")

# Ejemplos múltiples
temperatura = 15
ropa = "abrigo" if temperatura < 15 else "camiseta" if temperatura > 25 else "jersey"
print(f"Temperatura: {temperatura}°C -> Ropa: {ropa}")

numero = -5
signo = "positivo" if numero > 0 else "negativo" if numero < 0 else "cero"
print(f"Número: {numero} -> Signo: {signo}")

# ==========================================
# PARTE 2: ESTRUCTURAS DE REPETICIÓN
# ==========================================

print("\n" + "=" * 50)
print("PARTE 2: ESTRUCTURAS DE REPETICIÓN")
print("=" * 50)

# 8. BUCLE FOR - ITERACIÓN SOBRE SECUENCIAS
print("\n=== 8. BUCLE FOR ===")
print("Itera sobre elementos de una secuencia")

# For con listas
print("\nIterando sobre lista:")
colores = ["rojo", "verde", "azul"]
for color in colores:
    print(f"  - Color: {color}")

# For con strings
print("\nIterando sobre string:")
palabra = "Python"
for letra in palabra:
    print(f"  Letra: {letra}")

# For con range()
print("\nUsando range():")
print("range(5):", end=" ")
for i in range(5):
    print(i, end=" ")
print()

print("range(2, 8):", end=" ")
for i in range(2, 8):
    print(i, end=" ")
print()

print("range(0, 10, 2):", end=" ")
for i in range(0, 10, 2):
    print(i, end=" ")
print()

# 9. FOR CON ENUMERATE
print("\n=== 9. FOR CON ENUMERATE ===")
print("Obtiene índice y valor al mismo tiempo")

estudiantes = ["Ana", "Carlos", "María"]
print("Lista de estudiantes:")
for indice, nombre in enumerate(estudiantes):
    print(f"  {indice + 1}. {nombre}")

# Enumerate con inicio personalizado
print("\nCon inicio en 10:")
for indice, nombre in enumerate(estudiantes, start=10):
    print(f"  ID {indice}: {nombre}")

# 10. FOR CON ZIP
print("\n=== 10. FOR CON ZIP ===")
print("Itera sobre múltiples secuencias simultáneamente")

nombres = ["Ana", "Carlos", "María"]
edades = [25, 30, 28]
ciudades = ["Madrid", "Barcelona", "Valencia"]

print("Información de personas:")
for nombre, edad, ciudad in zip(nombres, edades, ciudades):
    print(f"  {nombre}, {edad} años, vive en {ciudad}")

# 11. BUCLE WHILE
print("\n=== 11. BUCLE WHILE ===")
print("Repite mientras una condición sea verdadera")

# Ejemplo básico
contador = 1
print("Contando hasta 5:")
while contador <= 5:
    print(f"  Contador: {contador}")
    contador += 1  # Muy importante: actualizar la variable

# Ejemplo práctico: Menú
print("\nSimulación de menú:")
opcion = 0
menu_activo = True

# Simulamos selecciones de usuario
selecciones = [1, 3, 2, 4]  # 4 será salir
indice_seleccion = 0

while menu_activo and indice_seleccion < len(selecciones):
    opcion = selecciones[indice_seleccion]
    indice_seleccion += 1
    
    print(f"\nOpción seleccionada: {opcion}")
    
    if opcion == 1:
        print("  ✓ Opción 1: Ver datos")
    elif opcion == 2:
        print("  ✓ Opción 2: Editar")
    elif opcion == 3:
        print("  ✓ Opción 3: Configuración")
    elif opcion == 4:
        print("  ✓ Saliendo del programa...")
        menu_activo = False
    else:
        print("  ❌ Opción inválida")

# 12. CONTROL DE BUCLES: BREAK Y CONTINUE
print("\n=== 12. CONTROL DE BUCLES ===")

# BREAK - termina el bucle inmediatamente
print("BREAK - Buscar número específico:")
numeros = [1, 3, 7, 2, 9, 4]
buscar = 7

for i, num in enumerate(numeros):
    print(f"  Revisando posición {i}: {num}")
    if num == buscar:
        print(f"  ✓ ¡Encontrado {buscar} en posición {i}!")
        break
else:
    print(f"  ❌ {buscar} no encontrado")

# CONTINUE - salta a la siguiente iteración
print("\nCONTINUE - Mostrar solo números pares:")
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numeros:
    if num % 2 != 0:  # Si es impar
        continue  # Salta esta iteración
    print(f"  Número par: {num}")

# 13. BUCLES ANIDADOS
print("\n=== 13. BUCLES ANIDADOS ===")
print("Un bucle dentro de otro bucle")

# Tabla de multiplicar
print("Tablas de multiplicar (1-3):")
for tabla in range(1, 4):
    print(f"\nTabla del {tabla}:")
    for multiplicador in range(1, 6):
        resultado = tabla * multiplicador
        print(f"  {tabla} x {multiplicador} = {resultado}")

# Matriz
print("\nMatriz 3x3:")
matriz = []
for fila in range(3):
    fila_actual = []
    for columna in range(3):
        valor = fila * 3 + columna + 1
        fila_actual.append(valor)
    matriz.append(fila_actual)

for fila in matriz:
    print(f"  {fila}")

# 14. COMPRENSIONES (LIST COMPREHENSION)
print("\n=== 14. COMPRENSIONES ===")
print("Forma compacta de crear listas con bucles")

# Comprensión básica
numeros = [1, 2, 3, 4, 5]
cuadrados = [x**2 for x in numeros]
print(f"Números: {numeros}")
print(f"Cuadrados: {cuadrados}")

# Con condición
pares = [x for x in range(1, 11) if x % 2 == 0]
print(f"Números pares del 1-10: {pares}")

# Más compleja
palabras = ["python", "java", "javascript", "go"]
palabras_largas = [palabra.upper() for palabra in palabras if len(palabra) > 4]
print(f"Palabras largas: {palabras_largas}")

# Comparación tradicional vs comprensión
print("\nComparación:")
# Forma tradicional
resultado_tradicional = []
for x in range(5):
    if x % 2 == 0:
        resultado_tradicional.append(x * 2)

# Comprensión
resultado_comprension = [x * 2 for x in range(5) if x % 2 == 0]

print(f"Tradicional: {resultado_tradicional}")
print(f"Comprensión: {resultado_comprension}")

# 15. CASOS PRÁCTICOS AVANZADOS
print("\n=== 15. CASOS PRÁCTICOS AVANZADOS ===")

# Sistema de validación
def validar_password(password):
    """Valida una contraseña con múltiples criterios"""
    criterios = {
        "longitud": len(password) >= 8,
        "mayuscula": any(c.isupper() for c in password),
        "minuscula": any(c.islower() for c in password),
        "numero": any(c.isdigit() for c in password),
        "especial": any(c in "!@#$%^&*" for c in password)
    }
    
    print(f"Validando password: {'*' * len(password)}")
    valida = True
    
    for criterio, cumple in criterios.items():
        estado = "✓" if cumple else "❌"
        print(f"  {estado} {criterio.capitalize()}: {cumple}")
        if not cumple:
            valida = False
    
    return valida

# Testear contraseñas
passwords_test = ["123", "Password1!", "password", "PASSWORD123"]
for pwd in passwords_test:
    print(f"\nTesting: {pwd}")
    es_valida = validar_password(pwd)
    print(f"Resultado: {'VÁLIDA' if es_valida else 'INVÁLIDA'}")
    print("-" * 30)

# Procesador de datos con estructuras combinadas
def procesar_ventas(ventas_data):
    """Procesa datos de ventas con estructuras de control"""
    print("Procesando datos de ventas...")
    
    total_ventas = 0
    ventas_por_vendedor = {}
    productos_populares = {}
    
    for venta in ventas_data:
        vendedor = venta["vendedor"]
        producto = venta["producto"]
        cantidad = venta["cantidad"]
        precio = venta["precio"]
        
        # Calcular total
        subtotal = cantidad * precio
        total_ventas += subtotal
        
        # Agrupar por vendedor
        if vendedor not in ventas_por_vendedor:
            ventas_por_vendedor[vendedor] = 0
        ventas_por_vendedor[vendedor] += subtotal
        
        # Contar productos populares
        if producto not in productos_populares:
            productos_populares[producto] = 0
        productos_populares[producto] += cantidad
    
    # Mostrar resultados
    print(f"\nTotal de ventas: ${total_ventas:,.2f}")
    
    print("\nVentas por vendedor:")
    for vendedor, total in ventas_por_vendedor.items():
        print(f"  {vendedor}: ${total:,.2f}")
    
    print("\nProductos más vendidos:")
    productos_ordenados = sorted(productos_populares.items(), 
                                key=lambda x: x[1], reverse=True)
    for producto, cantidad in productos_ordenados[:3]:
        print(f"  {producto}: {cantidad} unidades")

# Datos de ejemplo
ventas_ejemplo = [
    {"vendedor": "Ana", "producto": "Laptop", "cantidad": 2, "precio": 999.99},
    {"vendedor": "Carlos", "producto": "Mouse", "cantidad": 5, "precio": 25.50},
    {"vendedor": "Ana", "producto": "Teclado", "cantidad": 3, "precio": 75.00},
    {"vendedor": "María", "producto": "Laptop", "cantidad": 1, "precio": 999.99},
    {"vendedor": "Carlos", "producto": "Monitor", "cantidad": 2, "precio": 299.99}
]

procesar_ventas(ventas_ejemplo)

# 16. ERRORES COMUNES
print("\n=== 16. ERRORES COMUNES ===")
print("❌ ERRORES QUE DEBES EVITAR:")

print("\n1. Bucle infinito en WHILE:")
print("   while True:  # ❌ Sin condición de salida")
print("       print('Infinito')")
print("   SOLUCIÓN: Siempre actualizar la variable de control")

print("\n2. Modificar lista durante iteración:")
print("   for item in lista:")
print("       lista.remove(item)  # ❌ Puede causar errores")
print("   SOLUCIÓN: Iterar sobre copia: for item in lista.copy():")

print("\n3. Confundir = con ==:")
print("   if x = 5:  # ❌ Asignación en lugar de comparación")
print("   if x == 5:  # ✓ Comparación correcta")

print("\n4. Olvidar incrementar en WHILE:")
print("   contador = 0")
print("   while contador < 5:")
print("       print(contador)  # ❌ Falta: contador += 1")

# 17. MEJORES PRÁCTICAS
print("\n=== 17. MEJORES PRÁCTICAS ===")
print("💡 CONSEJOS PARA CÓDIGO LIMPIO:")
print()
print("✓ USA FOR cuando sepas cuántas iteraciones necesitas")
print("✓ USA WHILE cuando la condición sea dinámica")
print("✓ Prefiere comprensiones para transformaciones simples")
print("✓ Usa nombres descriptivos para variables de control")
print("✓ Evita bucles anidados profundos (máximo 3 niveles)")
print("✓ Considera funciones para lógica compleja")
print("✓ Usa break y continue con moderación")
print("✓ Siempre ten condiciones de salida claras")

# RESUMEN FINAL
print("\n" + "="*70)
print("RESUMEN: ESTRUCTURAS DE DECISIÓN Y REPETICIÓN")
print("="*70)

print("\n📋 ESTRUCTURAS DE DECISIÓN:")
print("┌─────────────┬─────────────────────────────────────────┐")
print("│ ESTRUCTURA  │ USO                                     │")
print("├─────────────┼─────────────────────────────────────────┤")
print("│ if          │ Una sola condición                     │")
print("│ if-else     │ Dos alternativas                       │")
print("│ if-elif-else│ Múltiples condiciones                  │")
print("│ ternario    │ Asignación condicional compacta        │")
print("└─────────────┴─────────────────────────────────────────┘")

print("\n🔄 ESTRUCTURAS DE REPETICIÓN:")
print("┌─────────────┬─────────────────────────────────────────┐")
print("│ ESTRUCTURA  │ USO                                     │")
print("├─────────────┼─────────────────────────────────────────┤")
print("│ for         │ Iterar sobre secuencias conocidas      │")
print("│ while       │ Repetir mientras condición sea true    │")
print("│ break       │ Salir del bucle inmediatamente         │")
print("│ continue    │ Saltar a siguiente iteración           │")
print("│ comprensión │ Crear listas de forma compacta          │")
print("└─────────────┴─────────────────────────────────────────┘")

print("\n🎯 CUÁNDO USAR CADA UNA:")
print("• IF: Para tomar decisiones simples")
print("• IF-ELIF-ELSE: Para múltiples opciones excluyentes")
print("• FOR: Cuando conoces la secuencia o número de iteraciones")
print("• WHILE: Para bucles con condiciones dinámicas")
print("• COMPRENSIONES: Para transformar datos de forma elegante")

print("\n🚀 ¡DOMINA ESTAS ESTRUCTURAS Y PODRÁS CREAR")
print("   CUALQUIER LÓGICA DE PROGRAMACIÓN EN PYTHON!")