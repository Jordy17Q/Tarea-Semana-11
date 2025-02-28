def buscar_valor_matriz(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return f"Valor {valor} encontrado en la posición ({i}, {j})"
    return f"Valor {valor} no encontrado en la matriz"

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

valor_a_buscar = 5
resultado = buscar_valor_matriz(matriz, valor_a_buscar)
print(resultado)
