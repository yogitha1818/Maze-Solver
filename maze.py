def input_maze():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    maze = []

    print("Enter the maze row by row (0 for path, 1 for wall):")
    for i in range(rows):
        while True:
            try:
                row = list(map(int, input(f"Row {i+1}: ").strip().split()))
                if len(row) != cols:
                    raise ValueError("Incorrect number of columns.")
                if any(cell not in (0, 1) for cell in row):
                    raise ValueError("Maze values must be 0 or 1.")
                maze.append(row)
                break
            except ValueError as e:
                print("Error:", e, "Try again.")

    return maze, rows, cols

def input_coordinates(prompt, max_row, max_col):
    while True:
        try:
            coords = tuple(map(int, input(prompt).strip().split()))
            if len(coords) != 2:
                raise ValueError("Enter two integers: row and column.")
            if not (0 <= coords[0] < max_row and 0 <= coords[1] < max_col):
                raise ValueError("Coordinates out of maze bounds.")
            return coords
        except ValueError as e:
            print("Error:", e, "Try again.")

def get_maze_from_user():
    maze, rows, cols = input_maze()
    start = input_coordinates("Enter start coordinates (row col): ", rows, cols)
    end = input_coordinates("Enter end coordinates (row col): ", rows, cols)
    return maze, start, end
