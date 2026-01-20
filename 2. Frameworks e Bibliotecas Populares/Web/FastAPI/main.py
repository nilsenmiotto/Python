from typing import Optional, Union
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from enum import Enum
import json

app = FastAPI()

with open("dados_produtos.json", "r", encoding="utf-8") as file:
    produtos_data = json.load(file)


class Categoria(Enum):
    GRAOS = "Grãos"
    LATICINIOS = "Laticínios"
    MASSAS = "Massas"
    LANCHES = "Lanches"
    OLEOS = "Óleos"
    BEBIDAS = "Bebidas"
    HIGIENE = "Higiene"
    LIMPEZA = "Limpeza"

class Produto_NEW(BaseModel):
    nome: str
    categoria: Categoria
    preco: float
    estoque: int
    unidade: str
    marca: str

class Produto_UPD(BaseModel):
    id: int
    nome: Optional[str] = None
    categoria: Optional[Categoria] = None
    preco: Optional[float] = None
    estoque: Optional[int] = None
    unidade: Optional[str] = None
    marca: Optional[str] = None


@app.get("/")
def read_root():

    dados = "Consulte a documentação em http://127.0.0.1:8000/docs"
    return JSONResponse(content=dados, media_type="application/json")


@app.get("/produtos/")
def retorna_produtos(categoria: Categoria = None, skip: int = 0, limit: int = 10):

    if categoria == None:
        filtro_por_categoria = produtos_data
    else:
        filtro_por_categoria = list(filter(lambda produto: produto["categoria"] == categoria.value, produtos_data))

    dados = filtro_por_categoria[skip : skip + limit]

    if not dados:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return JSONResponse(content=dados, media_type="application/json")


@app.get("/produtos/{id}")
def retorna_produto(id: int):

    dados = next((produto for produto in produtos_data if produto.get("id") == id), None)
    
    if not dados:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return JSONResponse(content=dados, media_type="application/json")


@app.put("/produtos/")
def cadastra_produto(produto: Produto_NEW):

    if not isinstance(produto.categoria, Categoria):
        raise HTTPException(status_code=400, detail="Categoria inválida")
    
    if not produto.preco:
        raise HTTPException(status_code=400, detail="Preço inválido")

    if not produto.estoque:
        raise HTTPException(status_code=400, detail="Estoque inválido")
    
    for encontrado in produtos_data:
        if encontrado.get("nome") == produto.nome and encontrado.get("categoria") == produto.categoria.value:
            raise HTTPException(status_code=400, detail="O produto já existe")

    id = max((item.get("id", 0) for item in produtos_data), default=0) + 1
    produto_recebido = produto.model_dump(mode="json")
    produto_recebido.update({"id" : id})
    produtos_data.append(produto_recebido)
    
    dados = "Produto cadastrado com a ID=" + str(id)
    return JSONResponse(content=dados, media_type="application/json")


@app.patch("/produtos/")
def atualiza_produto(produto: Produto_UPD):

    if not produto.id:
        raise HTTPException(status_code=404, detail="ID do produto não informada")
    
    produto_recebido = produto.model_dump(mode="json", exclude_none=True)
    dados = ""

    for pos, encontrado in enumerate(produtos_data):
        if encontrado.get("id") == produto.id:
            produtos_data[pos].update(produto_recebido)
            dados = "Produto atualizado com sucesso"
            break

    if not dados:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return JSONResponse(content=dados, media_type="application/json")

@app.delete("/produtos/{id}")
def deleta_produto(id : int):

    if not id:
        raise HTTPException(status_code=404, detail="ID do produto não informada")
    
    dados = ""

    for pos, encontrado in enumerate(produtos_data):
        if(encontrado.get("id") == id):
            produtos_data.pop(pos)
            dados = "Produto deletado com sucesso"
            break
    
    if not dados:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return JSONResponse(content=dados, media_type="application/json")


