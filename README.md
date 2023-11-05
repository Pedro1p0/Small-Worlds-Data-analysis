
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
| Wikipedia Vote Network         | 7115         | 103689      | -0.0673               | x                         | 7066 (0.993)                  | 0.1409         |
| Pokec Social Network           | 1632803      | 30622564    | -0.0511               | x                         | 1632803 (1.000)               | 0.1094         |
| Social Circles: Twitter        | 81306        | 1768149     | -0.1406               | x                         | 81306 (1.000)                 | 0.5653         |
| Youtube Social Network         | 1134890      | 2987624     | -0.1138               | x                         | 1134890 (1.000)               | 0.0808         |
| Google Web Graph               | 875713       | 5105039     | -0.0959               | x                         | 855802 (0.977)                | 0.5143         |

**Wikipedia Vote Network: Explorando a Colaboração Editorial**

A Wikipedia Vote Network é uma representação das conexões entre editores da Wikipedia, onde as arestas indicam votos entre editores. Com 7.115 vértices e 103.689 arestas, esta rede reflete uma comunidade de colaboradores que tomam decisões coletivas sobre as edições da enciclopédia online. 

O coeficiente de assortatividade de -0,0673 sugere que, embora a maioria dos editores não esteja fortemente conectada a outros com números semelhantes de votos, a rede mantém alguma estrutura. Além disso, a presença de cinco componentes conectados indica uma certa fragmentação na colaboração, mas o maior componente gigante (GCC) com 7.066 vértices (99,3% do total) destaca a força da interconexão entre editores. 

O coeficiente de agrupamento médio (Avg Clustering) de 0,1409 reflete a tendência da rede a formar agrupamentos locais de colaboradores, enquanto o alto número de triângulos (608.389) e a fração de triângulos fechados (0,04564) indicam a presença de conexões fortes na comunidade. O diâmetro de 7, que representa o caminho mais curto entre quaisquer dois editores, revela que as informações podem fluir eficientemente na rede.

**Pokec Social Network: Explorando a Amizade Online**

A Pokec Social Network, uma rede social eslovaca, representa as conexões de amizade entre seus usuários. Com um número impressionante de 1.632.803 vértices e 30.622.564 arestas, a rede é substancialmente maior do que a Wikipedia Vote Network.

O coeficiente de assortatividade de -0,0511 revela uma tendência decrescente na conexão de usuários, indicando que muitos usuários têm um número limitado de conexões, enquanto alguns têm um grande número de conexões. Esta estrutura é evidenciada pelo fato de que a rede tem apenas um componente conectado, onde todos os usuários estão interconectados. O tamanho do maior componente gigante (GCC) cobre 100% dos vértices, ressaltando a força da conectividade na rede.

O coeficiente de agrupamento médio (Avg Clustering) de 0,1094 sugere uma tendência à formação de agrupamentos locais, enquanto o grande número de triângulos (32.557.458) e a fração de triângulos fechados (0,01611) destacam a presença de conexões significativas entre os usuários. O diâmetro de 11 indica que a rede permite que informações e interações fluam eficientemente, embora em um número ligeiramente maior de etapas.

**Social Circles: Twitter - Explorando a Interação Social**

A rede "Social Circles: Twitter" representa as conexões de amizade no Twitter e é composta por 81.306 vértices e 1.768.149 arestas. O coeficiente de assortatividade de -0,1406 sugere uma tendência decrescente na conexão de usuários no Twitter, refletindo a natureza seletiva de seguir ou ser seguido.

A rede do Twitter possui um único componente conectado, onde todos os usuários estão interligados, e o tamanho do maior componente gigante (GCC) também abrange 100% dos vértices, indicando uma forte unidade entre os usuários. O coeficiente de agrupamento médio (Avg Clustering) é notavelmente alto, com um valor de 0,5653, o que indica uma tendência à formação de agrupamentos locais na rede. O alto número de triângulos (13.082.506) e a fração de triângulos fechados (0,06415) evidenciam conexões fortes na comunidade do Twitter. O diâmetro de 7 demonstra que as informações podem se espalhar eficientemente na rede, com a capacidade de alcançar outros usuários em um número relativamente pequeno de etapas.

**Youtube Social Network - Explorando a Compartilhamento de Conteúdo**

A rede do YouTube representa conexões de amizade na plataforma e é composta por 1.134.890 vértices e 2.987.624 arestas. O coeficiente de assortatividade de -0,1138 reflete uma tendência decrescente na conexão de usuários no YouTube, sugerindo que a maioria dos usuários possui um número limitado de conexões.

A rede do YouTube possui apenas um componente conectado, com todos os usuários fazendo parte de um único componente gigante (GCC), destacando a forte

 unidade na rede. O coeficiente de agrupamento médio (Avg Clustering) de 0,0808 indica um nível moderado de agrupamento local na rede, com conexões significativas formadas entre os usuários. No entanto, a fração de triângulos fechados é relativamente baixa, com 0,002081, indicando que as conexões mais fortes são menos comuns. O diâmetro de 20 mostra que, em média, o caminho mais curto entre quaisquer dois usuários pode ser percorrido em um número mais substancial de etapas, refletindo a complexidade da rede do YouTube.

**Google Web Graph - Explorando a Web**

O Google Web Graph é uma representação do grafo da web usado pelo Google para indexação e pesquisa na web. A rede é composta por 875.713 vértices e 5.105.039 arestas. O coeficiente de assortatividade de -0,0959 indica uma tendência decrescente na conexão de páginas da web, sugerindo que algumas páginas têm mais conexões do que outras.

A rede do Google Web Graph possui dois componentes conectados distintos, o que significa que algumas páginas da web estão menos interconectadas do que outras. O maior componente gigante (GCC) abrange 97,7% dos vértices, destacando a força da conectividade na rede. O coeficiente de agrupamento médio (Avg Clustering) de 0,5143 sugere que a rede forma agrupamentos locais, embora não tão fortes quanto o Twitter. A presença de um grande número de triângulos (13.391.903) e uma fração de triângulos fechados (0,01911) indica conexões significativas entre as páginas da web. O diâmetro de 21 reflete a complexidade da web, com caminhos mais longos entre as páginas.

**Conclusão: Diversidade de Redes Sociais e Grafos**

Essa análise comparativa destas cinco redes sociais e grafos revela a diversidade impressionante nas estruturas e dinâmicas dessas plataformas. Cada uma delas é única, influenciada pela natureza de suas interações, tamanho e finalidade. O estudo das métricas, como a quantidade de vértices, a quantidade de arestas, o coeficiente de assortatividade, a quantidade de componentes conectados, o tamanho do maior componente gigante (GCC) e o coeficiente de agrupamento médio (Avg Clustering), nos ajuda a compreender melhor o funcionamento de cada rede.

  
