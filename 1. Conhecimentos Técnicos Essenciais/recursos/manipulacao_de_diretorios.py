from pathlib import Path

diretorio_script = Path(__file__).resolve().parent # ..\1.Conhecimentos Técnicos Essenciais\recursos
diretorio_arquivos = diretorio_script / "manipulando_arquivos"  # ..\1.Conhecimentos Técnicos Essenciais\recursos\manipulando_arquivos

def criar_diretorio(nome_diretorio):
    novo_diretorio = diretorio_arquivos / nome_diretorio
    novo_diretorio.mkdir(exist_ok=True)
    print(f"Diretório criado: {novo_diretorio}")

criar_diretorio("teste_diretorio")

def listar_arquivos(diretorio, extensao=None):

    if(extensao):
        print(list(diretorio.glob(f"*.{extensao}")))
    else:
        print(list(diretorio.iterdir()))

listar_arquivos(diretorio_arquivos)

def mover_diretorio(origem, destino):

    diretorio_origem = diretorio_arquivos / origem
    diretorio_destino = diretorio_arquivos / destino
    diretorio_origem.rename(diretorio_destino)
    print(f"Diretório movido de {origem} para {destino}")

mover_diretorio("teste_diretorio", "diretorio_renomeado")

# Verificar existência
def existe(caminho):
    return caminho.exists()

existe(diretorio_arquivos / "diretorio_renomeado")

# Remover arquivo
def remover_arquivo(caminho):
    if caminho.exists():
        caminho.unlink()

remover_arquivo(diretorio_arquivos / "exemplo_saida.txt")

# Remover diretório vazio
def remover_diretorio_vazio(caminho):
    if caminho.exists():
        caminho.rmdir()

remover_diretorio_vazio(diretorio_arquivos / "diretorio_renomeado") 