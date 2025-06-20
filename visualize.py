import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

def visualize_maze(maze, path, start, end):
    rows, cols = len(maze), len(maze[0])
    maze_array = np.array(maze)

    # Initialize color grid (white for path, black for walls)
    color_grid = np.zeros((rows, cols, 3))
    color_grid[maze_array == 1] = [0, 0, 0]  # Walls = Black
    color_grid[maze_array == 0] = [1, 1, 1]  # Path = White

    # Mark path = Blue
    for r, c in path:
        color_grid[r, c] = [0, 0, 1]

    # Mark Start = Green, End = Red
    color_grid[start[0], start[1]] = [0, 1, 0]
    color_grid[end[0], end[1]] = [1, 0, 0]

    # ✅ Create a new figure and pass it to Streamlit
    fig, ax = plt.subplots(figsize=(cols, rows))
    ax.imshow(color_grid, interpolation='none')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title("Maze Path Visualization")

    st.pyplot(fig)  # ✅ FIXED: Pass fig to st.pyplot
