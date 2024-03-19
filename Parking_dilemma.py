# https://www.programmersought.com/article/51466642015/
def min_roof_length(cars, k):
    # Sort the car positions
    cars.sort()
    # Initialize the minimum length to a large number
    min_length = float('inf')
    # Iterate through the sorted list to find the minimum length
    for i in range(len(cars) - k + 1):
        # Calculate the distance between the i-th and (i+k-1)-th car
        current_length = cars[i+k-1] - cars[i] + 1
        # Update the minimum length if the current length is smaller
        min_length = min(min_length, current_length)
    return min_length

# Example usage:
cars = [2, 10, 8, 17]
k = 3
print(min_roof_length(cars, k))  # Output: 9
