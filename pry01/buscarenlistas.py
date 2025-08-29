# ==========================================
# BÚSQUEDA DE NÚMEROS DE FIBONACCI EN LISTAS
# ==========================================

import math

def es_numero_fibonacci(numero):
    """
    Verifica si un número pertenece a la secuencia de Fibonacci.
    
    Un número n es de Fibonacci si y solo si uno de estos es un cuadrado perfecto:
    - (5*n^2 + 4) 
    - (5*n^2 - 4)
    
    Args:
        numero (int): El número a verificar
        
    Returns:
        bool: True si es número de Fibonacci, False en caso contrario
    """
    if numero < 0:
        return False
    
    # Verificar si (5*n^2 + 4) o (5*n^2 - 4) es un cuadrado perfecto
    def es_cuadrado_perfecto(n):
        if n < 0:
            return False
        raiz = int(math.sqrt(n))
        return raiz * raiz == n
    
    return (es_cuadrado_perfecto(5 * numero * numero + 4) or 
            es_cuadrado_perfecto(5 * numero * numero - 4))

def generar_fibonacci(limite):
    """
    Genera números de Fibonacci hasta un límite específico.
    
    Args:
        limite (int): Número máximo hasta el cual generar Fibonacci
        
    Returns:
        list: Lista de números de Fibonacci hasta el límite
    """
    fibonacci = []
    a, b = 0, 1
    
    while a <= limite:
        fibonacci.append(a)
        a, b = b, a + b
    
    return fibonacci

def buscar_fibonacci_en_lista(numeros):
    """
    Busca números de Fibonacci en una lista de números.
    
    Args:
        numeros (list): Lista de números donde buscar
        
    Returns:
        dict: Diccionario con resultados de la búsqueda
    """
    if not numeros:
        return {
            "fibonacci_encontrados": [],
            "posiciones": [],
            "no_fibonacci": [],
            "total_fibonacci": 0,
            "porcentaje": 0.0
        }
    
    fibonacci_encontrados = []
    posiciones = []
    no_fibonacci = []
    
    for i, numero in enumerate(numeros):
        if es_numero_fibonacci(numero):
            fibonacci_encontrados.append(numero)
            posiciones.append(i)
        else:
            no_fibonacci.append(numero)
    
    total_fibonacci = len(fibonacci_encontrados)
    porcentaje = (total_fibonacci / len(numeros)) * 100 if numeros else 0
    
    return {
        "fibonacci_encontrados": fibonacci_encontrados,
        "posiciones": posiciones,
        "no_fibonacci": no_fibonacci,
        "total_fibonacci": total_fibonacci,
        "porcentaje": round(porcentaje, 2)
    }

def buscar_fibonacci_optimizado(numeros):
    """
    Versión optimizada que pre-genera Fibonacci hasta el máximo de la lista.
    
    Args:
        numeros (list): Lista de números donde buscar
        
    Returns:
        dict: Diccionario con resultados de la búsqueda
    """
    if not numeros:
        return {
            "fibonacci_encontrados": [],
            "posiciones": [],
            "no_fibonacci": [],
            "total_fibonacci": 0,
            "porcentaje": 0.0
        }
    
    # Encontrar el número máximo en la lista
    numero_maximo = max(numeros)
    
    # Generar todos los números de Fibonacci hasta el máximo
    fibonacci_set = set(generar_fibonacci(numero_maximo))
    
    fibonacci_encontrados = []
    posiciones = []
    no_fibonacci = []
    
    for i, numero in enumerate(numeros):
        if numero in fibonacci_set:
            fibonacci_encontrados.append(numero)
            posiciones.append(i)
        else:
            no_fibonacci.append(numero)
    
    total_fibonacci = len(fibonacci_encontrados)
    porcentaje = (total_fibonacci / len(numeros)) * 100
    
    return {
        "fibonacci_encontrados": fibonacci_encontrados,
        "posiciones": posiciones,
        "no_fibonacci": no_fibonacci,
        "total_fibonacci": total_fibonacci,
        "porcentaje": round(porcentaje, 2)
    }

def mostrar_resultados(numeros, resultados):
    """
    Muestra los resultados de la búsqueda de forma organizada.
    
    Args:
        numeros (list): Lista original de números
        resultados (dict): Resultados de la búsqueda
    """
    print("=" * 50)
    print("RESULTADOS DE BÚSQUEDA DE FIBONACCI")
    print("=" * 50)
    
    print(f"Lista original: {numeros}")
    print(f"Total de números: {len(numeros)}")
    print()
    
    print(f"✅ Números de Fibonacci encontrados: {resultados['fibonacci_encontrados']}")
    print(f"📍 Posiciones en la lista: {resultados['posiciones']}")
    print(f"❌ Números NO Fibonacci: {resultados['no_fibonacci']}")
    print()
    
    print(f"📊 ESTADÍSTICAS:")
    print(f"   • Total de Fibonacci: {resultados['total_fibonacci']}")
    print(f"   • Porcentaje: {resultados['porcentaje']}%")
    print()

def ejemplos_de_uso():
    """
    Función que demuestra diferentes ejemplos de uso.
    """
    print("🔍 EJEMPLOS DE BÚSQUEDA DE FIBONACCI EN LISTAS")
    print("=" * 60)
    
    # Ejemplo 1: Lista con algunos números de Fibonacci
    print("\n📋 EJEMPLO 1: Lista mixta")
    numeros1 = [1, 2, 3, 4, 5, 8, 10, 13, 15, 21, 25, 34]
    resultados1 = buscar_fibonacci_en_lista(numeros1)
    mostrar_resultados(numeros1, resultados1)
    
    # Ejemplo 2: Lista con muchos números de Fibonacci
    print("\n📋 EJEMPLO 2: Primeros números de Fibonacci")
    fibonacci_puros = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    resultados2 = buscar_fibonacci_en_lista(fibonacci_puros)
    mostrar_resultados(fibonacci_puros, resultados2)
    
    # Ejemplo 3: Lista sin números de Fibonacci
    print("\n📋 EJEMPLO 3: Sin números de Fibonacci")
    no_fibonacci = [4, 6, 7, 9, 10, 11, 12, 14, 15, 16]
    resultados3 = buscar_fibonacci_en_lista(no_fibonacci)
    mostrar_resultados(no_fibonacci, resultados3)
    
    # Ejemplo 4: Lista con números grandes
    print("\n📋 EJEMPLO 4: Números más grandes")
    numeros_grandes = [50, 55, 89, 100, 144, 200, 233, 377, 400, 610]
    resultados4 = buscar_fibonacci_en_lista(numeros_grandes)
    mostrar_resultados(numeros_grandes, resultados4)
    
    # Ejemplo 5: Lista con números negativos y cero
    print("\n📋 EJEMPLO 5: Con negativos y cero")
    numeros_mixtos = [-5, -1, 0, 1, 2, 3, 4, 5, 8]
    resultados5 = buscar_fibonacci_en_lista(numeros_mixtos)
    mostrar_resultados(numeros_mixtos, resultados5)

def comparar_rendimiento():
    """
    Compara el rendimiento entre la función normal y la optimizada.
    """
    import time
    
    print("\n⚡ COMPARACIÓN DE RENDIMIENTO")
    print("=" * 40)
    
    # Lista grande para probar rendimiento
    lista_grande = list(range(1, 1001))  # Números del 1 al 1000
    
    # Probar función normal
    inicio = time.time()
    resultados_normal = buscar_fibonacci_en_lista(lista_grande)
    tiempo_normal = time.time() - inicio
    
    # Probar función optimizada
    inicio = time.time()
    resultados_optimizado = buscar_fibonacci_optimizado(lista_grande)
    tiempo_optimizado = time.time() - inicio
    
    print(f"Lista de prueba: {len(lista_grande)} números (1-1000)")
    print(f"Fibonacci encontrados: {resultados_normal['total_fibonacci']}")
    print()
    print(f"Función normal:    {tiempo_normal:.4f} segundos")
    print(f"Función optimizada: {tiempo_optimizado:.4f} segundos")
    
    if tiempo_normal > 0:
        mejora = tiempo_normal / tiempo_optimizado
        print(f"Mejora de velocidad: {mejora:.2f}x más rápida")

def buscar_fibonacci_con_detalles(numeros):
    """
    Función avanzada que proporciona información detallada.
    
    Args:
        numeros (list): Lista de números donde buscar
        
    Returns:
        dict: Resultados detallados de la búsqueda
    """
    if not numeros:
        return {"error": "Lista vacía"}
    
    # Generar secuencia de Fibonacci hasta el máximo
    numero_maximo = max(numeros) if numeros else 0
    fibonacci_completo = generar_fibonacci(numero_maximo)
    fibonacci_set = set(fibonacci_completo)
    
    detalles = []
    fibonacci_encontrados = []
    estadisticas = {
        "total_numeros": len(numeros),
        "fibonacci_encontrados": 0,
        "mayor_fibonacci": 0,
        "menor_fibonacci": float('inf'),
        "suma_fibonacci": 0
    }
    
    for i, numero in enumerate(numeros):
        es_fib = numero in fibonacci_set
        detalle = {
            "posicion": i,
            "numero": numero,
            "es_fibonacci": es_fib,
            "indice_fibonacci": fibonacci_completo.index(numero) if es_fib else None
        }
        detalles.append(detalle)
        
        if es_fib:
            fibonacci_encontrados.append(numero)
            estadisticas["fibonacci_encontrados"] += 1
            estadisticas["suma_fibonacci"] += numero
            estadisticas["mayor_fibonacci"] = max(estadisticas["mayor_fibonacci"], numero)
            if estadisticas["menor_fibonacci"] == float('inf'):
                estadisticas["menor_fibonacci"] = numero
            else:
                estadisticas["menor_fibonacci"] = min(estadisticas["menor_fibonacci"], numero)
    
    # Ajustar menor_fibonacci si no se encontraron números
    if estadisticas["menor_fibonacci"] == float('inf'):
        estadisticas["menor_fibonacci"] = 0
    
    porcentaje = (estadisticas["fibonacci_encontrados"] / estadisticas["total_numeros"]) * 100
    
    return {
        "detalles": detalles,
        "fibonacci_encontrados": sorted(set(fibonacci_encontrados)),
        "estadisticas": estadisticas,
        "porcentaje": round(porcentaje, 2),
        "secuencia_fibonacci_completa": fibonacci_completo
    }

def mostrar_analisis_detallado(numeros):
    """
    Muestra un análisis detallado de la búsqueda.
    
    Args:
        numeros (list): Lista de números a analizar
    """
    print("\n🔬 ANÁLISIS DETALLADO")
    print("=" * 50)
    
    resultados = buscar_fibonacci_con_detalles(numeros)
    
    if "error" in resultados:
        print(f"Error: {resultados['error']}")
        return
    
    print(f"Lista analizada: {numeros}")
    print()
    
    # Mostrar detalles por número
    print("📋 ANÁLISIS POR NÚMERO:")
    print("Pos | Número | ¿Fibonacci? | Índice en secuencia")
    print("-" * 50)
    
    for detalle in resultados["detalles"]:
        pos = detalle["posicion"]
        num = detalle["numero"]
        es_fib = "✅ Sí" if detalle["es_fibonacci"] else "❌ No"
        indice = detalle["indice_fibonacci"] if detalle["indice_fibonacci"] is not None else "-"
        print(f"{pos:3} | {num:6} | {es_fib:8} | {indice}")
    
    print()
    
    # Mostrar estadísticas
    stats = resultados["estadisticas"]
    print("📊 ESTADÍSTICAS DETALLADAS:")
    print(f"   • Total de números analizados: {stats['total_numeros']}")
    print(f"   • Números de Fibonacci encontrados: {stats['fibonacci_encontrados']}")
    print(f"   • Porcentaje de Fibonacci: {resultados['porcentaje']}%")
    
    if stats['fibonacci_encontrados'] > 0:
        print(f"   • Fibonacci más pequeño encontrado: {stats['menor_fibonacci']}")
        print(f"   • Fibonacci más grande encontrado: {stats['mayor_fibonacci']}")
        print(f"   • Suma de todos los Fibonacci: {stats['suma_fibonacci']}")
        promedio = stats['suma_fibonacci'] / stats['fibonacci_encontrados']
        print(f"   • Promedio de Fibonacci encontrados: {promedio:.2f}")
    
    print()
    print(f"🧮 Secuencia de Fibonacci generada (hasta {max(numeros) if numeros else 0}):")
    fib_sequence = resultados["secuencia_fibonacci_completa"]
    if len(fib_sequence) <= 20:
        print(f"   {fib_sequence}")
    else:
        print(f"   Primeros 10: {fib_sequence[:10]}")
        print(f"   Últimos 10: {fib_sequence[-10:]}")
        print(f"   (Total: {len(fib_sequence)} números)")

# ==========================================
# FUNCIÓN PRINCIPAL PARA DEMOSTRACIÓN
# ==========================================

def main():
    """
    Función principal que ejecuta todos los ejemplos.
    """
    print("🎯 BUSCADOR DE NÚMEROS DE FIBONACCI EN LISTAS")
    print("=" * 60)
    print("Este programa encuentra números de Fibonacci en cualquier lista.")
    print()
    
    # Ejecutar ejemplos básicos
    ejemplos_de_uso()
    
    # Análisis detallado con una lista específica
    print("\n" + "=" * 60)
    lista_para_analisis = [1, 4, 8, 15, 21, 34, 50, 55, 89, 100]
    mostrar_analisis_detallado(lista_para_analisis)
    
    # Comparación de rendimiento
    comparar_rendimiento()
    
    # Función interactiva simple
    print("\n" + "=" * 60)
    print("🎮 EJEMPLO INTERACTIVO")
    print("=" * 25)
    
    # Ejemplo con lista personalizable
    mi_lista = [0, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
    print(f"Analizando lista: {mi_lista}")
    
    resultados = buscar_fibonacci_optimizado(mi_lista)
    mostrar_resultados(mi_lista, resultados)
    
    print("\n✨ FUNCIONES DISPONIBLES:")
    print("• buscar_fibonacci_en_lista(numeros)")
    print("• buscar_fibonacci_optimizado(numeros)")
    print("• buscar_fibonacci_con_detalles(numeros)")
    print("• es_numero_fibonacci(numero)")
    print("• generar_fibonacci(limite)")
    
    print("\n🎓 ¡Prueba las funciones con tus propias listas!")

# ==========================================
# EJECUCIÓN DEL PROGRAMA
# ==========================================

if __name__ == "__main__":
    main()
else:
    print("📚 Módulo de búsqueda de Fibonacci cargado.")
    print("💡 Usa main() para ver ejemplos completos.")
    print("🚀 O usa directamente las funciones:")
    print("   • buscar_fibonacci_en_lista([1,2,3,5,8])")
    print("   • es_numero_fibonacci(21)")