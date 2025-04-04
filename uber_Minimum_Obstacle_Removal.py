#https://www.fastprep.io/problems/uber-minimum-obstacle-removal


def min_obstacle_removal(matrix):
    rows, cols = len(matrix), len(matrix[0])
    obstacles_removed = 0
    
    for col in range(cols):
        shape_positions = []
        obstacles_in_column = 0
        
        #print("col:---------------", col)
        # Traverse the column from bottom to top
        for row in range(rows - 1, -1, -1):
            if matrix[row][col] == "#":
                obstacles_in_column += 1
                #print("obstacles_in_column:", obstacles_in_column)
            elif matrix[row][col] == "*":
                shape_positions.append(row)
                #print("row:", shape_positions)
        
        
        
        # Determine how many obstacles need to be removed
        for shape_row in reversed(shape_positions):
            if shape_row + obstacles_in_column < rows:
                obstacles_removed += obstacles_in_column
                obstacles_in_column = 0
            else:
                obstacles_removed += (shape_row + obstacles_in_column) - (rows - 1)
    
    return obstacles_removed

# Example usage
matrix = [
    ["*", "*", "*", "*"],
    ["#", "*", ".", "*"],
    [".", ".", "#", "."],
    [".", "#", ".", "#"]
]

print(min_obstacle_removal(matrix))  # Output: 4
