def a_star(start, goal):
    open_set = {start}
    closed_set = set()
    g = {start: 0}
    parent = {start: None}

    h = {'A': 7, 'B': 6, 'C': 2, 'D': 1, 'E': 0}

    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'D': 5},
        'C': {'D': 1},
        'D': {'E': 3},
        'E': {}
    }

    while open_set:
        current = min(open_set, key=lambda x: g[x] + h[x])

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            print("Path:", path[::-1])
            return

        open_set.remove(current)
        closed_set.add(current)

        for neighbor, cost in graph[current].items():
            if neighbor in closed_set:
                continue

            temp_g = g[current] + cost

            if neighbor not in open_set or temp_g < g.get(neighbor, float('inf')):
                parent[neighbor] = current
                g[neighbor] = temp_g
                open_set.add(neighbor)

a_star('A', 'E')
