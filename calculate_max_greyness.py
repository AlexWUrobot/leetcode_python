# https://www.fastprep.io/problems/amazon-get-max-grayness

def calculate_greyness(pixels):
    # Initialize an empty list to store the greyness values for each cell
    greyness = []
    
    # Iterate over each row in the grid of pixels
    for i in range(len(pixels)):
        # Initialize an empty string to store the greyness values for each cell in the current row
        row_greyness = ""
        
        # Iterate over each column in the current row
        for j in range(len(pixels[0])):
            # Count the number of black pixels in the current row and column
            black_row = pixels[i].count('1')
            black_column = sum(1 for k in range(len(pixels)) if pixels[k][j] == '1')
            
            # Calculate the number of white pixels in the current row and column
            white_row = len(pixels[0]) - black_row
            white_column = len(pixels) - black_column
            
            # Compute the greyness value for the current cell using the provided formula
            cell_greyness = (black_row + black_column) - (white_row + white_column)
            
            # Append the greyness value of the current cell to the string representing the current row
            row_greyness += str(cell_greyness) + " "
        
        # Append the string representing the greyness values of all cells in the current row to the list
        greyness.append(row_greyness.strip())
    
    # Return the list containing the greyness values for each cell in the grid
    return greyness

# Example usage:
pixels = ["011", "101", "001"]
result = calculate_greyness(pixels)
print(result)

array = result
# array = ['0 0 4', '0 0 4', '-2 -2 2']

# Convert string elements to integer values and flatten the array
flatten_array = [int(num) for nums in array for num in nums.split()]

# Find the maximum value
max_value = max(flatten_array)

print("The maximum value in the array is:", max_value)

# Example usage:
# pixels = ["011", "101", "001"]
pixels = ["1010", "0101", "1010"]
result = calculate_greyness(pixels)
print(result)
