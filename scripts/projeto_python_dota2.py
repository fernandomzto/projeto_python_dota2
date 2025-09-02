# %%
# Importando a Biblioteca Pandas, Matplotlib e Seaborn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# %%
# Abrindo o arquivo csv
df = pd.read_csv('dados/dota2_heroes.csv')
# %%
# Renomeando as colunas para melhor identificação
# Criar um dicionário para mapear os nomes antigos para os novos.

novos_nomes = {
    'Unnamed: 0': 'id_heroi',
    'Hero' : 'nome_heroi',
    'Primary Attribute' : 'atributo_primario',
    'Strength' : 'força',
    'Agility' : 'agilidade',
    'Intelligence' : 'inteligencia',
    'S+' : 'ganho_força_nivel',
    'A+' : 'ganho_agilidade_nivel',
    'I+' : 'ganho_inteligencia_nivel',
    'Movement speed' : 'velocidade_movimento',
    'Sight range Day' : 'alcance_visao_dia',
    'Sight range Night' : 'alcance_visao_noite',
    'Armor' : 'armadura',
    'Base attack time' : 'velocidade_base_ataque',
    'Damage1' : 'dano_primario',
    'Damage2' : 'dano_secundario',
    'Attack point' : 'ponto_ataque'
}

# Renomeando as colunas e atribuindo a variável df
df = df.rename(columns=novos_nomes)
# %%
# Verificando se as colunas foram renomeadas corretamente
print("Colunas após a renomeação:")
print(df.columns)
# %%
# Verificar a existência de misssing values
# Contando a quantidade de valores ausentes em cada coluna. isna() retorna um valor booleano para verificar se existem valores ausentes
# sum() é utilizado para somar a quantidade de valores booleanos retornados.
valores_ausentes_por_coluna = df.isna().sum()

print("\nContagem de valores ausentes por coluna:")
print(valores_ausentes_por_coluna)
# %%
# Verificar se existem registros duplicados
# Contando o número de linhas totalmente duplicadas
duplicatas = df.duplicated().sum()
print(f"O dataset possui {duplicatas} linhas duplicadas.")

# %%
# ANÁLISES

# Gera estatísticas descritivas para todas as colunas numéricas para ter uma visão geral do dataframe
print("\nEstatísticas Descritivas do Dataset:")

# Observando panorama geral do dataset
df.describe().T
# %%
# Verificando total de heróis na base de dados
df['id_heroi'].shape
# %%
# Quantos heróis de cada atributo? *Em valores totais
df['atributo_primario'].value_counts()
# %%
# %%
# Quantos heróis de cada atributo? *Em %
df['atributo_primario'].value_counts(normalize=True).round(3)*100
# %%
# Após análises de contagem, hora de organizar alguns Ranks e Extremos.

# Qual o Top 10 heróis de força (base)?
top_10_forca_base = df.sort_values(by='força', ascending=False).head(10)
print('Top 10 Heróis por Força(base):')
print(top_10_forca_base[['nome_heroi', 'força']])
#%%
# Qual o Top 10 heróis de agilidade (base)?
top_10_agilidade_base = df.sort_values(by='agilidade', ascending=False).head(10)
print('Top 10 Heróis por Agilidade(base):')
print(top_10_agilidade_base[['nome_heroi', 'agilidade']])
# %%
# Qual o Top 10 heróis de inteligência (base)?
top_10_inteligencia_base = df.sort_values(by='inteligencia', ascending=False).head(10)
print('Top 10 Heróis por Inteligência(base):')
print(top_10_inteligencia_base[['nome_heroi', 'inteligencia']])
# %%
# Qual o Top 10 Heróis por Velocidade de Movimento?
top_10_velocidade_movimento = df.sort_values(by='velocidade_movimento', ascending=False).head(10)
print('Top 10 Heróis por Velocidade de Movimento:')
print(top_10_velocidade_movimento[['nome_heroi', 'velocidade_movimento']])
# %%
# Qual o Top 10 Heróis por Armadura?
top_10_armadura = df.sort_values(by='armadura', ascending=False).head(10)
print('Top 10 Heróis por Armadura:')
print(top_10_armadura[['nome_heroi', 'armadura']])
# %%
# Qual o Top 10 Heróis por Velocidade Base de Ataque?
top_10_velocidade_base_ataque = df.sort_values(by='velocidade_base_ataque', ascending=False).head(10)
print('Top 10 Heróis por Velocidade de Ataque (base):')
print(top_10_velocidade_base_ataque[['nome_heroi', 'velocidade_base_ataque']])
# %%
# Qual o Top 10 Heróis que mais ganham Força por Nível?
top_10_ganho_forca = df.sort_values(by='ganho_força_nivel', ascending=False).head(10)
print('Top 10 Herói por Ganho de Força/Lvl:')
print(top_10_ganho_forca[['nome_heroi', 'ganho_força_nivel']])
# %%
# Qual o Top 10 Heróis que mais ganham Agilidade por Nível?
top_10_ganho_agilidade = df.sort_values(by='ganho_agilidade_nivel', ascending=False).head(10)
print('Top 10 Herói por Ganho de Agilidade/Lvl:')
print(top_10_ganho_agilidade[['nome_heroi', 'ganho_agilidade_nivel']])
# %%
# Qual o Top 10 Heróis que mais ganham Inteligência por Nível?
top_10_ganho_inteligencia = df.sort_values(by='ganho_inteligencia_nivel', ascending=False).head(10)
print('Top 10 Herói por Ganho de Inteligencia/Lvl:')
print(top_10_ganho_inteligencia[['nome_heroi', 'ganho_inteligencia_nivel']])
# %%
# Criando novas colunas para melhores insights
# Exemplo: Quem tem o maior dano médio (primário + secundário)?

df['dano_medio_total'] = (df['dano_primario'] + df['dano_secundario']) / 2

top_10_dano_medio_total = df.sort_values(by='dano_medio_total', ascending=False).head(10)
print('Top 10 Heróis por Dano Médio Total (primario + secundário)')
print(top_10_dano_medio_total[['nome_heroi', 'dano_medio_total']])
# %%
# Quais heróis ganha mais atributos no geral (força, agilidade e inteligência) a cada Nível?

df['ganho_geral_atributos'] = df['ganho_força_nivel'] + df['ganho_agilidade_nivel'] + df['ganho_inteligencia_nivel']

top_10_ganho_geral_nivel = df.sort_values(by='ganho_geral_atributos', ascending=False).head(10)
print('Top 10 Heróis por Ganho Geral de Atributos por Lvl:')
print(top_10_ganho_geral_nivel[['nome_heroi', 'ganho_geral_atributos']])
# %%
# Analisando as medidas por categorias/grupos

media_por_atributos = df.groupby('atributo_primario')[['força', 'agilidade', 'inteligencia', 'velocidade_movimento', 'armadura', 'dano_medio_total', 'ganho_geral_atributos']].mean()
print('\nMédia de Status por Atributo Primário:')
media_por_atributos.round(2).T
# %%
# Agora quero verificar uma combinação de atributos
# Quais heróis são "canhões de vidro" (alto dano e baixa armadura)?

# 1. Definir os limites (utilizando os quartis)
limite_dano_alto = df['dano_medio_total'].quantile(0.75)
limite_armadura_baixa = df['armadura'].quantile(0.25)

# 2. Aplicar o filtro combinado
canhoes_de_vidro = df[
    (df['dano_medio_total'] >= limite_dano_alto) &
    (df['armadura'] <= limite_armadura_baixa)
]

# 3. Exibir o resultado de forma organizada
print("Heróis com Dano Alto (Top 25%) e Armadura Baixa (Bottom 25%):")
print(canhoes_de_vidro.sort_values(by='dano_medio_total', ascending=False)[['nome_heroi', 'atributo_primario', 'dano_medio_total', 'armadura']])
# %%
# Quais os maiores "tanks" (alta armadura, alta força)
limite_armadura_alta = df['armadura'].quantile(0.75)
limite_força_alta = df['força'].quantile(0.75)

tanks = df[
    (df['armadura'] >= limite_armadura_alta) &
    (df['força'] >= limite_força_alta)
]

print('Heróis com Armadura Alta (Top 25%) e Força Alta (Top 25%):')
print(tanks.sort_values(by='armadura', ascending=False)[['nome_heroi', 'atributo_primario', 'armadura', 'força']])

# %%
# Quais heróis conseguem um melhor controle de mapa (alta velocidade de movimento e alta visão durante o dia)?
limite_movimento = df['velocidade_movimento'].quantile(0.9)
limite_visao = df['alcance_visao_dia'].quantile(0.9)

herois_mobilidade_visao = df[
    (df['velocidade_movimento'] >= limite_movimento) &
    (df['alcance_visao_dia'] >= limite_visao)
]

print('Heróis com Alta Mobilidade + Alta Visão:')
print(herois_mobilidade_visao[['nome_heroi', 'velocidade_movimento', 'alcance_visao_dia']])
# %%
# Observando correlações:

df.corr(numeric_only=True).round(1)

# Observando a matriz de correlações, não foi possível identificar correlações positivas
# ou negativas muito fortes. Isso pode ser devido ao fato do jogo tentar manter um equilíbrio entre os heróis.
# No caso, o que diferencia quais heróis estão no meta envolvem uma combinação de fatores como os exibidos nesse projeto
# aliados às habilidades e facets dos heróis em cada patch lançado.

# %%
# --- GRÁFICO 1: Contagem de Heróis por Atributo Primário ---

# 1. PREPARAR OS DADOS (você já fez isso antes)
contagem_atributos = df['atributo_primario'].value_counts()

# 2. CRIAR A FIGURA (o "quadro" onde vamos pintar)
# figsize=(10, 6) define o tamanho do gráfico em polegadas para que ele não fique muito pequeno.
plt.figure(figsize=(10, 6))

# 3. DESENHAR O GRÁFICO
# Usamos o Seaborn para criar um gráfico de barras.
# x=... : As categorias que ficam no eixo horizontal (Força, Agilidade, etc.).
# y=... : Os valores numéricos que definem a altura das barras.
sns.barplot(x=contagem_atributos.index, y=contagem_atributos.values, palette='viridis')

# 4. PERSONALIZAR E EXIBIR
# Usamos o Matplotlib para adicionar informações e dar o comando final.
plt.title('Quantidade de Heróis por Atributo Primário', fontsize=16) # Título do gráfico
plt.xlabel('Atributo Primário', fontsize=12) # Rótulo do eixo X
plt.ylabel('Número de Heróis', fontsize=12) # Rótulo do eixo Y
plt.xticks(rotation=45) # Rotaciona os rótulos do eixo X para não se sobreporem
plt.show() # Comando final para exibir o gráfico que criamos.
# %%
# --- GRÁFICO 2: Distribuição da Velocidade de Movimento ---

plt.figure(figsize=(12, 6))

# Usamos o histplot do Seaborn para visualizar a distribuição de uma única variável.
# kde=True adiciona uma linha de densidade para suavizar o formato da distribuição.
sns.histplot(data=df, x='velocidade_movimento', kde=True, bins=15)

plt.title('Distribuição da Velocidade de Movimento dos Heróis', fontsize=16)
plt.xlabel('Velocidade de Movimento', fontsize=12)
plt.ylabel('Frequência (Nº de Heróis)', fontsize=12)
plt.show()

# %%
# # --- GRÁFICO FINAL (Opcional): Mapa de Calor das Correlações ---
plt.figure(figsize=(16, 10))
matriz_arredondada = df.corr(numeric_only=True).round(2)
sns.heatmap(data=matriz_arredondada, annot=True, cmap='coolwarm', linewidths=.5)
plt.title('Mapa de Calor das Correlações de Atributos dos Heróis', fontsize=16)
plt.show()
# %%
# # Salvando o arquivo csv com as colunas renomeadas e outras correções
# # O index=False evita que o índice do Pandas seja salvo como uma coluna no CSV.
df.to_csv('dados/dota2_heroes_limpo.csv', index=False)
print("Arquivo CSV limpo exportado com sucesso!")
# %%
