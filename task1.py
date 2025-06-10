import networkx as nx
import matplotlib.pyplot as plt

# Приклад: транспортна мережа (станції метро)
G = nx.Graph()

# Додаємо вершини (станції)
stations = [
    "Central", "North", "South", "East", "West",
    "Park", "Airport", "Museum", "Stadium", "University"
]
G.add_nodes_from(stations)

# Додаємо ребра (шляхи між станціями)
edges = [
    ("Central", "North"),
    ("Central", "South"),
    ("Central", "East"),
    ("Central", "West"),
    ("North", "Park"),
    ("South", "Airport"),
    ("East", "Museum"),
    ("West", "Stadium"),
    ("Park", "University"),
    ("Stadium", "University"),
    ("Museum", "University")
]
G.add_edges_from(edges)

# Візуалізація
plt.figure(figsize=(10, 6))
nx.draw(G, with_labels=True, node_color='lightblue',
        node_size=1500, font_size=12)
plt.title("Транспортна мережа міста")
plt.show()

# Аналіз характеристик
print("Кількість вершин:", G.number_of_nodes())
print("Кількість ребер:", G.number_of_edges())
print("Ступінь вершин:")
for node, degree in G.degree():
    print(f"  {node}: {degree}")
