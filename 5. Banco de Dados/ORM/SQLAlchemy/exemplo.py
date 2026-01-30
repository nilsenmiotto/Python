from typing import Optional
from sqlalchemy import String, ForeignKey, create_engine, select, delete
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, relationship

# Cria a engine apontando para o banco
#engine = create_engine("sqlite:///meu_banco.db", echo=True)
#engine = create_engine("postgresql+psycopg2://postgres:mudar123@localhost:5432/meu_banco")
engine = create_engine("mysql+pymysql://root:mudar123@localhost:3306/meu_banco")

class Base(DeclarativeBase):
    ...

class Categoria(Base):
    __tablename__ = "categorias"
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(100))

    produtos: Mapped[list["Produto"]] = relationship(
        back_populates="categoria", cascade="all, delete-orphan"
    )

class Produto(Base):
    __tablename__ = "produtos"
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(80), nullable=False)
    preco: Mapped[float] = mapped_column(nullable=False)
    descricao: Mapped[Optional[str]] = mapped_column(String(200))
    categoria_id: Mapped[int] = mapped_column(ForeignKey("categorias.id"), nullable=False)
    categoria: Mapped[Categoria] = relationship(back_populates="produtos")


# Deleta e Cria as tabelas se não existirem
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

#with engine.begin() as conn:

    # Deleta em lote
    #conn.execute(delete(Produto).where(Produto.preco < 500))
    

# Use Session para garantir fechamento/rollback
with Session(engine) as session:

    # Inserir
    categoria_id = Categoria(nome="Periféricos")
    session.add(categoria_id)
    session.flush # garante criar a id antes de usar

    session.add_all([
        Produto(nome="Teclado", preco=199.9, categoria=categoria_id, descricao="Mecânico"),
        Produto(nome="Mouse", preco=99.9, categoria=categoria_id),
        Produto(nome="Monitor", preco=320.0, categoria=categoria_id),
    ])
    session.commit()

    # Consultar todos os produtos
    produtos = session.scalars(select(Produto)).all()
    for item in produtos:
        print("Produto:", item.nome, "| Preço:", item.preco, "| Descrição:", item.descricao, "| Categoria:", item.categoria.nome)

    # Atualizar
    produto = session.scalar(select(Produto).where(Produto.nome == "Mouse"))
    if produto:
        produto.preco = 98.1
        produto.descricao = "Gamer"
        session.commit() # flush + commit; gera UPDATE só no que mudou

    # Cunsultar todos os produtos com a categoria Periféricos
    perifericos = session.scalars(
        select(Produto).where(Produto.categoria.has(nome="Periféricos"))
    ).all()

    for periferico in perifericos:
        print("Produto:", periferico.nome, "| Categoria:", periferico.categoria.nome)

    
    # Deletar
    produto = session.scalar(select(Produto).where(Produto.nome == "Monitor"))
    if produto:
        session.delete(produto)
        session.commit()