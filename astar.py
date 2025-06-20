import heapq

def astar(maze, start, end):
    rows, cols = len(maze), len(maze[0])

    # Heuristic function: Manhattan distance
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    # Priority queue to explore nodes with lowest f(n) = g(n) + h(n)
    open_list = []
    heapq.heappush(open_list, (0 + heuristic(start, end), 0, start))  # (f(n), g(n), (x, y))
    
    g_cost = {start: 0}  # Cost to reach each node from start
    parent = {start: None}  # Parent node for path reconstruction

    # Directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while open_list:
        _, current_g, current = heapq.heappop(open_list)

        if current == end:
            # Reconstruct path
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]  # Reverse the path

        for dr, dc in directions:
            nr, nc = current[0] + dr, current[1] + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if maze[nr][nc] == 0:  # Only move to valid (path) cells
                    new_g = current_g + 1
                    if (nr, nc) not in g_cost or new_g < g_cost[(nr, nc)]:
                        g_cost[(nr, nc)] = new_g
                        f_cost = new_g + heuristic((nr, nc), end)
                        heapq.heappush(open_list, (f_cost, new_g, (nr, nc)))
                        parent[(nr, nc)] = current

    return None  # No path found
