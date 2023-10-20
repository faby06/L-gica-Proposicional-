# Definici�n de una base de reglas
reglas = {
    'regla1': (('p', 'q'), 'r'),  # Si p y q, entonces r
    'regla2': ('s', 'p'),        # Si s, entonces p
    'regla3': ('t', 'q'),        # Si t, entonces q
}

# Definici�n de hechos iniciales
hechos = ['s', 't']

# Funci�n para el encadenamiento hacia adelante
def encadenamiento_hacia_adelante(reglas, hechos):
    nueva_informacion = True
    while nueva_informacion:
        nueva_informacion = False
        for regla, (antecedentes, consecuente) in reglas.items():
            if all(hecho in hechos for hecho in antecedentes) and consecuente not in hechos:
                hechos.append(consecuente)
                nueva_informacion = True
                print(f"Se aplic� {regla}: {', '.join(antecedentes)} -> {consecuente}")
    return hechos

# Funci�n para el encadenamiento hacia atr�s
def encadenamiento_hacia_atras(reglas, objetivo):
    if objetivo in hechos:
        print(f"El objetivo {objetivo} ya se encuentra en los hechos iniciales.")
        return True

    for regla, (antecedentes, consecuente) in reglas.items():
        if objetivo == consecuente:
            print(f"Se intenta demostrar {objetivo} usando {', '.join(antecedentes)} (regla {regla}).")
            demostrado = all(encadenamiento_hacia_atras(reglas, antecedente) for antecedente in antecedentes)
            if demostrado:
                print(f"Se demostr� {objetivo} usando {', '.join(antecedentes)} (regla {regla}).")
                return True

    print(f"No se pudo demostrar {objetivo}.")
    return False

# Ejemplo de encadenamiento hacia adelante
hechos_finales = encadenamiento_hacia_adelante(reglas, hechos)
print("Hechos finales:", hechos_finales)

# Ejemplo de encadenamiento hacia atr�s
objetivo = 'r'
print(f"Intentando demostrar {objetivo} mediante encadenamiento hacia atr�s:")
encadenamiento_hacia_atras(reglas, objetivo)

