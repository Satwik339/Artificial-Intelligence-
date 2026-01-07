from itertools import permutations

cities = [0, 1, 2, 3]

dist = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

min_cost = float('inf')

for path in permutations(cities[1:]):
    cost = dist[0][path[0]]
    for i in range(len(path)-1):
        cost += dist[path[i]][path[i+1]]
    cost += dist[path[-1]][0]

    min_cost = min(min_cost, cost)

print("Minimum travelling cost:", min_cost)
