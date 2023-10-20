import sympy

# Definici�n de variables proposicionales
p, q, r = sympy.symbols('p q r')

# Definici�n de la f�rmula l�gica
formula = (p | ~q) & (~p | q | r) & (p | ~r)

# Convertir la f�rmula en su Forma Normal Conjuntiva (FNC)
fnc = sympy.to_cnf(formula)

# Mostrar la F�rmula Original
print("F�rmula Original:", formula)

# Mostrar la F�rmula en Forma Normal Conjuntiva (FNC)
print("Forma Normal Conjuntiva (FNC):", fnc)

# Resoluci�n
resolver = sympy.satisfiable(fnc)
print("�La FNC es satisfacible (resoluble)?:", resolver)

