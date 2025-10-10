# Em Python, classes são estruturas que permitem criar seus próprios tipos de dados, 
# agrupando dados (atributos) e comportamentos (métodos) em um só lugar.
# Elas são a base da programação orientada a objetos.

# Definição básica de classe
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome  # Atributo de instância
        self.idade = idade  # Atributo de instância

    def apresentar(self):  # Método de instância
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

# Criando uma instância (objeto) da classe Pessoa
pessoa1 = Pessoa("João", 25)
pessoa1.apresentar() # Saída: Olá, meu nome é João e tenho 25 anos.