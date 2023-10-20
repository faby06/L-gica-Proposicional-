#Inferencia Lógica Proposicional

import itertools

# Definir las proposiciones
proposiciones = ['p', 'q', 'r']

# Generar todas las combinaciones posibles de verdad para las proposiciones
combinaciones = list(itertools.product([True, False], repeat=len(proposiciones)))

# Definir una expresión lógica (puede ser personalizada)
expresion_logica = "(p and q) or (not r)"

# Realizar la inferencia lógica y mostrar el resultado
print("Proposiciones | Resultado")
print("-" * 30)

for combinacion in combinaciones:
    valores = {proposiciones[i]: combinacion[i] for i in range(len(proposiciones))}
    resultado = eval(expresion_logica, valores)
    
    # Formatear la salida
    combinacion_str = " ".join([f"{proposiciones[i]}={val}" for i, val in enumerate(combinacion)])
    print(f"{combinacion_str.ljust(13)} | {resultado}")

