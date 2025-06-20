from bfs import bfs
from dfs import dfs
from astar import astar
from visualize import visualize_maze


def get_maze_from_user():
    try:
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))
    except ValueError:
        print("Invalid input. Please enter integers for rows and columns.")
        return None, None, None

    maze = []
    print("Enter the maze row by row (0 for path, 1 for wall):")
    for i in range(rows):
        while True:
            try:
                row = list(map(int, input(f"Row {i+1}: ").strip().split()))
                if len(row) != cols:
                    raise ValueError("Incorrect number of columns.")
                if any(cell not in (0, 1) for cell in row):
                    raise ValueError("Maze must only contain 0 (path) or 1 (wall).")
                maze.append(row)
                break
            except ValueError as e:
                print("Error:", e, "Try again.")

    try:
        start = tuple(map(int, input("Enter start coordinates (row col): ").strip().split()))
        end = tuple(map(int, input("Enter end coordinates (row col): ").strip().split()))
        if len(start) != 2 or len(end) != 2:
            raise ValueError("Coordinates must be two integers.")
    except ValueError as e:
        print("Error in coordinates:", e)
        return None, None, None

    # Validate start and end positions
    if not (0 <= start[0] < rows and 0 <= start[1] < cols and maze[start[0]][start[1]] == 0):
        print("Invalid start point. It must be within bounds and not a wall.")
        return None, None, None

    if not (0 <= end[0] < rows and 0 <= end[1] < cols and maze[end[0]][end[1]] == 0):
        print("Invalid end point. It must be within bounds and not a wall.")
        return None, None, None

    return maze, start, end


def main():
    print("Maze Solver using BFS, DFS, and A* Algorithms")
    maze, start, end = get_maze_from_user()

    if maze is None or start is None or end is None:
        print("Failed to load maze. Exiting.")
        return

    print("\nChoose an algorithm:")
    print("1. Breadth-First Search (BFS)")
    print("2. Depth-First Search (DFS)")
    print("3. A* Search")

    choice = input("Enter choice (1/2/3): ").strip()

    if choice == '1':
        path = bfs(maze, start, end)
        algo = "Breadth-First Search (BFS)"
    elif choice == '2':
        path = dfs(maze, start, end)
        algo = "Depth-First Search (DFS)"
    elif choice == '3':
        path = astar(maze, start, end)
        algo = "A* Search"
    else:
        print("Invalid choice.")
        return

    if path:
        print(f"\n{algo} found a path:")
        print(" → ".join(str(pos) for pos in path))
        visualize_maze(maze, path, start, end)
    else:
        print(f"\n{algo} could not find a path.")


if __name__ == "__main__":
    main()
