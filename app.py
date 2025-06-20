import streamlit as st
from bfs import bfs
from dfs import dfs
from astar import astar
from visualize import visualize_maze
import matplotlib.pyplot as plt

def display_maze_grid(maze):
    for row in maze:
        st.text(" ".join(map(str, row)))

st.title("🧭 Maze Solver using BFS, DFS, A*")

rows = st.number_input("Enter number of rows:", min_value=2, value=5, step=1)
cols = st.number_input("Enter number of columns:", min_value=2, value=5, step=1)

maze = []
st.markdown("### Enter the maze row by row (0 for path, 1 for wall):")

for i in range(rows):
    row = st.text_input(f"Row {i + 1} (space-separated 0s and 1s):", value="0 " * cols)
    try:
        maze.append(list(map(int, row.strip().split())))
    except:
        st.error("Invalid input in row.")

start = st.text_input("Enter start coordinates (row col):", value="0 0")
end = st.text_input("Enter end coordinates (row col):", value=f"{rows-1} {cols-1}")

algorithm = st.selectbox("Choose an algorithm", ["Breadth-First Search (BFS)", "Depth-First Search (DFS)", "A* Search"])

if st.button("Solve Maze"):
    try:
        start = tuple(map(int, start.strip().split()))
        end = tuple(map(int, end.strip().split()))

        if not (0 <= start[0] < rows and 0 <= start[1] < cols):
            st.error("Invalid start coordinates.")
        elif not (0 <= end[0] < rows and 0 <= end[1] < cols):
            st.error("Invalid end coordinates.")
        elif maze[start[0]][start[1]] == 1 or maze[end[0]][end[1]] == 1:
            st.error("Start or end point is a wall!")
        else:
            if algorithm == "Breadth-First Search (BFS)":
                path = bfs(maze, start, end)
            elif algorithm == "Depth-First Search (DFS)":
                path = dfs(maze, start, end)
            else:
                path = astar(maze, start, end)

            if path:
                st.success(f"{algorithm} found a path: {path}")
                fig = visualize_maze(maze, path, start, end)
                st.pyplot(fig)
            else:
                st.warning(f"{algorithm} could not find a path.")

    except Exception as e:
        st.error(f"Error: {e}")