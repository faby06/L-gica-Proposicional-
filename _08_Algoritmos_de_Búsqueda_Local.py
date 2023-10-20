
import math
import random

# Funci�n de costo (puede personalizarla para su problema)
def funcion_de_costo(solucion):
    # Ejemplo de funci�n de costo: la suma de los cuadrados de los elementos
    return sum(x ** 2 for x in solucion)

# Funci�n para generar una soluci�n vecina
def generar_vecino(solucion, temperatura):
    vecino = solucion[:]
    indice = random.randint(0, len(vecino) - 1)
    cambio = random.uniform(-1, 1) * temperatura
    vecino[indice] += cambio
    return vecino

def recocido_simulado(funcion_de_costo, solucion_inicial, T_inicial, T_final, max_iter):
    solucion_actual = solucion_inicial
    costo_actual = funcion_de_costo(solucion_actual)
    mejor_solucion = solucion_actual
    mejor_costo = costo_actual

    for iteracion in range(max_iter):
        temperatura = T_inicial * math.exp(-iteracion / (max_iter / math.log(T_final / T_inicial)))
        vecino = generar_vecino(solucion_actual, temperatura)
        costo_vecino = funcion_de_costo(vecino)
        
        if costo_vecino < costo_actual:
            solucion_actual = vecino
            costo_actual = costo_vecino
            if costo_vecino < mejor_costo:
                mejor_solucion = vecino
                mejor_costo = costo_vecino
        else:
            probabilidad_aceptacion = math.exp((costo_actual - costo_vecino) / temperatura)
            if random.random() < probabilidad_aceptacion:
                solucion_actual = vecino
                costo_actual = costo_vecino

    return mejor_solucion, mejor_costo

# Par�metros del algoritmo
solucion_inicial = [random.uniform(-10, 10) for _ in range(5)]
T_inicial = 100.0
T_final = 0.1
max_iter = 1000

# Ejecutar el algoritmo de Recocido Simulado
mejor_solucion, mejor_costo = recocido_simulado(funcion_de_costo, solucion_inicial, T_inicial, T_final, max_iter)

print("Mejor soluci�n encontrada:", mejor_solucion)
print("Mejor costo encontrado:", mejor_costo)
