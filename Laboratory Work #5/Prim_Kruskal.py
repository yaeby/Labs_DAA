import numpy as np
import time
import matplotlib.pyplot as plt

# Prim's Algorithm
def prim(graph):
    n = len(graph)
    mst = [None] * n  # MST to store the constructed MST
    key = [float('inf')] * n  # Key values used to pick minimum weight edge in cut
    visited = [False] * n  # To represent set of vertices not yet included in MST

    # Always include first 0th vertex in MST.
    key[0] = 0
    mst[0] = -1  # First node is always root of MST

    for _ in range(n-1):
        # Pick the minimum key vertex from the set of vertices not yet included in MST
        u = min_key_vertex(key, visited)
        visited[u] = True

        # Update key and mst for adjacent vertices of the picked vertex
        for v in range(n):
            if 0 < graph[u][v] < key[v] and not visited[v]:
                mst[v] = u
                key[v] = graph[u][v]

    return mst

def min_key_vertex(key, visited):
    min_val = float('inf')
    min_index = -1

    for v in range(len(key)):
        if key[v] < min_val and not visited[v]:
            min_val = key[v]
            min_index = v

    return min_index

# Kruskal's Algorithm
class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        u_root = self.find(u)
        v_root = self.find(v)

        if u_root == v_root:
            return False

        if self.rank[u_root] < self.rank[v_root]:
            self.parent[u_root] = v_root
        elif self.rank[u_root] > self.rank[v_root]:
            self.parent[v_root] = u_root
        else:
            self.parent[v_root] = u_root
            self.rank[u_root] += 1

        return True

def kruskal(graph):
    n = len(graph)
    result = []
    ds = DisjointSet(n)

    edges = []
    for i in range(n):
        for j in range(i+1, n):
            if graph[i][j] > 0:
                edges.append((i, j, graph[i][j]))

    edges.sort(key=lambda x: x[2])

    for edge in edges:
        u, v, weight = edge
        if ds.union(u, v):
            result.append(edge)

    return result

# Generate Graphs
def generate_graph(size):
    graph = np.random.randint(1, 100, size=(size, size))
    for i in range(size):
        graph[i][i] = 0  # No self-loops
        for j in range(i+1, size):
            graph[j][i] = graph[i][j]  # Symmetric matrix for undirected graph
    return graph

# Benchmarking
def benchmark_algorithms(graph_sizes):
    prim_times = []
    kruskal_times = []

    for size in graph_sizes:
        graph = generate_graph(size)

        # Prim's Algorithm
        start_time = time.time()
        prim(graph)
        end_time = time.time()
        prim_times.append(end_time - start_time)

        # Kruskal's Algorithm
        start_time = time.time()
        kruskal(graph)
        end_time = time.time()
        kruskal_times.append(end_time - start_time)

    return prim_times, kruskal_times

# Graph Sizes
graph_sizes = [10, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1500, 2000]

# Benchmarking
prim_times, kruskal_times = benchmark_algorithms(graph_sizes)

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(graph_sizes, prim_times, marker='o', label="Prim's Algorithm")
plt.plot(graph_sizes, kruskal_times, marker='o', label="Kruskal's Algorithm")
plt.title('Empirical Analysis of Prim and Kruskal Algorithms')
plt.xlabel('Number of Nodes')
plt.ylabel('Execution Time (s)')
plt.legend()
plt.grid(True)
plt.show()
