def print_grid(grid):
    for row in grid:
        print(" ".join(str(num) for num in row))


def find_empty(grid):
    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0:
                return r, c

    return None


def is_valid(grid, row, col, num):

    for c in range(9):
        if grid[row][c] == num:
            return False

    for r in range(9):
        if grid[r][col] == num:
            return False

    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if grid[r][c] == num:
                return False

    return True


def solve_sudoku(grid):

    empty = find_empty(grid)

    if empty is None:
        return True

    row, col = empty

    for num in range(1, 10):

        if is_valid(grid, row, col, num):
            grid[row][col] = num

            if solve_sudoku(grid):
                return True

            grid[row][col] = 0

    return False


print("Enter the Sudoku grid row by row.")
print("Use 0 for empty cells and spaces between numbers.")

grid = []

for i in range(9):
    row = list(map(int, input(f"Row {i + 1}: ").split()))

    if len(row) != 9 or any(num < 0 or num > 9 for num in row):
        print("Invalid row. Enter exactly 9 numbers from 0 to 9.")
        raise SystemExit

    grid.append(row)

valid_input = True

for r in range(9):
    for c in range(9):
        num = grid[r][c]

        if num != 0:
            grid[r][c] = 0

            if not is_valid(grid, r, c, num):
                valid_input = False

            grid[r][c] = num

if not valid_input:
    print("The given Sudoku grid contains conflicting numbers.")

else:
    print("\nOriginal Sudoku:")
    print_grid(grid)

    if solve_sudoku(grid):
        print("\nSolved Sudoku:")
        print_grid(grid)
    else:
        print("No solution exists for this Sudoku grid.")