# Principais métodos por tipo de variável em Python:
#
# str (strings):
# - join(), split(), replace(), upper(), lower(), capitalize(), title(), strip(), find(), startswith(), endswith(), format()
#
texto = "Aprender programação em Python exige prática constante, leitura de código e exercícios estruturados."
texto_concatenado = " ".join([texto, "Vamos", "estudar", "juntos!"])
print(texto_concatenado)

palavras = texto.split(" ")
print(palavras)

texto_modificado = texto.replace("programação", "desenvolvimento")
print(texto_modificado)

print(texto.upper()) # converte para maiúsculas
print(texto.lower()) # converte para minúsculas
print(texto.capitalize()) # converte o primeiro caractere para maiúscula
print(texto.title()) # converte o primeiro caractere de cada palavra para maiúscula
print(texto.strip()) # remove espaços em branco no início e no fim
print(texto.find("Python")) # encontra a posição da substring
print(texto.startswith("Aprender")) # verifica se começa com a substring
print(texto.endswith("estruturados.")) # verifica se termina com a substring
formatted_text = "Olá, {}! Bem-vindo ao curso de {}.".format("João", "Python") 
print(formatted_text)

# list (listas):
# - append(), extend(), insert(), remove(), pop(), index(), count(), sort(), reverse(), copy(), clear()

minha_lista = [5, 2, 9, 1]
print("Lista original:", minha_lista)

minha_lista.append(7) # adiciona 7 ao final da lista
print("Após append:", minha_lista)

minha_lista.extend([3, 4]) # adiciona múltiplos elementos ao final
print("Após extend:", minha_lista)

minha_lista.insert(2, 8) # insere 8 na posição 2
print("Após insert:", minha_lista)

minha_lista.remove(1) # remove o primeiro elemento com valor 1
print("Após remove:", minha_lista)

removido = minha_lista.pop() # remove e retorna o último elemento
print("Após pop:", minha_lista, "| Removido:", removido)

print("Índice de 9:", minha_lista.index(9)) # encontra o índice de 9
print("Contagem do item 2:", minha_lista.count(2)) # conta quantas vezes 2 aparece

minha_lista.sort() # ordena a lista
print("Após sort:", minha_lista)

minha_lista.reverse() # inverte a ordem da lista
print("Após reverse:", minha_lista)

copia_lista = minha_lista.copy() # cria uma cópia da lista
print("Cópia da lista:", copia_lista)

minha_lista.clear() # limpa todos os elementos da lista
print("Após clear:", minha_lista)


# dict (dicionários):
# - keys(), values(), items(), get(), update(), pop(), popitem(), setdefault(), copy(), clear()

meu_dicionario = {"nome": "Ana", "idade": 25, "cidade": "São Paulo"}
print("Dicionário original:", meu_dicionario)
print("Chaves:", meu_dicionario.keys()) # obtém as chaves
print("Valores:", meu_dicionario.values()) # obtém os valores
print("Itens:", meu_dicionario.items()) # obtém os itens (chave, valor)
print("Nome:", meu_dicionario.get("nome")) # obtém o valor da chave "nome"

meu_dicionario.update({"idade": 26, "profissão": "Engenheira"}) # atualiza e adiciona itens
print("Após update:", meu_dicionario)

removido = meu_dicionario.pop("cidade") # remove e retorna o valor da chave "cidade"
print("Após pop:", meu_dicionario, "| Removido:", removido)

removido_item = meu_dicionario.popitem() # remove e retorna o último item adicionado
print("Após popitem:", meu_dicionario, "| Removido item:", removido_item)

meu_dicionario.setdefault("pais", "Brasil") # adiciona a chave "pais" se não existir
print("Após setdefault:", meu_dicionario)

copia_dict = meu_dicionario.copy() # cria uma cópia do dicionário
print("Cópia do dicionário:", copia_dict)

meu_dicionario.clear() # limpa todos os itens do dicionário
print("Após clear:", meu_dicionario)


# set (conjuntos):
# - add(), update(), remove(), discard(), pop(), union(), intersection(), difference(), symmetric_difference(), copy(), clear()

meu_conjunto = {1, 2, 3}
print("Conjunto original:", meu_conjunto)

meu_conjunto.add(4) # adiciona 4 ao conjunto
print("Após add:", meu_conjunto)

meu_conjunto.update([5, 6]) # adiciona múltiplos elementos
print("Após update:", meu_conjunto)

meu_conjunto.remove(2) # remove o elemento 2
print("Após remove:", meu_conjunto)

meu_conjunto.discard(10) # tenta remover 10 (não gera erro se não existir)
print("Após discard:", meu_conjunto)

removido = meu_conjunto.pop() # remove e retorna um elemento aleatório
print("Após pop:", meu_conjunto, "| Removido:", removido)

outro_conjunto = {4, 5, 6, 7}
print("União:", meu_conjunto.union(outro_conjunto)) # união dos conjuntos
print("Interseção:", meu_conjunto.intersection(outro_conjunto)) # retorna elementos comuns
print("Diferença:", meu_conjunto.difference(outro_conjunto)) # elementos em meu_conjunto mas não em outro_conjunto
print("Diferença simétrica:", meu_conjunto.symmetric_difference(outro_conjunto)) # elementos em um ou outro, mas não em ambos

copia_set = meu_conjunto.copy() # cria uma cópia do conjunto
print("Cópia do conjunto:", copia_set)

meu_conjunto.clear() # limpa todos os elementos do conjunto
print("Após clear:", meu_conjunto)


# tuple (tuplas):
# - count(), index()

minha_tupla = (1, 2, 3, 2, 4)
print("Tupla original:", minha_tupla)
print("Contagem do item 2:", minha_tupla.count(2)) # conta quantas vezes 2 aparece
print("Índice de 3:", minha_tupla.index(3)) # encontra o índice de 3

