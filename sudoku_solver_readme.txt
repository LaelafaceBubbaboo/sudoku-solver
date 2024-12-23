# Sudoku Solver

## Overview
This project is a Sudoku solver implemented in Python. It reads an unsolved Sudoku puzzle from a CSV file (`sudoku.csv`), solves it using a backtracking algorithm, and outputs the solution to `output.csv`. The solution is also printed to the console.

## Features
- Solves standard 9x9 Sudoku puzzles.
- Handles incomplete grids by interpreting empty cells.
- Exports the solved grid to a CSV file.
- Simple and efficient backtracking algorithm.

## Requirements
- Python 3.x

### Python Packages:
- csv (built-in)

## Installation
1. Clone or download this repository.
2. Ensure Python 3.x is installed on your system.
3. Place the Sudoku puzzle in `sudoku.csv` in the same directory as the script.

## Usage
1. Prepare a CSV file (`sudoku.csv`) containing the Sudoku puzzle:
   - Use `0` or leave cells empty for unsolved positions.
   - Ensure the grid is 9x9.

2. Run the script:
   ```bash
   python su2.py
   ```
3. If the puzzle is solvable, the solution will be printed to the console and saved to `output.csv`.
4. If no solution exists, a message will be displayed in the console.

## CSV Format Example
```
5,,3,,7,,,,
6,,8,1,9,5,,,
,,9,8,,,,6,
8,,,,6,,,,3
4,,8,,3,,1,,
7,,6,,,,2,,
,,6,,,,2,8,
,,,4,1,9,,5,
,,,8,,3,,,
```
- Empty cells are represented by empty spaces or `0`.

## How It Works
- **Grid Parsing**: The script reads the Sudoku puzzle from `sudoku.csv`.
- **Validation**: The algorithm checks if placing a number in a cell is valid by ensuring no duplicates exist in the same row, column, or 3x3 subgrid.
- **Backtracking**: The solver uses a recursive backtracking method to fill in numbers and backtrack when necessary.

## File Details
- **File**: `su2.py`
- **Created**: 12/22/2024
- **Version**: 1
- **Author**: Matt McCarter

## Notes
- The script assumes a standard 9x9 Sudoku grid.
- Large grids or complex puzzles may take longer to solve.

## License
This project is open-source and free to use under the MIT License.