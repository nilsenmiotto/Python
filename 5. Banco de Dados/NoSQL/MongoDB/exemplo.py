from pymongo import MongoClient, errors

MONGO_URI = "mongodb://localhost:27017"

client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)

#testa conexão
try:
    client.admin.command("ping")
    print("Conectado ao MongoDB!")
except Exception as erro:
    print(f"Erro ao conectar: {erro}")
    raise

db = client["meu_banco"]
colecao = db["usuarios"]
filtro = {"usuario": "alice"}

doc = colecao.find_one(filtro)
print(doc)

update = {"$set": {"idade": 31, "cidade": "Marialva"}}
resultado = colecao.update_one(filtro, update, upsert=True)
print("encontrado:", resultado.matched_count, "modificado:", resultado.modified_count)

novo_usuario = {"usuario": "maria", "senha": "NovaSenha", "nome": "Maria Souza", "cidade": "Marialva", "habilitado": False}
try:
    colecao.insert_one(novo_usuario)
    print("Usuário inserido")
except errors.DuplicateKeyError:
    print("Usuário já existe")


colecao.update_many(
    {"email": {"$exists": False}},
    {"$set": {"email": ""}}
)

# pipelines de agregação
pipeline = [
    {"$match": {"habilitado": True}},
    {"$group": {"_id": "$cidade", "total": {"$sum": 1}}},
    {"$sort": {"total": -1}},
]

for doc in colecao.aggregate(pipeline):
    print(doc)

# remoção de documentos
colecao.delete_one({"usuario": "maria"})

filtro = {"usuario": "alice"}
remove = {"$unset": {"cidade": "", "idade": ""}}
colecao.update_many(filtro, remove)

client.close()