# programa2_ordenacion_matriz.py

from typing import List
import copy

Matrix = List[List[int]]

def bubble_sort(lista: List[int]) -> List[int]:
    """
    Ordena una lista de enteros de forma ascendente usando Bubble Sort.
    Devuelve una NUEVA lista (no modifica la original).
    """
    arr = lista[:]  # copia superficial para no tocar la original
    n = len(arr)
    for i in range(n):
        intercambiado = False
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                intercambiado = True
        if not intercambiado:  # optimización: si no hubo cambios, ya está ordenada
            break
    return arr


def ordenar_fila_de_matriz(matriz: Matrix, indice_fila: int) -> Matrix:
    """
    Devuelve una NUEVA matriz en la que la fila 'indice_fila' está ordenada ascendentemente.
    Las demás filas permanecen iguales.
    """
    if indice_fila < 0 or indice_fila >= len(matriz):
        raise IndexError("El índice de fila está fuera de rango.")

    nueva = copy.deepcopy(matriz)
    nueva[indice_fila] = bubble_sort(nueva[indice_fila])
    return nueva


def main():
    # Matriz 3x3 de ejemplo (puedes cambiarla libremente)
    matriz = [
        [4, 7, 1],
        [9, 3, 5],
        [2, 8, 6]
    ]

    indice_fila = 1  # fila a ordenar (0, 1 o 2 en esta matriz 3x3)

    print("Matriz original:")
    for fila in matriz:
        print(fila)

    matriz_ordenada = ordenar_fila_de_matriz(matriz, indice_fila)

    print(f"\nMatriz con la fila {indice_fila} ordenada ascendentemente:")
    for fila in matriz_ordenada:
        print(fila)


if __name__ == "__main__":
    main()
