def min_changes_to_y(matrix):
    n = len(matrix)
    possible_pairs = [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]
    min_changes = float('inf')
    
    for y_val, bg_val in possible_pairs:
        changes = 0
        for i in range(n):
            for j in range(n):
                if (j == i and i < n // 2) or (j == n - i - 1 and i < n // 2) or (j == n // 2 and i >= n // 2):
                    if matrix[i][j] != y_val:
                        changes += 1
                else:
                    if matrix[i][j] != bg_val:
                        changes += 1
        min_changes = min(min_changes, changes)
    
    return min_changes

# Example usage:
matrix = [
    [2, 0, 0, 0, 2],
    [1, 2, 1, 2, 0],
    [0, 1, 2, 1, 0],
    [0, 0, 2, 1, 1],
    [1, 1, 2, 1, 1]
]
print(min_changes_to_y(matrix))  # Output: 8
