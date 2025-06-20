# Utility functions for the maze solver

def is_valid_position(maze, position):
    """
    Checks if a position (row, col) is valid (within maze bounds and not a wall).
    :param maze: 2D list representing the maze (0 for path, 1 for wall)
    :param position: Tuple (row, col) representing the position to check
    :return: True if the position is valid, False otherwise
    """
    rows, cols = len(maze), len(maze[0])
    row, col = position
    return 0 <= row < rows and 0 <= col < cols and maze[row][col] == 0

def print_maze(maze):
    """
    Prints the maze in a readable format.
    :param maze: 2D list representing the maze (0 for path, 1 for wall)
    """
    for row in maze:
        print(" ".join(str(cell) for cell in row))

def is_within_bounds(maze, position):
    """
    Checks if a position is within the bounds of the maze.
    :param maze: 2D list representing the maze
    :param position: Tuple (row, col) representing the position to check
    :return: True if the position is within bounds, False otherwise
    """
    rows, cols = len(maze), len(maze[0])
    row, col = position
    return 0 <= row < rows and 0 <= col < cols

def reconstruct_path(parent, start, end):
    """
    Reconstructs the path from the start to the end using the parent dictionary.
    :param parent: Dictionary where keys are positions and values are the parent positions
    :param start: Starting position (row, col)
    :param end: Ending position (row, col)
    :return: List of positions representing the path from start to end
    """
    path = []
    current = end
    while current != start:
        path.append(current)
        current = parent.get(current)
        if current is None:  # No path found
            return None
    path.append(start)
    return path[::-1]  # Reverse the path to start from the beginning

def manhattan_distance(a, b):
    """
    Computes the Manhattan distance between two points.
    :param a: Tuple (row, col) representing the first point
    :param b: Tuple (row, col) representing the second point
    :return: Manhattan distance between a and b
    """
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
