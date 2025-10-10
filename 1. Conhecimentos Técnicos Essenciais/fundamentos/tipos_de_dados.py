# Aqui estão os principais tipos de dados que o Python suporta nativamente.

numero = 10 # int
texto = "Olá" # str
decimal = 3.14 # float
valores = [5, 1, 2, 3, 3] # list
dicionario = {"chave": "valor"} # dict
booleano = True # bool
tupla = (5, 1, 2, 3, 3) # tuple
conjunto = {5, 3, 1, 2, 3} # set
nulo = None # NoneType
byte = b'bytes' # bytes
byte_array = bytearray(b'abcdefg') # bytearray

# Imprimindo os dados e seus tipos
print(numero, type(numero))
print(texto, type(texto))
print(decimal, type(decimal))
print(valores, type(valores))
print(dicionario, type(dicionario))
print(booleano, type(booleano))
print(tupla, type(tupla))
print(conjunto, type(conjunto))
print(nulo, type(nulo))
print(byte, type(byte))
print(byte_array, type(byte_array))

# Atribuindo novos valores aos tipos mutáveis
numero += numero
texto = texto + " Mundo"
decimal = decimal * 2
valores.append("novo valor")
dicionario["nova_chave"] = "novo_valor"
booleano = False
tupla = tupla + ("texto", 4.56) # Tuplas são imutáveis, mas podemos criar uma nova
conjunto.add("novo elemento")
nulo = "agora não é mais nulo"
byte_array[0] = byte[4] # Modificando os bytes
byte_array[1] = byte[3]
byte_array[2] = byte[2]
byte_array[3] = byte[1]
byte_array[4] = byte[0]

# Imprimindo os dados e seus tipos após modificações
print("\nApós modificações:")
print(numero, type(numero))
print(texto, type(texto))
print(decimal, type(decimal))
print(valores, type(valores))
print(dicionario, type(dicionario))
print(booleano, type(booleano))
print(tupla, type(tupla))
print(conjunto, type(conjunto))
print(nulo, type(nulo))
print(byte, type(byte))
print(byte_array, type(byte_array))