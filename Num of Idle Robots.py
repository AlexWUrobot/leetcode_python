#https://www.fastprep.io/problems/amazon-num-idle-drives
from typing import List

def numIdleDrives(x: List[int], y: List[int]) -> int:
    # Initialize a counter for idle drives
    count = 0
    # Create a list of coordinate pairs
    coordinates = [*zip(x, y)]
    # Iterate through each coordinate pair
    for x, y in coordinates:
        # Filter coordinates where x is greater than the current x and y is the same
        x_min = list(filter(lambda a: x > a[0] and y == a[1], coordinates))
        # Filter coordinates where x is less than the current x and y is the same
        x_max = list(filter(lambda a: x < a[0] and y == a[1], coordinates))
        # Filter coordinates where y is greater than the current y and x is the same
        y_min = list(filter(lambda a: y > a[1] and x == a[0], coordinates))
        # Filter coordinates where y is less than the current y and x is the same
        y_max = list(filter(lambda a: y < a[1] and x == a[0], coordinates))
        
        # If there are non-empty lists for all four filters, increment the count
        if x_min and x_max and y_min and y_max:
            count += 1
    return count

x = [0, 0, 0, 0, 0, 1, 1, 1, 2, -1, -1, -2, -1]
y = [-1, 0, 1, 2, -2, 0, 1, -1, 0, 1, -1, 0, 0]
print(numIdleDrives(x, y))   # 5 

x = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3]
y = [1, 2, 3, 1, 2, 3, 5, 1, 2, 3]
print(numIdleDrives(x, y))   # 2
