import networkx as nx
import matplotlib.pyplot as plt

def generate_and_visualize_random_graph(n, p):
    # Generate an Erdös-Renyi random graph
    G = nx.gnp_random_graph(n, p)
    return G

def maximum_degree_heuristic_matching(graph):
    # Create an empty set to store the matching
    matching = set()
    
    # Sort nodes by degree in descending order
    nodes_by_degree = sorted(graph.nodes(), key=lambda x: -graph.degree(x))
    
    # Iterate through the nodes and add edges to the matching
    for node in nodes_by_degree:
        if node not in matching:
            neighbor = next(iter(graph.neighbors(node)), None)
            if neighbor and neighbor not in matching:
                matching.add(node)
                matching.add(neighbor)
    
    return matching

def minimum_degree_heuristic_matching(graph):
    # Create an empty set to store the matching
    matching = set()
    
    # Sort nodes by degree in ascending order
    nodes_by_degree = sorted(graph.nodes(), key=lambda x: graph.degree(x))
    
    # Iterate through the nodes and add edges to the matching
    for node in nodes_by_degree:
        if node not in matching:
            neighbor = next(iter(graph.neighbors(node)), None)
            if neighbor and neighbor not in matching:
                matching.add(node)
                matching.add(neighbor)
    
    return matching

# Generate and visualize the random graph before matching
G = generate_and_visualize_random_graph(n=120, p=0.04)

# Display the original random graph
pos = nx.spring_layout(G, seed=42)
plt.figure(figsize=(15, 5))
plt.subplot(131)
plt.title("Original Random Graph")
nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=100)
nx.draw_networkx_labels(G, pos, font_size=8, font_color='black')
nx.draw_networkx_edges(G, pos, alpha=0.5, edge_color='gray')

# Perform Maximum Degree Heuristic matching
matching_max_degree = maximum_degree_heuristic_matching(G)

# Generate and visualize the graph after Maximum Degree Heuristic matching
G_max_degree = G.copy()
G_max_degree.remove_nodes_from(matching_max_degree)

plt.subplot(132)
plt.title("After Maximum Degree Heuristic Matching")
nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=100)
nx.draw_networkx_labels(G, pos, font_size=8, font_color='black')
nx.draw_networkx_edges(G, pos, alpha=0.5, edge_color='gray')
nx.draw_networkx_edges(G_max_degree, pos, edgelist=G.edges(), edge_color='red', width=2)

# Perform Minimum Degree Heuristic matching
matching_min_degree = minimum_degree_heuristic_matching(G)

# Generate and visualize the graph after Minimum Degree Heuristic matching
G_min_degree = G.copy()
G_min_degree.remove_nodes_from(matching_min_degree)

plt.subplot(133)
plt.title("After Minimum Degree Heuristic Matching")
nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=100)
nx.draw_networkx_labels(G, pos, font_size=8, font_color='black')
nx.draw_networkx_edges(G, pos, alpha=0.5, edge_color='gray')
nx.draw_networkx_edges(G_min_degree, pos, edgelist=G.edges(), edge_color='red', width=2)

plt.tight_layout()
plt.show()
