import numpy as np

data = np.array([1, 2])
ones = np.ones(2, dtype=int)
print("Data + Ones = ", data + ones)  # Output: [2 3]
print("Data - Ones = ", data - ones)  # Output: [0 1]
print("Data * Ones = ", data * ones)  # Output: [1 2]
print("Data / Ones = ", data / ones)  # Output: [1. 2.]

somando = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Soma dos elementos = ", np.sum(somando))  # Output: 55

somando_matriz = np.array([[1, 2], [3, 4]])
print("Soma do axys 0 = ", np.sum(somando_matriz, axis=0))  # Output: [4 6] colunas
print("Soma do axys 1 = ", np.sum(somando_matriz, axis=1))  # Output: [3 7] linhas

print("Multiplicando por um valor escalar = ", data * 3.1)  # Output: [3.1 6.2]

meu_array = np.array([1, 2, 3, 4, 5])
print("minimo = ", meu_array.min())  # Output: 1
print("maximo = ", meu_array.max())  # Output: 5
print("media = ", meu_array.mean())  # Output: 3.0

minha_matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("minimo da matriz = ", minha_matriz.min())  # Output: 1
print("maximo da matriz = ", minha_matriz.max())  # Output: 9
print("media da matriz = ", minha_matriz.mean())  # Output: 5.0

raw_data = np.array([11, 11, 12, 13, 14, 15, 16, 17, 12, 13, 11, 14, 18, 19, 20])
valores_unicos, indices = np.unique(raw_data, return_index=True)
print("Valores únicos = ", valores_unicos)  # Output: [11 12 13 14 15 16 17 18 19 20]
print("Índices dos valores únicos = ", indices)  # Output: [ 0  2  3  4  5  6  7 12 13 14]

print("Matriz original = ", minha_matriz)
print("Matriz reshapeada (1x9) = ", minha_matriz.reshape(1, 9)) # Output: [[1 2 3 4 5 6 7 8 9]]
print("Matriz reshapeada (3x3) = ", minha_matriz.reshape(3, 3)) # Output: [[1 2 3] [4 5 6] [7 8 9]]
print("Matriz achatada = ", minha_matriz.flatten())  # Output: [1 2 3 4 5 6 7 8 9]
print("Matriz transposta = ", minha_matriz.T)  # Output: [[1 4 7] [2 5 8] [3 6 9]]
print("Matriz reversa = ", np.flip(minha_matriz))  # Output: [[9 8 7] [6 5 4] [3 2 1]]