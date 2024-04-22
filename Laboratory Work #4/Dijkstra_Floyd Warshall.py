import numpy as np
import time
import matplotlib.pyplot as plt

# Dijkstra's Algorithm
def min_distance(dist, visited):
    min_dist = float('inf')
    min_index = -1

    for i in range(len(dist)):
        if dist[i] < min_dist and not visited[i]:
            min_dist = dist[i]
            min_index = i

    return min_index

def dijkstra(graph, start):
    n = len(graph)
    dist = [float('inf')] * n
    dist[start] = 0
    visited = [False] * n

    for _ in range(n):
        u = min_distance(dist, visited)
        visited[u] = True

        for v in range(n):
            if graph[u][v] > 0 and not visited[v] and dist[v] > dist[u] + graph[u][v]:
                dist[v] = dist[u] + graph[u][v]

    return dist

# Floyd-Warshall Algorithm
def floyd_warshall(graph):
    n = len(graph)
    dist = np.copy(graph)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

# Generate Sparse Graph
def generate_sparse_graph(size):
    graph = np.random.randint(1, 100, size=(size, size)) * np.random.choice([0, 1], size=(size, size))
    return graph

# Generate Dense Graph
def generate_dense_graph(size):
    graph = np.random.randint(1, 100, size=(size, size))
    return graph

# Benchmarking
def benchmark_algorithms(graph_sizes):
    dijkstra_times_sparse = []
    floyd_warshall_times_sparse = []
    dijkstra_times_dense = []
    floyd_warshall_times_dense = []

    for size in graph_sizes:
        sparse_graph = generate_sparse_graph(size)
        dense_graph = generate_dense_graph(size)

        # Dijkstra's Algorithm for sparse graph
        start_time = time.time()
        dijkstra(sparse_graph, 0)  # Starting from node 0
        end_time = time.time()
        dijkstra_times_sparse.append(end_time - start_time)

        # Dijkstra's Algorithm for dense graph
        start_time = time.time()
        dijkstra(dense_graph, 0)  # Starting from node 0
        end_time = time.time()
        dijkstra_times_dense.append(end_time - start_time)

        # Floyd-Warshall Algorithm for sparse graph
        start_time = time.time()
        floyd_warshall(sparse_graph)
        end_time = time.time()
        floyd_warshall_times_sparse.append(end_time - start_time)

        # Floyd-Warshall Algorithm for dense graph
        start_time = time.time()
        floyd_warshall(dense_graph)
        end_time = time.time()
        floyd_warshall_times_dense.append(end_time - start_time)

    return dijkstra_times_sparse, floyd_warshall_times_sparse, dijkstra_times_dense, floyd_warshall_times_dense

# Graph Sizes
graph_sizes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 150, 200, 250, 300]

# Benchmarking
dijkstra_times_sparse, floyd_warshall_times_sparse, dijkstra_times_dense, floyd_warshall_times_dense = benchmark_algorithms(graph_sizes)

# Plotting
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(graph_sizes, dijkstra_times_sparse, marker='o', label='Dijkstra (Sparse)')
plt.plot(graph_sizes, floyd_warshall_times_sparse, marker='o', label='Floyd-Warshall (Sparse)')
plt.title('Sparse Graph')
plt.xlabel('Number of Nodes')
plt.ylabel('Execution Time (s)')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(graph_sizes, dijkstra_times_dense, marker='o', label='Dijkstra (Dense)')
plt.plot(graph_sizes, floyd_warshall_times_dense, marker='o', label='Floyd-Warshall (Dense)')
plt.title('Dense Graph')
plt.xlabel('Number of Nodes')
plt.ylabel('Execution Time (s)')
plt.legend()

plt.tight_layout()
plt.show()
