# Funções internas (built-in) mais usadas em Python:
# print()      – exibe informações na tela
# len()        – retorna o tamanho de uma sequência
# type()       – mostra o tipo de um objeto
# range()      – gera uma sequência de números
# input()      – lê dados do usuário
# int(), float(), str() – conversão de tipos
# list(), dict(), set(), tuple() – criação de coleções
# sum()        – soma elementos de uma sequência numérica
# max(), min() – maior e menor valor de uma sequência
# sorted()     – retorna uma lista ordenada
# enumerate()  – itera com índice e valor
# zip()        – combina elementos de várias sequências
# map(), filter() – processamento funcional de coleções
# isinstance() – verifica o tipo de um objeto
# any(), all() – verifica condições em coleções
# round()      – arredonda um número
# chr(), ord() – conversão entre caracteres e códigos Unicode
# format()     – formata valores em strings
# eval()       – executa uma string como código Python (use com cuidado)
# iter()       – cria um iterador a partir de um objeto iterável
# next()       – obtém o próximo item de um iterador

verifica_boleano = True
if(type(verifica_boleano) == bool):
    print("É um booleano!")

texto = "Python é muito bom!"
if(type(texto) == str):
    print(texto.split(" "))

for numeros in range(10, 100, 10):
    print(numeros)

#input_usuario = input("Qual o seu nome?\n")
#print("Olá,", input_usuario)

inteiro = int("10")
flutuante = float("10.5")
string = str(10)
print(inteiro, flutuante, string)

minha_lista = list((1, 2, 3))
meu_dicionario = dict(chave1="valor1", chave2="valor2")
meu_conjunto = set([1, 2, 3])
minha_tupla = tuple((1, 2, 3))
print(minha_lista, meu_dicionario, meu_conjunto, minha_tupla)

soma = sum(minha_lista)
print("A soma dos elementos da lista é:", soma)

maior = max(minha_tupla)
print("O maior elemento da tupla é:", maior)

menor = min(meu_conjunto)
print("O menor elemento do conjunto é:", menor)

desordenado = [3, 1, 4, 2]
ordenado = sorted(desordenado)# retorna uma nova lista ordenada
print("Lista desordenada:", desordenado)
print("Lista ordenada:", ordenado)

#enumerate cria um indice para cada elemento da lista
for i, valor in enumerate(ordenado):
   print(f"Índice: {i}, Valor: {valor}")
   ordenado[i] = valor * 10
print("Lista ordenada modificada:", ordenado)

#zip combina duas listas em uma lista de tuplas
nomes = ["Ana", "João", "Maria", "Pedro"]
idades = [25, 30, 22, 28]
pessoas = list(zip(nomes, idades))
print(pessoas) # Saída: [('Ana', 25), ('João', 30), ('Maria', 22), ('Pedro', 28)]

for nome, idade in zip(nomes, idades):
    print(f"{nome} tem {idade} anos.")

#map aplica uma função a todos os elementos de uma lista
def quadrado(x):
    return x * x

numeros = [1, 2, 3, 4, 5]
quadrados = list(map(quadrado, numeros))
print("Números:", numeros)
print("Quadrados:", quadrados)

def inverte_string(s):
    return s[::-1]

nomes_invertidos = list(map(inverte_string, nomes))
print("Nomes:", nomes)
print("Nomes invertidos:", nomes_invertidos)

#filter filtra elementos de uma lista com base em uma condição
def strings_pequenas(s):
    return len(s) <= 3

nomes_pequenos = list(filter(strings_pequenas, nomes))
print("Nomes pequenos:", nomes_pequenos)

if(isinstance(10, int)):
    print("É um inteiro!")


lista = [0, False, 3, ""]

if(isinstance(lista, (list, tuple, set))):
    print("É uma lista, tupla ou conjunto!")

print(any(lista))  # Saída: True (porque 3 é verdadeiro)
print(all(lista))  # Saída: False (porque 0, False e "" são falsos)

print(round(3.14159, 2))  # Saída: 3.14

#As funções chr() e ord() em Python servem para conversão entre caracteres e seus códigos Unicode (ou ASCII):
print(chr(65))  # Saída: 'A'
print(chr(8364))  # Saída: '€'
print(ord('A'))  # Saída: 65
print(ord('€'))  # Saída: 8364

valor = 3.14159
print("valor formatado: {:.2f}".format(valor))  # Saída: valor formatado: 3.14

nome = "Ana"
idade = 25
mensagem = "Meu nome é {0} e tenho {1} anos.".format(nome, idade)
print(mensagem)  # Saída: Meu nome é Ana e tenho 25 anos.
mensagem2 = "Meu nome é {nome} e tenho {idade} anos.".format(nome=nome, idade=idade)
print(mensagem2)  # Saída: Meu nome é Ana e tenho 25 anos

#eval executa uma expressão Python passada como string
# Cuidado ao usar eval com entradas não confiáveis, pois pode executar código malicioso
expressao = "2 + 3 * 4"
resultado = eval(expressao)
print(resultado)  # Saída: 14

#iter() transforma um objeto iterável em um iterador, que pode ser consumido elemento por elemento.
lista = [1, 2, 3]
it = iter(lista)
print(it)

#A função next() em Python é usada para obter o próximo item de um iterador.
numeros = iter([10, 20, 30])
print(next(numeros))  # Saída: 10
print(next(numeros))  # Saída: 20
print(next(numeros))  # Saída: 30
print(next(numeros, "Fim"))  # Saída: Fim (evita StopIteration)

