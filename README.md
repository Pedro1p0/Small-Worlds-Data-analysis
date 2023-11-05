
# Projeto de Análise de Redes Sociais e Grafos

Este projeto visa a análise e visualização de dados de diferentes redes sociais e grafos usando a linguagem de programação Python, juntamente com as bibliotecas NetworkX, Matplotlib e Seaborn. O objetivo é explorar as propriedades dessas redes e grafos para obter insights valiosos sobre suas estruturas e relações.

## Conjunto de Dados

O projeto utiliza várias fontes de dados representando diferentes redes sociais e grafos. Algumas das redes sociais e grafos incluídos são:

1. **Wikipedia Vote Network**: Um grafo que representa conexões entre editores da Wikipedia, onde as arestas indicam votos entre editores.

2. **Pokec Social Network**: Um grafo que descreve conexões em uma rede social eslovaca chamada Pokec.

3. **Social Circles: Twitter**: Dados de conexões de amizade no Twitter, representando círculos sociais.

4. **Youtube Social Network and Ground-Truth Communities**: Dados de conexões de amizade no YouTube, juntamente com informações sobre as comunidades reais.

5. **Google Web Graph**: Uma representação do grafo da web do Google, que é usado para indexação e pesquisa na web.

## Resultado da compilação dos códigos e analise dos gráficos

**Wikipedia Vote Network**: Um grafo que representa conexões entre editores da Wikipedia, onde as arestas indicam votos entre editores.
  ![Resultado no VSCode](https://github.com/Pedro1p0/Small-Worlds-Data-analysis/blob/d733ab54e35fc54356d779f12813c2cb0a1bf5f2/wiki_vote_dcata.png)

**Pokec Social Network**: Um grafo que descreve conexões em uma rede social eslovaca chamada Pokec.
  ![Resultado no VSCode](https://github.com/Pedro1p0/Small-Worlds-Data-analysis/blob/348b993a34bf0a437e831ae7fc51ade5f3b9f5a2/pokec_data.png)

**Social Circles: Twitter**: Dados de conexões de amizade no Twitter, representando círculos sociais.
  ![Resultado no VSCode](https://github.com/Pedro1p0/Small-Worlds-Data-analysis/blob/348b993a34bf0a437e831ae7fc51ade5f3b9f5a2/twitter_data.png)

**Youtube Social Network and Ground-Truth Communities**: Dados de conexões de amizade no YouTube, juntamente com informações sobre as comunidades reais.
  ![Resultado no VSCode](https://github.com/Pedro1p0/Small-Worlds-Data-analysis/blob/348b993a34bf0a437e831ae7fc51ade5f3b9f5a2/youtube_data.png)

**Google Web Graph**: Uma representação do grafo da web do Google, que é usado para indexação e pesquisa na web.
  ![Resultado no VSCode](https://github.com/Pedro1p0/Small-Worlds-Data-analysis/blob/348b993a34bf0a437e831ae7fc51ade5f3b9f5a2/Google_data.png)

# Análise dos gráficos
 Análise Comparativa de Redes Sociais e Grafos

A análise de redes sociais e grafos desempenha um papel fundamental na compreensão das dinâmicas de relacionamento em várias plataformas online. Neste estudo, exploramos a estrutura e as propriedades de cinco redes sociais e grafos populares: Wikipedia Vote Network, Pokec Social Network, Social Circles: Twitter, YouTube Social Network and Ground-Truth Communities e Google Web Graph. Utilizamos um gráfico de dispersão que relaciona o grau dos nós com o grau médio dos vizinhos em cada um desses grafos para obter insights sobre suas características distintas.

## Wikipedia Vote Network

O gráfico da Wikipedia Vote Network apresentou uma tendência decrescente, indicando que os nós com graus mais altos tendem a estar conectados a vizinhos com graus mais baixos. A maioria dos pontos se acumula na metade esquerda do gráfico, sugerindo que há uma concentração de editores com um número relativamente baixo de votos e conexões. No entanto, é interessante notar que alguns pontos estão mais à direita, o que indica que um pequeno número de editores altamente conectados ainda existe. Essa estrutura sugere que a Wikipedia é uma rede com uma maioria de colaboradores com interações limitadas, mas também inclui alguns editores altamente influentes com um grande número de conexões.

## Pokec Social Network

O gráfico da Pokec Social Network exibe uma concentração notável de pontos à esquerda, formando uma reta vertical no início. Isso indica que a maioria dos usuários da rede tem um número relativamente baixo de conexões. No entanto, à medida que nos movemos para a direita no gráfico, encontramos apenas alguns pontos, o que sugere que um pequeno grupo de usuários possui conexões substanciais. Essa estrutura é consistente com uma rede social em que a maioria dos usuários tem um círculo social relativamente restrito, enquanto um pequeno número de influenciadores pode ter um grande número de seguidores.

## Social Circles: Twitter

Ao analisar o gráfico da rede Social Circles do Twitter, também notamos uma tendência decrescente, mas com algumas diferenças em relação ao gráfico da Pokec. Embora ainda haja uma concentração de pontos à esquerda, indicando que a maioria dos usuários tem um número limitado de seguidores, essa concentração é menos pronunciada. Além disso, observamos que alguns pontos estão mais à direita, sugerindo que, no Twitter, um número maior de usuários possui um número significativo de seguidores. Isso pode refletir a natureza mais aberta do Twitter, onde muitos usuários têm a oportunidade de ganhar seguidores substanciais, como celebridades e figuras públicas.

## YouTube Social Network and Ground-Truth Communities

O gráfico da rede social do YouTube mostra uma tendência semelhante à da Wikipedia e do Twitter, com uma concentração significativa de pontos à esquerda, indicando que muitos usuários têm um número limitado de conexões. No entanto, em comparação com as redes anteriores, a estrutura é mais dispersa, com menos pontos à direita. Isso sugere que, embora haja uma concentração de usuários com um pequeno número de seguidores, a diferença entre os usuários menos conectados e os mais conectados é menos acentuada no YouTube.

## Google Web Graph

O Google Web Graph é um caso interessante, pois exibe a tendência decrescente característica, mas com uma estrutura menos acentuada. Os pontos no gráfico estão mais distribuídos ao longo da reta, sugerindo uma variedade mais equilibrada de sites na web. Enquanto ainda há uma concentração de sites com poucos links, a diferença entre sites altamente conectados e menos conectados não é tão extrema quanto em algumas das redes sociais analisadas. Isso é consistente com a natureza da web, onde sites populares, como mecanismos de busca, podem ser altamente conectados, mas muitos sites individuais também têm um número considerável de links.

## Conclusão

A análise dos gráficos de dispersão das redes sociais e grafos revela uma série de padrões e tendências interessantes. A natureza decrescente dos gráficos sugere que, em muitas redes sociais, a maioria dos usuários ou nós tende a ter um número limitado de conexões ou seguidores, enquanto apenas um pequeno número de usuários alcança altos níveis de conexões.

A diferença entre as redes sociais reside na intensidade dessas tendências. Redes como a Wikipedia e a Pokec exibem concentrações significativas de nós com baixos graus, enquanto redes como o Twitter e o YouTube são mais inclusivas, com uma proporção maior de usuários alcançando um número significativo de conexões.

O Google Web Graph, por sua vez, representa uma estrutura da web mais balanceada, refletindo a diversidade de sites na internet, onde a distribuição de links é mais uniforme.

Essas análises ilustram a importância de entender a estrutura das redes sociais e grafos em diferentes contextos. A compreensão dessas estruturas é fundamental para estratégias de marketing, influência social, otimização de mecanismos de busca e muito mais. A análise de grafos é uma ferramenta poderosa para desvendar as complexas dinâmicas das redes e grafos em nosso mundo interconectado.

## Tabela no formato markdown com caracteristicas dos dados

| Rede                           | Qtd Vértices | Qtd Arestas | Degree Assortativity | Qtd Componentes Conectados | Tamanho do Comp. Gigante (GCC) | Avg Clustering |
|--------------------------------|--------------|-------------|-----------------------|---------------------------|-------------------------------|----------------|
| Wikipedia Vote Network         | 7115         | 103689      | -0.0673               | 5                         | 7066 (0.993)                  | 0.1409         |
| Pokec Social Network           | 1632803      | 30622564    | -0.0511               | 1                         | 1632803 (1.000)               | 0.1094         |
| Social Circles: Twitter        | 81306        | 1768149     | -0.1406               | 1                         | 81306 (1.000)                 | 0.5653         |
| Youtube Social Network         | 1134890      | 2987624     | -0.1138               | 1                         | 1134890 (1.000)               | 0.0808         |
| Google Web Graph               | 875713       | 5105039     | -0.0959               | 2                         | 855802 (0.977)                | 0.5143         |

