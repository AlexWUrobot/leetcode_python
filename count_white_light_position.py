def count_white_positions(n, m, lights):
    # Initialize lights array
    lights_array = [0] * n

    # Update lights array
    for i in range(m):
        color, left, right = lights[i]
        for j in range(left - 1, right):
            lights_array[j] += color

    # Count white positions
    count = 0
    for i in range(n):
        if lights_array[i] == 6:
            count += 1

    return count

# Example usage
n = 5
m = 3
lights = [[1, 1, 5], [2, 2, 5], [3, 3, 5]]
print(count_white_positions(n, m, lights))  # Output: 3
