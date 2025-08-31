# programa1_busqueda_matriz.py

from typing import List, Optional, Tuple

Matrix = List[List[int]]

def buscar_en_matriz(matriz: Matrix, valor: int) -> Optional[Tuple[int, int]]:
    """
    Busca 'valor' en la matriz 2D y devuelve (fila, columna) si lo encuentra.
    Si no se encuentra, devuelve None.
    """
    for i, fila in enumerate(matriz):
        for j, elem in enumerate(fila):
            if elem == valor:
                return i, j
    return None


def main():
    # Matriz 3x3 de ejemplo (puedes cambiarla libremente)
    matriz = [
        [4, 7, 1],
        [9, 3, 5],
        [2, 8, 6]
    ]

    print("Matriz:")
    for fila in matriz:
        print(fila)

    # Valor a buscar (cámbialo para probar)
    valor = 5

    resultado = buscar_en_matriz(matriz, valor)
    if resultado is not None:
        i, j = resultado
        print(f"\n✅ El valor {valor} SÍ se encontró en la posición (fila={i}, columna={j}).")
    else:
        print(f"\n❌ El valor {valor} NO se encontró en la matriz.")


if __name__ == "__main__":
    main()
