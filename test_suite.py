import networkx as nx
import numpy as np

n = np.random.randint(0, 10000, size = (10000,2))

np.savetxt('/Users/georgeberry/Google Drive/networkj/graph.csv', n, delimiter=",")

n = np.genfromtxt('/Users/georgeberry/Google Drive/networkj/graph.csv', delimiter=",")

g = nx.Graph()

for row in n:
    g.add_edge(*list(row))

gg = g.subgraph([1., 386., 611., 836., 741.])

print(nx.number_connected_components(g))