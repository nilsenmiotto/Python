import pandas as pd
from pathlib import Path

arquivo = Path(__file__).parent / "titanic.csv"
titanic = pd.read_csv(arquivo)

print(titanic.head())

idade = titanic["Age"]
print(idade.describe())

print(titanic.shape)

titanic_menores_30 = titanic[titanic["Age"] < 30]
print(titanic_menores_30)

classe_2_3 = titanic[titanic["Pclass"].isin([2, 3])]
print(classe_2_3.shape)

nome_idosos = titanic.loc[titanic["Age"] > 60, "Name"]
print(nome_idosos)

media_idade = titanic["Age"].mean()
print(f"Média de idade: {media_idade}")

print(f"Média de idade e tarifa: {titanic[['Age', 'Fare']].mean()}")

agregrando = titanic.agg(
    {
        "Age": ["min", "max", "median", "skew"],
        "Fare": ["min", "max", "median", "mean"],
    }
)
print(f"Agregando estatísticas:\n{agregrando}")

media_idade_por_sexo = titanic[["Sex", "Age"]].groupby("Sex").mean()
print(f"Média de idade por sexo:\n{media_idade_por_sexo}")

media_idade_por_sexo2 = titanic.groupby("Sex")["Age"].mean()
print(f"Média de idade por sexo (método 2):\n{media_idade_por_sexo2}")

preco_medio_ticket_por_sexo = titanic.groupby(["Sex", "Pclass"])["Fare"].mean()
print(f"Preço médio do ticket por sexo e classe:\n{preco_medio_ticket_por_sexo}")

quantidade_por_classe = titanic["Pclass"].value_counts()
print(f"Quantidade de passageiros por classe:\n{quantidade_por_classe}")

# manipulando strings
titanic["Name_upper"] = titanic["Name"].str.upper()
print(titanic[["Name", "Name_upper"]].head())

titanic["Last_Name"] = titanic["Name"].str.split(",").str[0]
print(titanic[["Name", "Last_Name"]].head())

print(titanic["Name"].str.contains("Heath"))

print(titanic["Name"].str.len())

print(titanic["Name"].str.len().idxmax())
print(titanic.loc[titanic["Name"].str.len().idxmax(), "Name"])

titanic["Sex_short"] = titanic["Sex"].replace({"male": "M", "female": "F"})
print(titanic["Sex_short"].head())