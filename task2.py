from collections import deque


graph = {
    "Central": ["North", "South", "East", "West"],
    "North": ["Central", "Park"],
    "South": ["Central", "Airport"],
    "East": ["Central", "Museum"],
    "West": ["Central", "Stadium"],
    "Park": ["North", "University"],
    "Airport": ["South"],
    "Museum": ["East", "University"],
    "Stadium": ["West", "University"],
    "University": ["Park", "Museum", "Stadium"]
}


def bfs_recursive(graph, queue, visited=None):
    if visited is None:
        visited = set()
    if not queue:
        return
    vertex = queue.popleft()
    if vertex not in visited:
        print(vertex, end=" ")
        visited.add(vertex)
        queue.extend(set(graph[vertex]) - visited)
    bfs_recursive(graph, queue, visited)


def dfs_recursive(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex, end=' ')
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)


start_node = "Central"

print("DFS (рекурсивно) шлях:")
dfs_recursive(graph, start_node)
print("\n")

print("BFS (рекурсивно) шлях:")
bfs_recursive(graph, deque([start_node]))
print("\n")
