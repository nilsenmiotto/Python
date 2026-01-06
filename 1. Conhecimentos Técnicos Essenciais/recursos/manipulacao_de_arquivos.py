"""
Manipulação de arquivos em Python - exemplos comuns
- Uso recomendado: contexto `with` para abrir arquivos (fecha automaticamente).
- Modos: 'r' (read), 'w' (write, sobrescreve), 'a' (append), 'rb'/'wb' (binário).
- Encoding: especifique encoding='utf-8' para arquivos de texto.
- Pathlib facilita operações com caminhos.
"""

from pathlib import Path

diretorio_script = Path(__file__).resolve().parent # ..\1.Conhecimentos Técnicos Essenciais\recursos
diretorio_raiz = diretorio_script.parent.parent  # ..\
diretorio_arquivos = diretorio_script / "manipulando_arquivos"  # ..\1.Conhecimentos Técnicos Essenciais\recursos\manipulando_arquivos

# Leitura de um arquivo texto
with open(diretorio_raiz / "README.md", 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

# Escrita em um arquivo texto
with open(diretorio_arquivos / "exemplo_saida.txt", 'w', encoding='utf-8') as arquivo:
    arquivo.write("Linha 1\nLinha 2\nLinha 3\n")
    arquivo.write(conteudo)

# Ler linha a linha
def leitura_linha_a_linha():

    with open(diretorio_raiz / 'README.md', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            yield linha.strip()

# muito eficiente para arquivos grandes
print("\nLeitura linha a linha:")
for linha in leitura_linha_a_linha():
    print(linha)

# Leitura e escrita binária
with open(diretorio_arquivos / "Album anos 80.png", 'rb') as arquivo_binario:
    dados = arquivo_binario.read()
    print(f"\nArquivo binário lido: {len(dados)} bytes")

    with open(diretorio_arquivos / "Album anos 80 saida.png", 'wb') as copia:
        copia.write(dados)
        print("Cópia do arquivo binário criada.")