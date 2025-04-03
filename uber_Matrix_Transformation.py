# https://www.fastprep.io/problems/uber-matrix-transformation

from typing import List

def rotate_90_clockwise(matrix: List[List[int]]) -> List[List[int]]:
    """Rotates the matrix 90 degrees clockwise."""
    return [list(row) for row in zip(*matrix[::-1])]

def reflect_main_diagonal(matrix: List[List[int]]) -> List[List[int]]:
    """Reflects the matrix along its main diagonal."""
    return [list(row) for row in zip(*matrix)]

def reflect_secondary_diagonal(matrix: List[List[int]]) -> List[List[int]]:
    """Reflects the matrix along its secondary diagonal."""
    n = len(matrix)
    return [[matrix[n - 1 - j][n - 1 - i] for j in range(n)] for i in range(n)]

def transform_matrix(matrix: List[List[int]], queries: List[int]) -> List[List[int]]:
    """Applies transformations to the matrix based on queries."""
    for q in queries:
        if q == 0:
            matrix = rotate_90_clockwise(matrix)
        elif q == 1:
            matrix = reflect_main_diagonal(matrix)
        elif q == 2:
            matrix = reflect_secondary_diagonal(matrix)
    return matrix

# Example usage
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
q = [0, 1, 2]
print(transform_matrix(a, q))
