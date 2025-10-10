# Estruturas de Controle em Python

# Estruturas condicionais
idade = 20
if idade < 18:
    print("Menor de idade")
elif idade >= 18 and idade < 65:
    print("Adulto")
else:
    print("Idoso")

# Estruturas de repetição
for i in range(5):
    print("Iteração:", i)

contador = 0
while contador < 5:
    print("Contador:", contador)
    contador += 1

# Exemplo de uso de break e continue
for letra in "Python":
    if letra == "t":
        continue  # Pula a letra 't'
    if letra == "o":
        break  # Sai do loop ao encontrar 'o'
    print("Letra:", letra)

# Exemplo com listas
frutas = ["maçã", "banana", "cereja"]
for fruta in frutas:
    print("Fruta:", fruta)

# Exemplo com dicionários
pessoa = {"nome": "João", "idade": 25, "cidade": "São Paulo"}
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")
