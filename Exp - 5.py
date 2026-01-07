from collections import deque

def is_valid(m, c):
    return (m == 0 or m >= c) and (3-m == 0 or 3-m >= 3-c)

def missionaries_cannibals():
    start = (3, 3, 0)   
    goal = (0, 0, 1)

    moves = [(2,0),(0,2),(1,1),(1,0),(0,1)]
    q = deque([(start, [])])
    visited = set()

    while q:
        (m, c, b), path = q.popleft()

        if (m, c, b) == goal:
            for step in path + [(m, c, b)]:
                print(step)
            return

        if (m, c, b) in visited:
            continue
        visited.add((m, c, b))

        for dm, dc in moves:
            if b == 0:   
                nm, nc = m - dm, c - dc
            else:       
                nm, nc = m + dm, c + dc

            if 0 <= nm <= 3 and 0 <= nc <= 3 and is_valid(nm, nc):
                q.append(((nm, nc, 1-b), path + [(m, c, b)]))

missionaries_cannibals()
