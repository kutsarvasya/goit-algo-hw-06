import networkx as nx


G = nx.Graph()
G.add_weighted_edges_from([
    ("Central", "North", 3),
    ("Central", "South", 4),
    ("Central", "East", 2),
    ("Central", "West", 5),
    ("North", "Park", 6),
    ("South", "Airport", 7),
    ("East", "Museum", 3),
    ("West", "Stadium", 4),
    ("Park", "University", 5),
    ("Stadium", "University", 6),
    ("Museum", "University", 4)
])


shortest_paths = nx.single_source_dijkstra_path(G, source="Central")
shortest_lengths = nx.single_source_dijkstra_path_length(G, source="Central")


print("Найкоротші шляхи від 'Central':")
for target in G.nodes:
    if target == "Central":
        continue
    path = shortest_paths[target]
    length = shortest_lengths[target]
    print(f"  До {target}: шлях {path}, довжина: {length}")
