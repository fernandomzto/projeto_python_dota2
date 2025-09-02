# %%
# Importando a Biblioteca Pandas
import pandas as pd

# %%
# Abrindo o arquivo csv
df = pd.read_csv('dados/dota2_heroes.csv')

# %%
# Mostrar as primeiras linhas
df.head()

# %%
# Mostrar as últimas linhas
df.tail()

# %%
# Mostrar as colunas do dataframe
df.columns

# %%
# Mostrar a quantidade de linhas e colunas do dataframe
df.shape

# %%
# Mostrar um resumo do dataframe
df.info()

# %%
# Acessando uma coluna em específico
df['Hero']

# %%
# Acessando várias colunas simultâneas. Precisa colocar as colunas em uma lista.
df[['Hero', 'Primary Attribute']]

# %%
# Acessando linhas específicas. Exemplo: acessando a primeira linha
df['Hero'][0]

# %%
# .loc acessa por rótulos dos índices ou nome das colunas
# Exemplo: Acessando a primeira linha de índice 0 com as colunas Hero e Primary Attribute
df.loc[0, ['Hero', 'Primary Attribute']]

# %%
# .iloc acessa pela posição numérica da linha/coluna no DataFrame
# Acessando a primeira linha e colunas 1 e 2 (n-1), que são Hero e Primary Attribute
df.iloc[0, 1:3]

# %%
# FILTROS COM PANDAS
# Exemplo: Quero apenas os heróis de atributo primário Strength
df['Primary Attribute'] == "strength"

# %%
df.loc[df['Primary Attribute'] == "strength"]
# %%
# Quantos são heróis de força?
df.loc[df['atributo_primario'] == "strength"].shape

# %%
# Para utilizar duas lógicas ao mesmo tempo
# Exemplo: Quero saber quais são os heróis de força que possuem Força maior que 25
df.loc[(df['Primary Attribute'] == "strength") & (df['Strength'] > 25)]

# %%
# Para verificar duas lógicas, mas apenas uma das condições precisa ser verdadeira
# Exemplo: Quero saber quais são os heróis de força OU (|) que possuem Força maior que 25.
df.loc[(df['Primary Attribute'] == "strength") | (df['Strength'] > 25)]

# %%
# Consultas semelhantes ao SQL
df.query("Strength > 20 and Agility > 20 or Intelligence > 26")
# %%
df.groupby('Primary Attribute')[['Damage1', 'Damage2']].mean()
# %%
df.groupby('Primary Attribute')['Armor'].mean()
# %%
# Quantos heróis de cada atributo? *Em valores totais
df['atributo_primario'].value_counts()

# %%
# Quantos heróis de cada atributo? *Em %
df['atributo_primario'].value_counts(normalize=True)*100