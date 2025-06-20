import matplotlib.pyplot as plt
import numpy as np

def visualize_maze(maze, path, start, end):
    """
    Visualizes the maze and the path found by the algorithm.
    :param maze: 2D list representing the maze (0 for path, 1 for wall)
    :param path: List of (row, col) tuples representing the path
    :param start: Tuple (row, col) representing the start point
    :param end: Tuple (row, col) representing the end point
    """
    # Convert maze to a numpy array for easier manipulation
    maze_array = np.array(maze)

    # Create a plot
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_xticks(np.arange(maze_array.shape[1] + 1) - 0.5, minor=True)
    ax.set_yticks(np.arange(maze_array.shape[0] + 1) - 0.5, minor=True)
    ax.grid(which="minor", color="black", linestyle='-', linewidth=2)

    # Set the maze grid: 1 for walls (black), 0 for open paths (white)
    ax.imshow(maze_array, cmap="binary", origin="upper")

    # Highlight the start and end points
    ax.plot(start[1], start[0], marker='o', color='green', markersize=10, label='Start')
    ax.plot(end[1], end[0], marker='x', color='red', markersize=10, label='End')

    # Highlight the path if there is one
    if path:
        path_rows, path_cols = zip(*path)
        ax.plot(path_cols, path_rows, color='blue', linewidth=2, label='Path')

    # Add a legend
    ax.legend(loc='upper left')

    # Display the plot
    plt.title("Maze Visualization")
    plt.show()
