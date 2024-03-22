# https://leetcode.com/discuss/interview-question/4106381/Amazon-Online-Assessment-2023/

from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Get the dimensions of the grid
        rows, cols = len(grid), len(grid[0])
        # Initialize a counter for fresh oranges
        fresh_count = 0
        # Create a queue to hold the positions of rotten oranges
        queue = deque()

        # Step 1: Populate the queue and count fresh oranges
        for r in range(rows):
            for c in range(cols):
                # If the orange is rotten, add its position to the queue
                if grid[r][c] == 2:
                    queue.append((r, c))
                # If the orange is fresh, increment the fresh count
                elif grid[r][c] == 1:
                    fresh_count += 1

        # Initialize a variable to count the minutes passed
        minutes_passed = 0
        # Define the 4-directional movements (up, down, left, right)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # Step 2: Process the queue until there are no more fresh oranges or the queue is empty
        while queue and fresh_count > 0:
            # Increment the time for each round of processing
            minutes_passed += 1
            # Process all rotten oranges at the current minute
            for _ in range(len(queue)):
                x, y = queue.popleft()
                # Check all 4 directions around the rotten orange
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    # If the adjacent orange is fresh, rot it and add to the queue
                    if nx >= 0 and nx < rows and ny >= 0 and ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        queue.append((nx, ny))
                        # Decrement the fresh count as it has now become rotten
                        fresh_count -= 1

        # Step 3: After processing, check if there are any fresh oranges left
        # If no fresh oranges remain, return the time passed; otherwise, return -1
        return minutes_passed if fresh_count == 0 else -1
        
test_class = Solution()
grid = [[2,1,1],[1,1,0],[0,1,1]]
grid = [[2,1,1],[0,1,1],[1,0,1]]
print(test_class.orangesRotting(grid))
