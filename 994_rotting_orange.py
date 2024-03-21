

from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh_count = 0
        queue = deque()

        # Step 1: Initialize the queue with all rotten oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1

        # Step 2: Start the BFS process
        minutes_passed = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue and fresh_count > 0:
            minutes_passed += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if nx >= 0 and nx < rows and ny >= 0 and ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        queue.append((nx, ny))
                        fresh_count -= 1

        # Step 3: Check for remaining fresh oranges
        return minutes_passed if fresh_count == 0 else -1
# The time complexity of the BFS solution for the “Rotting Oranges” problem is O(N), where N is the number of cells in the grid. This is because in the worst-case scenario, each cell is visited at least once during the BFS process.
