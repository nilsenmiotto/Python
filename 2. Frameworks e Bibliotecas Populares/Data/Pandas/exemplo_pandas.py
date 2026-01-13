"""
Roteiro rápido para praticar pandas no console ou em notebook.

Execute cada bloco e observe as saídas. Adapte as perguntas ao seu domínio.
"""

import pandas as pd
from pathlib import Path


def carregar_dados() -> pd.DataFrame:
    """Cria um DataFrame pequeno para experimentos."""
    dados = {
        "produto": ["cafe", "cafe", "cafe", "cha", "cha", "cha", "suco", "suco", "suco", "refri", "refri", "refri"],
        "loja": ["A", "B", "C", "A", "B", "C", "A", "B", "C", "A", "B", "C"],
        "preco": [12.5, 13.0, 12.0, 9.5, 9.0, 9.5, 7.0, 7.5, 6.9, 11.0, 11.2, 10.5],
        "quantidade": [100, 80, 120, 140, 200, 180, 217, 150, 150, 217, 150, 301],
        "data": [
            "2024-01-01",
            "2024-01-02",
            "2024-01-02",
            "2024-01-03",
            "2024-01-01",
            "2024-01-03",
            "2024-01-02",
            "2024-01-03",
            "2024-01-01",
            "2024-01-02",
            "2024-01-02",
            "2024-01-03",
        ],
    }
    df = pd.DataFrame(dados)
    df["data"] = pd.to_datetime(df["data"])
    return df


def inspeccionar(df: pd.DataFrame) -> None:
    print("\n=== Inspeção inicial ===")
    print(df.head())
    print("\nInfo:")
    print(df.info())
    print("\nResumo estatístico:")
    print(df.describe())


def selecionar(df: pd.DataFrame) -> None:
    print("\n=== Seleção de colunas/linhas ===")
    print("Coluna produto:")
    print(df["produto"])
    print("\nFiltro por loja A:")
    print(df[df["loja"] == "A"])
    print("\nFiltro por Produto refri:")
    print(df[df["produto"] == "refri"])
    print("\nloc (linhas 0-2, colunas produto/preco):")
    print(df.loc[0:2, ["produto", "preco"]])
    print("\niloc (linhas 0-2, colunas 0-1):")
    print(df.iloc[0:3, 0:2])


def transformar(df: pd.DataFrame) -> None:
    print("\n=== Transformações ===")
    df_com_total = df.assign(total=lambda x: x["preco"] * x["quantidade"])
    print("Com coluna total:")
    print(df_com_total.head(20))

    print("\nAgrupado por produto:")
    agrupado = df_com_total.groupby("produto").agg(
        vendas_total=("total", "sum"),
        preco_medio=("preco", "mean"),
        unidades=("quantidade", "sum"),
    )
    print(agrupado)

    print("\nReceita bruta por loja:")
    agrupado_loja = df_com_total.groupby("loja").agg(
        vendas_total=("total", "sum"),
    )
    print(agrupado_loja)

    pivot = df_com_total.pivot_table(
        index="data", columns="loja", values="quantidade", aggfunc="sum"
    )
    print("\nPivot quantidades por data/loja:")
    print(pivot)

    melt = df_com_total.melt(id_vars=["produto", "loja"], value_vars=["preco", "quantidade"])
    print("\nMelt para formato longo:")
    print(melt.head())


def integrar(df: pd.DataFrame) -> None:
    print("\n=== Merge/Join ===")
    catalogo = pd.DataFrame(
        {
            "produto": ["cafe", "cha", "suco", "refri"],
            "categoria": ["quente", "quente", "frio", "frio"],
        }
    )
    combinado = df.merge(catalogo, on="produto", how="left")
    print(combinado.head(20))


def tratar_dados(df: pd.DataFrame) -> None:
    print("\n=== Limpeza simples ===")
    sujo = df.copy()
    sujo.loc[1, "preco"] = None
    sujo.loc[4, "produto"] = None
    sujo.loc[10, "quantidade"] = None
    print("Dados sujos:")
    print(sujo)

    print("\nValores faltantes por coluna:")
    print(sujo.isna().sum())

    limpo = sujo.copy()
    limpo["preco"] = limpo["preco"].fillna(limpo["preco"].median())
    limpo["produto"] = limpo["produto"].fillna("desconhecido")
    limpo["quantidade"] = limpo["quantidade"].fillna(0)
    print("\nApós tratar faltantes:")
    print(limpo)


def salvar_csv(df: pd.DataFrame, caminho: str = "saida.csv") -> None:
    print(f"\n=== Salvando em {caminho} ===")
    df.to_csv(caminho, index=False)
    print("Arquivo escrito.")


def roteiro():
    df = carregar_dados()
    inspeccionar(df)
    selecionar(df)
    transformar(df)
    integrar(df)
    tratar_dados(df)

    arquivo = Path(__file__).resolve().parent / "dados_saida.csv"
    salvar_csv(df, arquivo)

if __name__ == "__main__":
    roteiro()
