# Generators são funções especiais em Python que usam a palavra-chave
# yield para retornar valores um de cada vez, criando um iterador.
# Eles permitem gerar (produzir) valores sob demanda, economizando memória,
# pois não armazenam todos os valores de uma vez.
# São úteis para trabalhar com grandes volumes de dados ou fluxos infinitos.

def contador():
    for i in range(3):
        yield i

for numero in contador():
    print(numero)


lista = ["Ameixa", "Banana", "Cereja"]

# Apesar do gerador_de_espacos ter um loop interno e a sua execução ser executada com um loop for,
# ele ainda é mais eficiente em termos de memória porque retorna um valor por vez com yield
# no final das contas é como se existisse um loop for externo que consome os valores gerados um a um.

def gerador_de_espacos(lista):
    for item in lista:
        resultado = " ".join(item.upper())
        yield resultado

for item in gerador_de_espacos(lista):
    print(item)

for item in gerador_de_espacos(["Kombi", "Fusca", "Brasília"]):
    print(item)