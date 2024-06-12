from inputParser import *

def find_combinations(n, hints):
    results = []

    if len(hints) == 1:
        temp_results = []
        subset_length = hints[0]
        for i in range(n - subset_length + 1):
            temp_array = ['-'] * n
            for j in range(subset_length):
                temp_array[i + j] = 'x'
            temp_results.append(temp_array)
        results = temp_results.copy()
    else:
        def generate_multiple_combinations(start, hint_idx, temp_array):
            if hint_idx == len(hints):
                results.append(temp_array.copy())
                return

            subset_length = hints[hint_idx]
            for i in range(start, n - subset_length + 1):
                valid = True
                for j in range(subset_length):
                    if temp_array[i + j] == 'x' or (i + j > 0 and temp_array[i + j - 1] == 'x') or (i + j < n - 1 and temp_array[i + j + 1] == 'x'):
                        valid = False
                        break
                if valid:
                    for j in range(subset_length):
                        temp_array[i + j] = 'x'
                    generate_multiple_combinations(i + subset_length + 1, hint_idx + 1, temp_array)
                    for j in range(subset_length):
                        temp_array[i + j] = '-'
        
        generate_multiple_combinations(0, 0, ['-'] * n)
    
    return results

def cartesian_product(arrays):
    if not arrays:
        return [[]]
    result = [[]]
    for array in arrays:
        new_result = []
        for item in array:
            for prev in result:
                new_result.append(prev + [item])
        result = new_result
    return result

def validate_combinations(row_combinations, col_combinations):
    for i in range(len(row_combinations)):
        for j in range(len(col_combinations)):
            if satisfies_clues(row_combinations[i], col_combinations[j]):
                return row_combinations[i]
    return None

def satisfies_clues(row_combination, col_combination):
    for i in range(len(row_combination)):
        for j in range (len(col_combination)):
            if row_combination[i][j] != col_combination[j][i]:
                return False
    return True

def print_nonogram(row_hints, col_hints, solution):
    max_row_hint_length = max(len(hint) for hint in row_hints)
    max_col_hint_length = max(len(hint) for hint in col_hints)
    
    hint_space = 3 
    row_hint_space = max_row_hint_length * hint_space

    for i in range(max_col_hint_length):
        row_hint_line = ' ' * (row_hint_space)
        for col_hint in col_hints:
            if len(col_hint) >= max_col_hint_length - i:
                row_hint_line += f"{col_hint[len(col_hint) - max_col_hint_length + i]:>{hint_space}}"
            else:
                row_hint_line += ' ' * hint_space
        print(row_hint_line)

    for row_hint, row in zip(row_hints, solution):
        row_hint_line = ' '.join(map(str, row_hint)).rjust(row_hint_space)
        solution_line = ' '.join([' ■' if cell == 'x' else ' x' for cell in row])  # Ensure consistent cell width
        print(f"{row_hint_line} {solution_line}")

def bruteforceSolver(row_hints, col_hints, n):
    row_combination = []
    col_combination = []

    for row in row_hints:
        row_combination.append(find_combinations(n, row))

    for col in col_hints:
        col_combination.append(find_combinations(n, col))

    row_combinations = cartesian_product(row_combination)
    col_combinations = cartesian_product(col_combination)

    result = validate_combinations(row_combinations, col_combinations)

    if result != None:
        print("\n")
        print_nonogram(row_hints, col_hints, result)
    else:
        print("\nMaaf, tidak ada solusi")

# print(find_combinations(5, [2,2]))