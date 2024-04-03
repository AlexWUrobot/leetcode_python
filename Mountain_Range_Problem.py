# https://www.geeksforgeeks.org/amazon-interview-experience-for-applied-scientist-internship/#
def max_altitude_difference(heights):
    # Initialize the maximum difference to 0
    max_diff = 0
    
    # Initialize the first pointer to the first mountain
    for i in range(len(heights)):
        # Initialize the second pointer to the next mountain
        for j in range(i+1, len(heights)):
            # Calculate the altitude difference
            diff = heights[j] - heights[i]
            
            # Update the maximum difference if the current one is greater
            max_diff = max(max_diff, diff)
    
    return max_diff

# Example usage:
mountain_heights = [1, 2, 3, 4, 5, 6]
print("The maximum altitude difference is:", max_altitude_difference(mountain_heights))
