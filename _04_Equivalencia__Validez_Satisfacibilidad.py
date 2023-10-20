
import itertools
import sympy

# Define las variables proposicionales y la fórmula lógica
variables = sympy.symbols('p q r')
formula = sympy.Eq((variables[0] & variables[1]) | ~variables[2], variables[2])

# 1. Verificar la equivalencia
equivalente = formula.equals(True)

# 2. Verificar la validez
valido = formula.simplify().equals(True)

# 3. Verificar la satisfacibilidad
satisfacible = False
for valores in itertools.product([True, False], repeat=len(variables)):
    sustitucion = {variables[i]: valores[i] for i in range(len(variables))}
    if formula.subs(sustitucion):
        satisfacible = True
        break

# Resultados
print("Fórmula Lógica:", formula)
print("1. Equivalente a Verdadero:", equivalente)
print("2. Válida (siempre verdadera):", valido)
print("3. Satisfacible (al menos una asignación verdadera):", satisfacible)
