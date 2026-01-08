import json
from pathlib import Path

arquivo = Path(__file__).resolve().parent / "dados_saida.json"

# Escrevendo dados em JSON
dados = {
    "nome": "João",
    "idade": 30,
    "cidade": "São Paulo",
    "habilidades": ["Python", "JavaScript", "SQL"]
}

with arquivo.open("w", encoding="utf-8") as buffer:
    json.dump(dados, buffer, indent=4, ensure_ascii=False)
    

# Lendo dados de um arquivo JSON
with arquivo.open("r", encoding="utf-8") as buffer:
    dados_carregados = json.load(buffer)
    print(dados_carregados)

# Acessando dados específicos
print(f"Nome: {dados_carregados['nome']} Habilidades: {', '.join(dados_carregados['habilidades'])}")

# Atualizando dados no arquivo JSON
dados_carregados["cidade"] = "Marialva"
dados_carregados["habilidades"].remove("JavaScript")
dados_carregados["habilidades"].append("C")
dados_carregados["empregado"] = True

with arquivo.open("w", encoding="utf-8") as buffer:
    json.dump(dados_carregados, buffer, indent=4, ensure_ascii=False)

# Verificando as alterações
with arquivo.open("r", encoding="utf-8") as buffer:
    dados_atualizados = json.load(buffer)
    print(dados_atualizados)

print("\n\nExemplos de conversão entre JSON e dicionário Python:")
# Convertendo string JSON para dicionário Python
json_string = '{"produto": "Notebook", "preco": 2500.75, "em_estoque": true}'
produto_dict = json.loads(json_string)
print(produto_dict)

# Convertendo dicionário Python para string JSON
novo_json_string = json.dumps(produto_dict, indent=4)
print(f"String JSON formatada:\n{novo_json_string}")