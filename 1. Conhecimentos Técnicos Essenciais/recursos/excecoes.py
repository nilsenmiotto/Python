# Principais exceções embutidas:
# ZeroDivisionError – divisão por zero
# ValueError – valor inválido
# TypeError – tipo de dado incorreto
# IndexError – índice fora do intervalo
# KeyError – chave não encontrada em dicionário
# FileNotFoundError – arquivo não encontrado

try:
    resultado = 10 / 0 # ZeroDivisionError
    valor = int("abc") # ValueError
    soma = "2" + 3 # TypeError
    lista = [1, 2, 3]
    item = lista[5] # IndexError
    dicionario = {"chave": "valor"}
    valor = dicionario["outra_chave"] # KeyError
    with open("arquivo_inexistente.txt", "r") as arquivo: # FileNotFoundError
        conteudo = arquivo.read()


except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")
except ValueError:
    print("Erro: valor inválido para conversão.")
except TypeError:
    print("Erro: tipo de dado incorreto.")
except FileNotFoundError:
    print("Erro: arquivo não encontrado.")
except Exception as e:
    print(f"Erro genérico: {e}")
else:
    print("Tudo ok.")
finally:
    print("Operação finalizada.")

