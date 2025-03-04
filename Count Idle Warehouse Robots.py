# https://www.fastprep.io/problems/1.amazon-num-idle-drives
from typing import List

class Solution:
    def numIdleDrives(self, x: List[int], y: List[int]) -> int:
        # Build maps to store the range of robots for each coordinate
        x_map = {}  # key: y-coord, value: (leftmost x, rightmost x)
        y_map = {}  # key: x-coord, value: (lowest y, highest y)
        
        # Build the maps
        for i in range(len(x)):
            curr_x, curr_y = x[i], y[i]
            
            # Update x_map
            if curr_y in x_map:
                left, right = x_map[curr_y]
                x_map[curr_y] = (min(left, curr_x), max(right, curr_x))
            else:
                x_map[curr_y] = (curr_x, curr_x)
            
            # Update y_map
            if curr_x in y_map:
                down, up = y_map[curr_x]
                y_map[curr_x] = (min(down, curr_y), max(up, curr_y))
            else:
                y_map[curr_x] = (curr_y, curr_y)
        
        # Count idle robots
        idle_count = 0
        for i in range(len(x)):
            curr_x, curr_y = x[i], y[i]
            
            # Check if robot is enclosed
            if curr_y in x_map and curr_x in y_map:
                left, right = x_map[curr_y]
                down, up = y_map[curr_x]
                
                # Robot is idle if there are robots to its left, right, above, and below
                if left < curr_x and curr_x < right and down < curr_y and curr_y < up:
                    idle_count += 1
        
        return idle_count
        
        
# Example usage
solution = Solution()
x = [0, 0, 0, 0, 0, 1, 1, 1, 2, -1, -1, -2, -1]
y = [-1, 0, 1, 2, -2, 0, 1, -1, 0, 1, -1, 0, 0]
print(solution.numIdleDrives(x,y))

x = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3]
y = [1, 2, 3, 1, 2, 3, 5, 1, 2, 3]
print(solution.numIdleDrives(x,y))

