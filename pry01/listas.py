# ==========================================
# PRINCIPALES OPERACIONES CON LISTAS EN PYTHON
# ==========================================

# 1. CREACIÓN DE LISTAS
print("=== 1. CREACIÓN DE LISTAS ===")
lista_vacia = []
lista_numeros = [1, 2, 3, 4, 5]
lista_mixta = [1, "texto", 3.14, True]
lista_repetida = [0] * 5  # [0, 0, 0, 0, 0]
lista_rango = list(range(1, 6))  # [1, 2, 3, 4, 5]

print("Lista vacía:", lista_vacia)
print("Lista números:", lista_numeros)
print("Lista mixta:", lista_mixta)
print("Lista repetida:", lista_repetida)
print("Lista rango:", lista_rango)

# 2. ACCESO A ELEMENTOS (INDEXACIÓN)
print("\n=== 2. ACCESO A ELEMENTOS ===")
palabra = ['d','f','f','g','q']
print("Primer elemento:", palabra[0])
print("Segundo elemento:", palabra[1])
print("Último elemento:", palabra[-1])
print("Penúltimo elemento:", palabra[-2])

# 3. SLICING (REBANADO)
print("\n=== 3. SLICING ===")
otraPalabra = 'Murcielagos Blancos'
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("palabra[1:3]:", palabra[1:3])
print("numeros[2:7]:", numeros[2:7])
print("numeros[:5]:", numeros[:5])
print("numeros[5:]:", numeros[5:])
print("numeros[::2]:", numeros[::2])  # Cada 2 elementos
print("numeros[::-1]:", numeros[::-1])  # Lista invertida

# 4. AGREGAR ELEMENTOS
print("\n=== 4. AGREGAR ELEMENTOS ===")
frutas = ["manzana", "banana"]
print("Lista inicial:", frutas)

# append() - agrega un elemento al final
frutas.append("naranja")
print("Después de append('naranja'):", frutas)

# insert() - agrega en posición específica
frutas.insert(1, "uva")
print("Después de insert(1, 'uva'):", frutas)

# extend() - agrega múltiples elementos
frutas.extend(["pera", "kiwi"])
print("Después de extend(['pera', 'kiwi']):", frutas)

# 5. ELIMINAR ELEMENTOS
print("\n=== 5. ELIMINAR ELEMENTOS ===")
colores = ["rojo", "verde", "azul", "amarillo", "verde"]
print("Lista inicial:", colores)

# remove() - elimina la primera ocurrencia
colores.remove("verde")
print("Después de remove('verde'):", colores)

# pop() - elimina por índice y retorna el elemento
elemento_eliminado = colores.pop(1)
print(f"Después de pop(1), elemento eliminado: {elemento_eliminado}, lista: {colores}")

# del - elimina por índice
del colores[0]
print("Después de del colores[0]:", colores)

# clear() - vacía la lista
colores_copia = colores.copy()
colores_copia.clear()
print("Después de clear():", colores_copia)

# 6. MODIFICAR ELEMENTOS
print("\n=== 6. MODIFICAR ELEMENTOS ===")
animales = ["gato", "perro", "pájaro"]
print("Lista original:", animales)
animales[1] = "león"
print("Después de animales[1] = 'león':", animales)
animales[0:2] = ["tigre", "oso"]
print("Después de animales[0:2] = ['tigre', 'oso']:", animales)

# 7. BUSCAR Y VERIFICAR
print("\n=== 7. BUSCAR Y VERIFICAR ===")
tecnologias = ["Python", "Java", "JavaScript", "C++", "Python"]
print("Lista:", tecnologias)
print("'Python' in tecnologias:", "Python" in tecnologias)
print("'Ruby' in tecnologias:", "Ruby" in tecnologias)
print("Índice de 'Java':", tecnologias.index("Java"))
print("Contar 'Python':", tecnologias.count("Python"))

# 8. ORDENAR LISTAS
print("\n=== 8. ORDENAR LISTAS ===")
numeros_desordenados = [5, 2, 8, 1, 9, 3]
print("Lista original:", numeros_desordenados)

# sort() - modifica la lista original
numeros_copia = numeros_desordenados.copy()
numeros_copia.sort()
print("Después de sort():", numeros_copia)

# sorted() - retorna nueva lista ordenada
nueva_lista = sorted(numeros_desordenados, reverse=True)
print("sorted() descendente:", nueva_lista)
print("Lista original sin cambios:", numeros_desordenados)

# reverse() - invierte la lista
numeros_desordenados.reverse()
print("Después de reverse():", numeros_desordenados)

# 9. FUNCIONES ÚTILES
print("\n=== 9. FUNCIONES ÚTILES ===")
edades = [25, 30, 18, 45, 22, 35]
print("Lista de edades:", edades)
print("Longitud len():", len(edades))
print("Máximo max():", max(edades))
print("Mínimo min():", min(edades))
print("Suma sum():", sum(edades))
print("Promedio:", sum(edades) / len(edades))

# 10. COMPRENSIÓN DE LISTAS (LIST COMPREHENSION)
print("\n=== 10. COMPRENSIÓN DE LISTAS ===")
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Básica
cuadrados = [x**2 for x in numeros]
print("Cuadrados:", cuadrados)

# Con condición
pares = [x for x in numeros if x % 2 == 0]
print("Números pares:", pares)

# Más compleja
resultado = [x*2 if x % 2 == 0 else x*3 for x in numeros]
print("x*2 si par, x*3 si impar:", resultado)

# 11. CONCATENAR Y REPETIR
print("\n=== 11. CONCATENAR Y REPETIR ===")
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
concatenada = lista1 + lista2
print("Concatenación (+):", concatenada)
repetida = lista1 * 3
print("Repetición (*):", repetida)

# 12. COPIAR LISTAS
print("\n=== 12. COPIAR LISTAS ===")
original = [1, 2, [3, 4]]
copia_superficial = original.copy()  # o original[:]
import copy
copia_profunda = copy.deepcopy(original)

print("Original:", original)
print("Copia superficial:", copia_superficial)
print("Copia profunda:", copia_profunda)

# 13. ITERAR SOBRE LISTAS
print("\n=== 13. ITERAR SOBRE LISTAS ===")
nombres = ["Ana", "Carlos", "María"]

print("Iteración simple:")
for nombre in nombres:
    print(f"  - {nombre}")

print("Con índice usando enumerate:")
for i, nombre in enumerate(nombres):
    print(f"  {i}: {nombre}")

print("Con índice manual:")
for i in range(len(nombres)):
    print(f"  Posición {i}: {nombres[i]}")

print("\n=== ¡PRACTICA ESTAS OPERACIONES! ===")
print("Estas son las operaciones fundamentales que todo programador")
print("Python debe dominar para trabajar eficientemente con listas.")
