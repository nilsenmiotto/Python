soma = lambda x, y: x + y
print(soma(2, 3))  # Saída: 5

# Map retorna uma lista com os resultados da aplicação da função a cada item do iterável
numeros = [1, 2, 3, 4]
dobrados = list(map(lambda x: x * 2, numeros))
print(dobrados)  # Saída: [2, 4, 6, 8]

# Filter retorna uma lista com os itens do iterável que retornam True na função
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # Saída: [2, 4]

lower = lambda nomes: nomes.lower()
nomes = ["Ana", "Zuleide", "Pedro", "Marcos", "Eloisa"]
ordenados = sorted(nomes, key=lower)
print(ordenados)  # Saída: ['Ana', 'Eloisa', 'Marcos', 'Pedro', 'Zuleide']

reverso = sorted(nomes, key=lower, reverse=True)
print(reverso)  # Saída: ['Zuleide', 'Pedro', 'Marcos', 'Eloisa', 'Ana']