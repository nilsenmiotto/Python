# Decorators são funções que recebem outra função como argumento e retornam uma nova função, 
# geralmente para adicionar ou modificar funcionalidades sem alterar o código original.
# São usados com o símbolo @ acima da definição da função.

def meu_decorator(func):
    def wrapper():
        print("Antes da função ser chamada.")
        func()
        print("Depois da função ser chamada.")
    return wrapper

@meu_decorator
def diz_ola():
    print("Olá!")

diz_ola()

# Eu descobri que decorators são muito úteis para logging, autenticação, medição de tempo de execução, etc.
def debuga_funcao(func):
    def wrapper(*args, **kwargs):
        print(f"Chamando a função '{func.__name__}' com argumentos {args} e {kwargs}")
        resultado = func(*args, **kwargs)
        print(f"A função '{func.__name__}' retornou {resultado}")
        return resultado
    return wrapper

@debuga_funcao
def soma(a, b):
    return a + b
    

soma(3, 5)

@debuga_funcao
def exibe_info(nome, idade):
    return f"{nome} tem {idade} anos."

exibe_info("Carlos", 29)