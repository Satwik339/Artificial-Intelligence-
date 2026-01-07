def dfs(graph, start, visited):
    visited.add(start)
    print(start, end=" ")

    for node in graph[start]:
        if node not in visited:
            dfs(graph, node, visited)

# Graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

visited = set()
dfs(graph, 'A', visited)
