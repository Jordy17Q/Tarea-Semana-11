def bubble_sort(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n-i-1):
            if fila[j] > fila[j+1]:
                fila[j], fila[j+1] = fila[j+1], fila[j]
    return fila

matriz = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

fila_a_ordenar = 1  # Índice de la fila a ordenar (0, 1 o 2)
print("Matriz original:")
for fila in matriz:
    print(fila)

matriz[fila_a_ordenar] = bubble_sort(matriz[fila_a_ordenar])

print("\nMatriz después de ordenar la fila:")
for fila in matriz:
    print(fila)
