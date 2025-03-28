# Sistema de Recomendação de Filmes

Este projeto apresenta um sistema de recomendação de filmes baseado em filtragem colaborativa, desenvolvido a partir de uma aula sobre modelos de recomendação. O código utilizado neste repositório é o mesmo apresentado na aula e foi adaptado para demonstrar como criar um modelo simples de recomendação utilizando técnicas de aprendizado de máquina.

Aula: [Como criar um modelo de Machine Learning de RECOMENDAÇÃO](https://www.youtube.com/watch?v=sDI3ntGFbSI)

## Funcionalidades

- **Filtragem de Usuários e Filmes**: Considera apenas usuários com mais de 999 avaliações e filmes com mais de 999 avaliações para garantir a qualidade das recomendações.
- **Criação de Tabela Pivô**: Transforma os dados de avaliações em uma matriz onde as linhas representam filmes, as colunas representam usuários e os valores são as avaliações correspondentes.
- **Modelo k-NN (k-Nearest Neighbors)**: Utiliza o algoritmo k-NN para identificar filmes semelhantes com base nos padrões de avaliação dos usuários.
- **Recomendações Personalizadas**: Dado um filme de referência, o sistema sugere outros filmes com padrões de avaliação semelhantes.

## Tecnologias Utilizadas

- **Python**: Linguagem principal para manipulação de dados e implementação do modelo.
- **Pandas**: Para manipulação e análise de dados.
- **NumPy**: Para operações numéricas eficientes.
- **SciPy**: Para criação de matrizes esparsas.
- **Scikit-learn**: Para implementação do algoritmo k-NN.

## Como Executar

1. Clone este repositório para sua máquina local.
2. Certifique-se de ter todas as bibliotecas necessárias instaladas. Você pode instalar as dependências utilizando o seguinte comando:
   ```bash
   pip install -r requirements.txt

3. Execute o script principal para gerar recomendações com base nos dados fornecidos. Por exemplo:
    ```bash
    python recomendacao_filmes.py

