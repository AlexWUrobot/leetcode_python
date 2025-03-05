# Compute Minimum Total Distance

# https://chatgpt.com/share/67c84fba-d0d8-8005-831f-a10e1e748138
# https://www.fastprep.io/problems/amazon-get-min-total-distance

from typing import List

def compute_minimum_total_distance(distribution_center_locations):
    # Sort the distribution centers
    distribution_center_locations.sort()
    n = len(distribution_center_locations)
    
    # Initialize the minimum distance sum to a large number
    min_distance_sum = float('inf')
    
    # Helper function to compute the median
    def median(arr, start, end):
        length = end - start + 1
        if length % 2 == 0:
            return (arr[start + length // 2 - 1] + arr[start + length // 2]) // 2
        else:
            return arr[start + length // 2]
    
    # Try different partition points
    for i in range(1, n):
        median1 = median(distribution_center_locations, 0, i - 1)
        median2 = median(distribution_center_locations, i, n - 1)
        
        current_distance_sum = 0
        
        for center in distribution_center_locations:
            distance_to_closest_warehouse = min(abs(center - median1), abs(center - median2))
            current_distance_sum += distance_to_closest_warehouse
        
        min_distance_sum = min(min_distance_sum, current_distance_sum)
    
    return min_distance_sum


# Example usage
distribution_center_locations = [1, 2, 3]
print(compute_minimum_total_distance(distribution_center_locations))  # Output: 1


# Example usage
distribution_center_locations = [1, 6]
print(compute_minimum_total_distance(distribution_center_locations))  
# Output: 0


# Example usage
distribution_center_locations = [1, 2, 5, 6]
print(compute_minimum_total_distance(distribution_center_locations))   
# Output: 2
