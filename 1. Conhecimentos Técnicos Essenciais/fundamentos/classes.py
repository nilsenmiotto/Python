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

# Outra classe para demonstrar herança
class Curso:
    def __init__(self, nome_curso, duracao):
        self.nome_curso = nome_curso  # Atributo de instância
        self.duracao = duracao  # Atributo de instância
    
    def detalhes_curso(self):  # Método de instância
        print(f"Curso: {self.nome_curso}, Duração: {self.duracao} meses.")

# Herança: criando uma classe que herda de outra
class Estudante(Pessoa, Curso):
    def __init__(self, nome, idade, nome_curso, duracao):
        Pessoa.__init__(self, nome, idade)  # Chama o construtor da classe Pessoa
        Curso.__init__(self, nome_curso, duracao)  # Chama o construtor da classe Curso

    def apresentar(self):  # Sobrescrevendo o método apresentar
        super().apresentar()  # Chama o método da classe base
        print(f"Estou estudando {self.nome_curso}.")


# Criando uma instância da classe Estudante
estudante1 = Estudante("Maria", 22, "Engenharia", 48)
estudante1.apresentar()
estudante1.detalhes_curso()