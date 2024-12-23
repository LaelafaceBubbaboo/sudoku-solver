# created 12/22/2024
# ver 1
# by Matt McCarter

import csv

N = 9

def printing(arr):
    """Prints the Sudoku grid to console and writes it to a CSV file."""
    with open('output.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for row in arr:
            print(" ".join(str(cell) for cell in row))
            writer.writerow(row)

def isSafe(grid, row, col, num):
    """Checks if placing 'num' at (row, col) is valid."""
    for x in range(N):
        if grid[row][x] == num:
            return False  # Check row
        if grid[x][col] == num:
            return False  # Check column

    # Check 3x3 subgrid
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True

def solveSudoku(grid, row, col):
    """Solves the Sudoku puzzle using backtracking."""
    if row == N - 1 and col == N:
        return True  # Puzzle solved

    if col == N:
        row += 1
        col = 0

    if grid[row][col] > 0:  # If cell is pre-filled
        return solveSudoku(grid, row, col + 1)

    for num in range(1, N + 1):
        if isSafe(grid, row, col, num):
            grid[row][col] = num
            if solveSudoku(grid, row, col + 1):
                return True
            grid[row][col] = 0  # Backtrack

    return False

# Read Sudoku puzzle from CSV
grid = []
with open('sudoku.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    for row in reader:
        grid_row = []
        for cell in row:
            if cell == '':
                grid_row.append(0)  # Handle empty cells
            else:
                grid_row.append(int(cell))
        grid.append(grid_row)

if solveSudoku(grid, 0, 0):
    printing(grid)
else:
    print("No solution exists")