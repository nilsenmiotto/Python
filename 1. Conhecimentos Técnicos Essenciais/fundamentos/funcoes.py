# Definição básica de função
def minha_funcao():
    print("Função chamada!")

minha_funcao()

def soma(valor1, valor2):
    return valor1 + valor2

resultado = soma(5, 3)
print("Resultado da soma:", resultado)

# Função com valor padrão
def saudacao(nome="Mundo"):
    print(f"Olá, {nome}")

saudacao()          # Usa o valor padrão
saudacao("Isabela")  # Usa o valor fornecido

# Função com argumentos nomeados
def exibir_dados(nome, idade, cidade):
    print(f"{nome}, {idade} anos, mora em {cidade}")

exibir_dados("Ana", 30, "Recife") # Argumentos na ordem
exibir_dados(idade=25, nome="Pedro", cidade="Salvador") # Argumentos nomeados fora de ordem
exibir_dados("Lucas", cidade="Fortaleza", idade=28) # Mistura de posicional e nomeado

# Função com número variável de argumentos
def exibe_parametros(*parametros):
    for parametro in parametros:
        print(parametro)
    print("Total de parâmetros:", len(parametros))

exibe_parametros("Ana", "Bruno", "Carla")
exibe_parametros(1, 2, 3, 4, 5)
exibe_parametros()  # Sem argumentos
exibe_parametros(resultado, minha_funcao(), soma(1, 2))  # Passando funções como argumentos
# Quando eu passo minha_funcao() como argumento, 
# a função é executada durante a chamada de exibe_parametros, 
# e o valor retornado (None) é passado como argumento porque a função não retorna valores.

# Função com argumentos variáveis nomeados
def mostrar_info(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

mostrar_info(cpu="Intel", ram="16GB", ssd="512GB")
mostrar_info(usuario="joao", email="joao@example.com", ativo=True, avisos=5)