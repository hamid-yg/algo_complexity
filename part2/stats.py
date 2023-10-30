import networkx as nx
import time
import random
import statistics
import matplotlib.pyplot as plt

def generate_random_graph(n, p):
    return nx.gnp_random_graph(n, p)

def maximum_degree_heuristic_matching(graph):
    matching = set()
    nodes_by_degree = sorted(graph.nodes(), key=lambda x: -graph.degree(x))
    for node in nodes_by_degree:
        if node not in matching:
            neighbor = next(iter(graph.neighbors(node)), None)
            if neighbor and neighbor not in matching:
                matching.add(node)
                matching.add(neighbor)
    return matching

def minimum_degree_heuristic_matching(graph):
    matching = set()
    nodes_by_degree = sorted(graph.nodes(), key=lambda x: graph.degree(x))
    for node in nodes_by_degree:
        if node not in matching:
            neighbor = next(iter(graph.neighbors(node)), None)
            if neighbor and neighbor not in matching:
                matching.add(node)
                matching.add(neighbor)
    return matching

# Experiment settings
num_graphs = 100
n = 120
p = 0.04

matching_sizes_max_degree = []
matching_sizes_min_degree = []
execution_times_max_degree = []
execution_times_min_degree = []

# Perform experiments on multiple random graph instances
for _ in range(num_graphs):
    random_graph = generate_random_graph(n, p)
    
    start_time = time.time()
    matching_max_degree = maximum_degree_heuristic_matching(random_graph)
    execution_time_max_degree = time.time() - start_time

    start_time = time.time()
    matching_min_degree = minimum_degree_heuristic_matching(random_graph)
    execution_time_min_degree = time.time() - start_time

    matching_sizes_max_degree.append(len(matching_max_degree))
    matching_sizes_min_degree.append(len(matching_min_degree))
    execution_times_max_degree.append(execution_time_max_degree)
    execution_times_min_degree.append(execution_time_min_degree)

# Statistical analysis
mean_matching_size_max_degree = statistics.mean(matching_sizes_max_degree)
mean_matching_size_min_degree = statistics.mean(matching_sizes_min_degree)
mean_execution_time_max_degree = statistics.mean(execution_times_max_degree)
mean_execution_time_min_degree = statistics.mean(execution_times_min_degree)

# Print and visualize the results
print("Statistical Comparison:")
print(f"Mean Matching Size (Max Degree): {mean_matching_size_max_degree}")
print(f"Mean Matching Size (Min Degree): {mean_matching_size_min_degree}")
print(f"Mean Execution Time (Max Degree): {mean_execution_time_max_degree} seconds")
print(f"Mean Execution Time (Min Degree): {mean_execution_time_min_degree} seconds")

# Create histograms to visualize matching sizes
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.hist(matching_sizes_max_degree, bins=15, alpha=0.5, label="Max Degree Heuristic")
plt.hist(matching_sizes_min_degree, bins=15, alpha=0.5, label="Min Degree Heuristic")
plt.title("Matching Sizes Distribution")
plt.xlabel("Matching Size")
plt.ylabel("Frequency")
plt.legend()

# Create histograms to visualize execution times
plt.subplot(1, 2, 2)
plt.hist(execution_times_max_degree, bins=15, alpha=0.5, label="Max Degree Heuristic")
plt.hist(execution_times_min_degree, bins=15, alpha=0.5, label="Min Degree Heuristic")
plt.title("Execution Times Distribution")
plt.xlabel("Execution Time (seconds)")
plt.ylabel("Frequency")
plt.legend()

plt.tight_layout()
plt.show()
