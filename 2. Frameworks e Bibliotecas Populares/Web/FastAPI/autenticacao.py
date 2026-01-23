from typing import Optional, Annotated
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pwdlib import PasswordHash
from pydantic import BaseModel
from jwt.exceptions import InvalidTokenError
from datetime import datetime, timedelta, timezone
import json
import jwt


app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
password_hash = PasswordHash.recommended()

with open("usuarios.json", "r", encoding="utf-8") as file:
    usuarios_data = json.load(file)
    

# executar com o git bash ou terminal:
# openssl rand -hex 32
CHAVE_SECRETA = "00ac51fe165905ea336962e3c65c5222d60feb6fb2d7bfb0ffd10d7f1716c11f"
ALGORITIMO = "HS256"
TEMPO_EXPIRAR_TOKEN_ACESSO = 30

class Usuario(BaseModel):
    usuario: str
    senha: str
    nome: Optional[str] = None
    email: Optional[str] = None
    habilitado: bool

class Token(BaseModel):
    access_token: str
    token_type: str

class DadosToken(BaseModel):
    usuario: str | None = None

def verificar_senha(senha_simples, senha_hash):
    return password_hash.verify(senha_simples, senha_hash)


def gerar_senha_hash(senha):
    return password_hash.hash(senha)


def recupera_usuario(usuario: str):

    for cada_usuario in usuarios_data:
        if cada_usuario.get("usuario") == usuario:
            senha = cada_usuario.get("senha")
            # Se a senha não parece hash (sem prefixo de hash), gera hash em memória
            if isinstance(senha, str) and not senha.startswith("$"):
                cada_usuario.update({"senha": gerar_senha_hash(senha)})

            return Usuario(**cada_usuario)


def autentica_usuario(usuario: str, senha: str):

    usuario_atual = recupera_usuario(usuario)
    if not usuario_atual:
        return False
    if not verificar_senha(senha, usuario_atual.senha):
        return False
    return usuario_atual


def gera_token_acesso(dados: dict, duracao: timedelta | None = None):

    dados_encode = dados.copy()
    if duracao:
        expira = datetime.now(timezone.utc) + duracao
    else:
        expira = datetime.now(timezone.utc) + timedelta(minutes=15)

    dados_encode.update({"exp": expira})
    token = jwt.encode(dados_encode, CHAVE_SECRETA, algorithm=ALGORITIMO)
    return token


async def recupera_usuario_atual(token: Annotated[str, Depends(oauth2_scheme)]):

    falha_credencial = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Não foi possivel validar o acesso",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:

        carregamento = jwt.decode(token, CHAVE_SECRETA, algorithms=[ALGORITIMO])
        nome_usuario = carregamento.get("sub")
        if nome_usuario is None:
            raise falha_credencial
        
        dados_token = DadosToken(usuario=nome_usuario)
    except InvalidTokenError:
        raise falha_credencial
    
    usuario = recupera_usuario(dados_token.usuario)
    if usuario is None:
        raise falha_credencial

    return usuario


async def recupera_usuario_habilitado(usuario: Annotated[Usuario, Depends(recupera_usuario_atual)]):

    if not usuario.habilitado:
        raise HTTPException(status_code=400, detail="Usuário inativo")
    return usuario


@app.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):

    falha_login = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Usuário ou senha incorreta",
        headers={"WWW-Authenticate": "Bearer"},
    )

    usuario = autentica_usuario(form_data.username, form_data.password)
    if not usuario:
        raise falha_login
    
    expiracao_token_acesso = timedelta(minutes=TEMPO_EXPIRAR_TOKEN_ACESSO)
    token_acesso = gera_token_acesso(dados={"sub": usuario.usuario}, duracao=expiracao_token_acesso)
    return Token(access_token=token_acesso, token_type="bearer")


@app.get("/users/me", response_model=Usuario)
async def read_users_me(usuario_logado: Annotated[Usuario, Depends(recupera_usuario_habilitado)]):
    return usuario_logado

@app.get("/users/me/items/")
async def read_own_items(usuario_logado: Annotated[Usuario, Depends(recupera_usuario_habilitado)]):
    return [{"item_id": "Foo", "owner": usuario_logado.usuario}]