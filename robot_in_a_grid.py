

# DFS (Depth-First Search)
# The time complexity is O(mxn). mxn are the number of rows and columns of the grid, respectively.
from typing import List
from collections import deque

class Solution:
    # Function to find a path through a grid with obstacles
    def DFS_method(self, obstacleGrid: List[List[int]]) -> List[List[int]]:
        # Depth-first search (DFS) function to explore possible paths
        def dfs(i, j):
            # Base case: if out of bounds or on an obstacle, return False
            if i >= m or j >= n or obstacleGrid[i][j] == -1:
                return False
            # Record the current position as part of the path
            ans.append([i, j])
            # Mark the current cell as visited by setting it to -1
            obstacleGrid[i][j] = -1
            # If the bottom-right cell is reached, or if a path is found from the right or down cell, return True
            if (i == m - 1 and j == n - 1) or dfs(i + 1, j) or dfs(i, j + 1):
                return True
            # If no path is found, remove the current position from the path and backtrack
            ans.pop()
            return False

        # Get the dimensions of the grid
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        # Initialize the answer list to record the path
        ans = []
        # Start the DFS from the top-left cell; return the path if found, else return an empty list
        return (ans ,"Yes") if dfs(0, 0) else ([], "No")
        
    def BFS_method(self, obstacleGrid: List[List[int]]) -> List[List[int]]:
        # Define the dimensions of the grid
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        # Check if the starting or ending point is an obstacle
        if obstacleGrid[0][0] == -1 or obstacleGrid[m - 1][n - 1] == -1:
            return []
        
        # Initialize the queue with the starting point and the path taken so far
        queue = deque([([0, 0], [[0, 0]])])
        
        # Mark the starting point as visited
        obstacleGrid[0][0] = -1
        
        # Define the directions in which the robot can move
        directions = [(1, 0), (0, 1)]  # Down, Right
        
        # Loop until the queue is empty
        while queue:
            # Get the current position and path from the queue
            (x, y), path = queue.popleft()
            
            # Check if we have reached the destination
            if x == m - 1 and y == n - 1:
                return path  # Return the path taken to reach the destination
            
            # Explore the neighboring cells
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                # Check if the new position is within bounds and not an obstacle
                if 0 <= nx < m and 0 <= ny < n and obstacleGrid[nx][ny] == 0:
                    # Add the new position to the queue with the updated path
                    queue.append(([nx, ny], path + [[nx, ny]]))
                    
                    # Mark the new position as visited
                    obstacleGrid[nx][ny] = -1
        
        # If no path is found, return an empty list
        return []    
        
        
        
test = Solution()

case1 = [[ 0, 0, 0, -1, 0], 
        [-1, 0, 0, -1, -1], 
        [ 0, 0, 0, -1, 0], 
        [-1, 0, 0, 0, 0], 
        [ 0, 0, -1, 0, 0]]
print(" path:", test.DFS_method(case1))
# case1 = [[ 0, 0, 0, -1, 0], 
#         [-1, 0, 0, -1, -1], 
#         [ 0, 0, 0, -1, 0], 
#         [-1, 0, 0, 0, 0], 
#         [ 0, 0, -1, 0, 0]]
# print("BFS path:", test.BFS_method(case1))
case2 = [[ 0, 0, 0, 0, 0], 
        [-1, 0, 0, -1, -1], 
        [ 0, 0, 0, -1, 0], 
        [-1, 0, 0, 0, 0], 
        [ 0, 0, -1, 0, 0]]
print(" path:", test.DFS_method(case2))
# case2 = [[ 0, 0, 0, 0, 0], 
#         [-1, 0, 0, -1, -1], 
#         [ 0, 0, 0, -1, 0], 
#         [-1, 0, 0, 0, 0], 
#         [ 0, 0, -1, 0, 0]]
# print("BFS path:", test.BFS_method(case2))
case3 = [[ 0, 0, 0, 0, 0], 
        [-1, 0, -1, -1, 0], 
        [ 0, -1, 0, -1, 0], 
        [-1, 0, 0, 0, 0], 
        [ 0, 0, -1, 0, 0]]
print(" path:", test.DFS_method(case3))
# case3 = [[ 0, 0, 0, 0, 0], 
#         [-1, 0, -1, -1, 0], 
#         [ 0, -1, 0, -1, 0], 
#         [-1, 0, 0, 0, 0], 
#         [ 0, 0, -1, 0, 0]]
# print("BFS path:", test.BFS_method(case3))
case3 = [[ 0, 0, 0, -1, 0], 
         [-1, 0, 0, -1, -1], 
         [ 0, 0, 0, -1, 0], 
         [-1, 0, -1, 0, 0], 
         [ 0, 0, -1, 0, 0]]
print(" path:", test.DFS_method(case3))

# case3 = [[ 0, 0, 0, -1, 0], 
#          [-1, 0, 0, -1, -1], 
#          [ 0, 0, 0, -1, 0], 
#          [-1, 0, -1, 0, 0], 
#          [ 0, 0, -1, 0, 0]]
# print("BFS path:", test.BFS_method(case3))
# similar to 200. number of island 
# similar to 130, 286, 994 rotting oragne
# https://doocs.github.io/leetcode/en/lcci/8.2/#description
