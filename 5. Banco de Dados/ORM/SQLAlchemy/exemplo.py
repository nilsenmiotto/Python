from typing import Optional
from sqlalchemy import String, create_engine, select, delete
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column

# Cria a engine apontando para o banco
#engine = create_engine("sqlite:///meu_banco.db", echo=True)
#engine = create_engine("postgresql+psycopg2://postgres:mudar123@localhost:5432/meu_banco")
engine = create_engine("mysql+pymysql://root:mudar123@localhost:3306/meu_banco")

class Base(DeclarativeBase):
    ...

class Produto(Base):
    __tablename__ = "produtos"
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(80), nullable=False)
    preco: Mapped[float] = mapped_column(nullable=False)
    descricao: Mapped[Optional[str]] = mapped_column(String(200))

# Cria as tabelas se não existirem
Base.metadata.create_all(engine)

with engine.begin() as conn:

    # Deleta em lote
    conn.execute(delete(Produto).where(Produto.preco < 500))


# Use Session para garantir fechamento/rollback
with Session(engine) as session:

    # Inserir
    session.add_all([
        Produto(nome="Teclado", preco=199.9, descricao="Mecânico"),
        Produto(nome="Mouse", preco=99.9),
        Produto(nome="Monitor", preco=320.0),
    ])
    session.commit()


with Session(engine) as session:

    # Consultar
    produtos = session.scalars(select(Produto)).all()
    for item in produtos:
        print("Produto:", item.nome, "| Preço:", item.preco, "| Descrição:", item.descricao)


with Session(engine) as session:

    # Atualizar
    produto = session.scalar(select(Produto).where(Produto.nome == "Mouse"))
    if produto:
        produto.preco = 98.1
        produto.descricao = "Gamer"
        session.commit() # flush + commit; gera UPDATE só no que mudou

with Session(engine) as session:
    
    # Deletar
    produto = session.scalar(select(Produto).where(Produto.nome == "Monitor"))
    if produto:
        session.delete(produto)
        session.commit()