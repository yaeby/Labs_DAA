import networkx as nx
import random
import time
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

def bfs(graph, start):
    visited = set()
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            queue.extend([n for n in graph.neighbors(node) if n not in visited])
    return visited

def dfs(graph, start):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            stack.extend([n for n in graph.neighbors(node) if n not in visited])
    return visited

# Initialize lists to store data
bfs_times = []
dfs_times = []
graph_sizes = []

# Perform empirical analysis
for i in range(10, 10001, 10):  # Generate graphs with nodes from 10 to 100 in steps of 10
    graph = generate_random_graph(i, i*2)
    graph_sizes.append(i)

    start_time = time.time()
    bfs(graph, 0)
    bfs_time = time.time() - start_time
    bfs_times.append(bfs_time)

    start_time = time.time()
    dfs(graph, 0)
    dfs_time = time.time() - start_time
    dfs_times.append(dfs_time)

# Create a DataFrame to display results
data = {'Graph Size': graph_sizes, 'BFS Time (seconds)': bfs_times, 'DFS Time (seconds)': dfs_times}
df = pd.DataFrame(data)

# Plot the results
plt.plot(graph_sizes, bfs_times, label='BFS')
plt.plot(graph_sizes, dfs_times, label='DFS')
plt.xlabel('Graph Size (Number of Nodes)')
plt.ylabel('Time (seconds)')
plt.title('Performance of BFS and DFS on Random Graphs')
plt.legend()
plt.grid(True)
plt.show()

# Display the table
print(df)
