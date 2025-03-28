# Importando os pacotes a serem utilizados
import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors
from scipy.sparse import csr_matrix


# Importar o arquivo com os filmes
filmes = pd.read_csv('movies_metadata.csv', low_memory=False)

# Importando o arquivo de avaliações 
avaliacoes = pd.read_csv('ratings.csv')

# Filtrando somente as colunas necessárias e renomeando o nome das variaveis

# Seleciona somente as variaveis que iremos utilizar
filmes = filmes[['id', 'original_title', 'original_language', 'vote_count']]

# Renomeia as variaveis
filmes.rename(columns={'id':'ID_FILME', 'original_title':'TITULO', 'original_language':'LINGUAGEM', 'vote_count':'QT_AVALIACOES'}, inplace=True)

# Filtrando somente as colunas necessárias e renomeando o nome das variaveis

# Seleciona somente as variaveis que iremos utilizar
avaliacoes = avaliacoes [['userId', 'movieId', 'rating']]

# Renomeia as variaveis
avaliacoes.rename(columns={'userId':'ID_USUARIO', 'movieId':'ID_FILME', 'rating':'AVALIACAO'}, inplace=True)

# Verificando se há valores nulos
filmes.isna().sum()

# Como são poucos os valores nulos iremos remover porque não terá impacto nenhum
filmes.dropna(inplace=True)

# Verificando se há valores nulos
filmes.isna().sum()

# Verificando se há valores nulos
avaliacoes.isna().sum()

# Verificando a quantidade de avaliacoes por usuarios
avaliacoes['ID_USUARIO'].value_counts()

# Vamos pegar o ID_USUARIO somente de usuários que fizeram mais de 999 avaliações
qt_avaliacoes = avaliacoes['ID_USUARIO'].value_counts() > 999
y = qt_avaliacoes[qt_avaliacoes].index # index para puxar o indice de avaliações

# avaliacoes.shape # mostra as dimensões do dataframe, (26024289, 3) então vai ser (resultados, colunas)

# Pegando somente avaliacoes dos usuarios que avaliaram mais de 999 vezes
avaliacoes = avaliacoes[avaliacoes['ID_USUARIO'].isin(y)]

# Vamos usar os filmes que possuem somente uma quantidade de avaliações superior a 999 avaliações
filmes = filmes[filmes['QT_AVALIACOES'] > 999]

# Vamos agrupar e visualizar a quantidade de filmes pela linguagem
filmes_linguagem = filmes['LINGUAGEM'].value_counts()

# Selecionar somente os filmes da linguagem EN (English)
filmes = filmes[filmes['LINGUAGEM'] == 'en']

# Precisamos converter a variavel ID_FILME em inteiro
filmes['ID_FILME'] = filmes['ID_FILME'].astype(int)

# Concatenando os dataframes
avaliacoes_e_filmes = avaliacoes.merge(filmes, on='ID_FILME')

# Vamos excluir a variavel ID_FILME porque não iremos utiliza-la
del avaliacoes_e_filmes['ID_FILME']

# Agora precisamos fazer um PIVOT. O que queremos é que cada ID_USUÁRIO seja uma variável com o respectivo valor de nota para cada filme avaliado
filmes_pivot = avaliacoes_e_filmes.pivot_table(columns='ID_USUARIO', index='TITULO', values='AVALIACAO')

# Os valores que são nulos iremos preencher com ZERO
filmes_pivot.fillna(0, inplace=True)

# Vamos transformar o nosso dataset em uma matriz sparse
filmes_sparse = csr_matrix(filmes_pivot)

# Criando e treinando o modelo preditivo
modelo = NearestNeighbors(algorithm='brute')
modelo.fit(filmes_sparse)

# 127 Hours
distances, sugestions = modelo.kneighbors(filmes_pivot.filter(items=['127 Hours'], axis=0).values.reshape(1, -1))

for i in range(len(sugestions)):
    print(filmes_pivot.index[sugestions[i]])