import networkx as nx
import random
import matplotlib.pyplot as plt
import pandas as pd

def generate_random_graph(num_nodes, num_edges):
    G = nx.Graph()
    for i in range(num_nodes):
        G.add_node(i)
    edges = [(random.randint(0, num_nodes-1), random.randint(0, num_nodes-1)) for _ in range(num_edges)]
    for edge in edges:
        G.add_edge(*edge)
    return G

i = 10
graph = generate_random_graph(i, i*2)

nx.draw(graph, with_labels=True)

# Show the graph
plt.show()