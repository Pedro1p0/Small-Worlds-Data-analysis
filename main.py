import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns

# Crie uma lista vazia chamada 'graphs' para armazenar os gráficos
graphs = []

# Carregue o segundo grafo a partir de um arquivo de lista de adjacência
graph2 = nx.read_adjlist("soc-pokec-relationships.txt")

# Adicione o segundo grafo à lista 'graphs'
graphs.append(graph2)

# Calcule a média do grau dos vizinhos de cada nó no grafo
degree2, avg_neigh_degree2 = zip(*nx.average_degree_connectivity(graph2).items())

# Converta as tuplas em listas separadas
degree2 = list(degree2)
avg_neigh_degree2 = list(avg_neigh_degree2)

# Configurar o estilo do gráfico
plt.style.use("fivethirtyeight")

# Crie uma figura e eixo para o gráfico
fig, ax = plt.subplots(1, 1, figsize=(12, 8))

# Crie um gráfico de dispersão usando Seaborn com os graus dos nós no eixo x e a média dos graus dos vizinhos no eixo y
sns.regplot(x=degree2, y=avg_neigh_degree2, ax=ax)

# Defina rótulos dos eixos
ax.set_xlabel("Grau do Nó")
ax.set_ylabel("Grau Médio dos Vizinhos") 

# Limite o eixo x para começar em 0 e estender para valores não especificados
ax.set_xlim(0, None)

# Exiba o gráfico
plt.show()
