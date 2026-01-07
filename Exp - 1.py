from collections import deque

goal = ((1, 2, 3),
        (4, 5, 6),
        (7, 8, 0))

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def generate_states(state):
    x, y = find_blank(state)
    new_states = []

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [list(row) for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            new_states.append(tuple(tuple(row) for row in new_state))

    return new_states

def bfs(start):
    queue = deque([(start, [])])
    visited = set()
    visited.add(start)

    while queue:
        current, path = queue.popleft()

        if current == goal:
            return path + [current]

        for state in generate_states(current):
            if state not in visited:
                visited.add(state)
                queue.append((state, path + [current]))

    return None


start = ((1, 2, 3),
         (4, 0, 6),
         (7, 5, 8))

solution = bfs(start)

for step in solution:
    for row in step:
        print(row)
    print()
