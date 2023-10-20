#Sintaxis y Semántica: Tablas de Verdad

import itertools

# Definición de las variables y operadores
variables = ["p", "q"]
operators = ["->"]  # Operador condicional (implicación)

# Función para evaluar una proposición condicional
def evaluar_proposicion(p, q):
    return (not p) or q

# Encabezado de la tabla de verdad
print(f"{'p':<2} {'q':<2} {'p -> q'}")

# Generar y evaluar todas las combinaciones posibles de p y q
for p, q in itertools.product([True, False], repeat=2):
    resultado = evaluar_proposicion(p, q)
    print(f"{p:<2} {q:<2} {resultado}")

