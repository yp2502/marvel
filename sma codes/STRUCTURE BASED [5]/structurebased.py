import networkx as nx
import matplotlib.pyplot as plt

# Step 1: Create a graph
G = nx.Graph()

# Step 2: Add nodes (Users in a social network)
users = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"]
G.add_nodes_from(users)

# Step 3: Add edges (Connections between users)
edges = [("Alice", "Bob"), ("Alice", "Charlie"), ("Bob", "David"),
         ("Charlie", "David"), ("David", "Eve"), ("Eve", "Frank"),
         ("Bob", "Eve"), ("Charlie", "Frank")]
G.add_edges_from(edges)

# Step 4: Display edges
print("\nEdges in the Graph:", list(G.edges))

# Step 5: Draw the Graph with better styling
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G, seed=42)  # Better layout
nx.draw(G, pos, with_labels=True, node_size=3000, node_color="skyblue",
        edge_color="gray", font_size=12, font_weight="bold")
plt.title("Social Media Network Graph", fontsize=14)
plt.show()

# Step 6: Calculate centrality measures
degree_centrality = nx.degree_centrality(G)
closeness_centrality = nx.closeness_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)
eigenvector_centrality = nx.eigenvector_centrality(G)

# Step 7: Find most influential user (highest degree centrality)
most_influential = max(degree_centrality, key=degree_centrality.get)

# Step 8: Find graph density
graph_density = nx.density(G)

# Step 9: Find cliques
cliques = list(nx.find_cliques(G))

# Step 10: Ego graph (connections of a specific user)
ego_user = "Bob"  # Choose a user to analyze their network
ego_G = nx.ego_graph(G, ego_user)

plt.figure(figsize=(6, 5))
nx.draw(ego_G, with_labels=True, node_color="lightgreen", edge_color="black",
        font_size=12, font_weight="bold")
plt.title(f"Ego Graph of {ego_user}", fontsize=14)
plt.show()

# Step 11: Find if the graph has bridges (critical connections)
has_bridges = nx.has_bridges(G)

# Step 12: Display Results with Formatting
print("\nNetwork Analysis Results")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print(f"Most Influential User: {most_influential}")
print(f"Graph Density: {graph_density:.4f}")
print(f"Does the Graph Have Bridges? {'Yes' if has_bridges else 'No'}")
print("\nCentrality Scores:")

for user in G.nodes():
    print(f"\n{user}:")
    print(f" - Degree Centrality: {degree_centrality[user]:.4f}")
    print(f" - Closeness Centrality: {closeness_centrality[user]:.4f}")
    print(f" - Betweenness Centrality: {betweenness_centrality[user]:.4f}")
    print(f" - Eigenvector Centrality: {eigenvector_centrality[user]:.4f}")

print("\nCliques (Groups of closely connected users):")
for idx, clique in enumerate(cliques, 1):
    print(f"  Clique {idx}: {clique}")
