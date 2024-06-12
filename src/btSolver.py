from bfSolver import find_combinations, print_nonogram
from inputParser import *

# fungsi pembatas
def is_valid_partial_row(row, row_hint):
    segments = []
    current_segment = 0
    for cell in row:
        if cell == 'x':
            current_segment += 1
        elif current_segment > 0:
            segments.append(current_segment)
            current_segment = 0
    if current_segment > 0:
        segments.append(current_segment)

    if len(segments) > len(row_hint):
        return False

    for i in range(len(segments)):
        if segments[i] > row_hint[i]:
            return False

    return True

def backtrackingSolver(row_hints, col_hints):
    def solve_recursive(grid, row_hints, col_hints, col_idx):
        if col_idx == len(grid[0]):
            return True

        possible_cols = find_combinations(len(col_hints), col_hints[col_idx])

        for col in possible_cols:
            # Temporarily place the column in the grid
            for row_idx in range(len(row_hints)):
                grid[row_idx][col_idx] = col[row_idx]

            valid = True
            for row_idx in range(len(row_hints)):
                if not is_valid_partial_row(grid[row_idx], row_hints[row_idx]):
                    valid = False
                    break
            if valid:
                if solve_recursive(grid, row_hints, col_hints, col_idx + 1):
                    return True

            # Backtrack
            for row_idx in range(len(row_hints)):
                grid[row_idx][col_idx] = '-'

        return False

    grid = [['-'] * len(col_hints) for _ in range(len(row_hints))]
    if solve_recursive(grid, row_hints, col_hints, 0):
        return grid
    else:
        return None

def backtrackingSolverMain(row_hints, col_hints):
    solution = backtrackingSolver(row_hints, col_hints)

    if solution != None:
        print("\n")
        print_nonogram(row_hints, col_hints, solution)
    else:
        print("\nMaaf, tidak ada solusi")
