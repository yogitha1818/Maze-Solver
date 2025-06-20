import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

def visualize_maze(maze, path, start, end):
    rows, cols = len(maze), len(maze[0])
    maze_array = np.array(maze)

    # Create a color grid: 1=wall (black), 0=path (white)
    color_grid = np.zeros((rows, cols, 3))
    color_grid[maze_array == 1] = [0, 0, 0]  # Black for walls
    color_grid[maze_array == 0] = [1, 1, 1]  # White for paths

    # Mark the path in blue
    for r, c in path:
        color_grid[r, c] = [0, 0, 1]  # Blue path

    # Start in green, End in red
    sr, sc = start
    er, ec = end
    color_grid[sr, sc] = [0, 1, 0]  # Green
    color_grid[er, ec] = [1, 0, 0]  # Red

    fig, ax = plt.subplots(figsize=(cols, rows))
    ax.imshow(color_grid, interpolation='none')
    ax.set_xticks(np.arange(-0.5, cols, 1))
    ax.set_yticks(np.arange(-0.5, rows, 1))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.grid(color='black', linestyle='-', linewidth=1)
    ax.set_title("Maze Visualization")

    st.pyplot(fig)
