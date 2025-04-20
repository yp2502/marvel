import networkx as nx
import matplotlib.pyplot as plt


# Create a directed graph
G = nx.DiGraph()


# Adding nodes (Users in social media)
users = ["Alice", "Bob", "Charlie", "David", "Eve"]
G.add_nodes_from(users)


# Adding edges (Relationships: Follows, Likes, Mentions)
edges = [("Alice", "Bob"), ("Bob", "Charlie"), ("Charlie", "David"),
         ("David", "Eve"), ("Eve", "Alice"), ("Alice", "Charlie"),
         ("Bob", "Eve"), ("Charlie", "Alice")]
G.add_edges_from(edges)


# Calculate centrality measures
degree_centrality = nx.degree_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)
eigenvector_centrality = nx.eigenvector_centrality(G)


# Display centrality measures
print("Degree Centrality:", degree_centrality)
print("Betweenness Centrality:", betweenness_centrality)
print("Eigenvector Centrality:", eigenvector_centrality)


# Draw the network
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)  # Positioning nodes visually
nx.draw(G, pos, with_labels=True, node_color='skyblue', edge_color='gray', node_size=2000, font_size=10)
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): 'follows' for u, v in edges})
plt.title("Social Media Network Graph")
plt.show()