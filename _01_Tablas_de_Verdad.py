#Sintaxis y Sem�ntica: Tablas de Verdad

import itertools

# Definici�n de las variables y operadores
variables = ["p", "q"]
operators = ["->"]  # Operador condicional (implicaci�n)

# Funci�n para evaluar una proposici�n condicional
def evaluar_proposicion(p, q):
    return (not p) or q

# Encabezado de la tabla de verdad
print(f"{'p':<2} {'q':<2} {'p -> q'}")

# Generar y evaluar todas las combinaciones posibles de p y q
for p, q in itertools.product([True, False], repeat=2):
    resultado = evaluar_proposicion(p, q)
    print(f"{p:<2} {q:<2} {resultado}")

