def es_seguro(tablero, fila, columna, n):
    # Verifica si es seguro colocar una reina en la fila y columna dadas
    # Verifica la misma columna
    for i in range(fila):
        if tablero[i][columna] == 1:
            return False

    # Verifica la diagonal izquierda superior
    i, j = fila, columna
    while i >= 0 and j >= 0:
        if tablero[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Verifica la diagonal derecha superior
    i, j = fila, columna
    while i >= 0 and j < n:
        if tablero[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def resolver_n_reinas(n):
    tablero = [[0] * n for _ in range(n)]

    def resolver_recursivo(fila):
        if fila == n:
            # Se encontró una solución
            for fila in tablero:
                print(fila)
            print()
        else:
            for columna in range(n):
                if es_seguro(tablero, fila, columna, n):
                    tablero[fila][columna] = 1
                    resolver_recursivo(fila + 1)
                    tablero[fila][columna] = 0

    resolver_recursivo(0)

n = 8  # Cambia el valor de 'n' para encontrar soluciones para diferentes tamaños del tablero
resolver_n_reinas(n)

