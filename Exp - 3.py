from collections import deque

def water_jug(jug1, jug2, target):
    visited = set()
    q = deque([(0, 0)])

    while q:
        x, y = q.popleft()

        if x == target or y == target:
            print("Solution Found:", (x, y))
            return

        if (x, y) in visited:
            continue
        visited.add((x, y))

        q.extend([
            (jug1, y),            
            (x, jug2),            
            (0, y),               
            (x, 0),               
            (min(jug1, x+y), max(0, x+y-jug1)),  
            (max(0, x+y-jug2), min(jug2, x+y))    
        ])

    print("No Solution")

water_jug(4, 3, 2)
