from typing import List


def dfs_method(obstacleGrid: List[List[int]]) -> List[List[int]]:
    m, n = len(obstacleGrid), len(obstacleGrid[0])

    # Quick check for invalid start or destination
    if obstacleGrid[0][0] == -1 or obstacleGrid[m - 1][n - 1] == -1:
        return []

    ans = []

    def dfs(i, j):
        # Base case: out of bounds or on an obstacle
        if i >= m or j >= n or obstacleGrid[i][j] == -1:
            return False

        ans.append([i, j])
        obstacleGrid[i][j] = -1  # Mark visited

        # Reached target, or valid path exists moving Down or Right
        if (i == m - 1 and j == n - 1) or dfs(i + 1, j) or dfs(i, j + 1):
            return True

        ans.pop()  # Backtrack
        return False

    return ans if dfs(0, 0) else []


# Test case
case1 = [
    [0, 0, 0, -1, 0],
    [-1, 0, 0, -1, -1],
    [0, 0, 0, -1, 0],
    [-1, 0, 0, 0, 0],
    [0, 0, -1, 0, 0],
]

print("path:", dfs_method(case1))











from collections import deque

def find_path(grid):
    m, n = len(grid), len(grid[0])
    if grid[0][0] == 1 or grid[-1][-1] == 1:
        return []

    parent = {(0, 0): None}
    queue = deque([(0, 0)])

    while queue:
        x, y = queue.popleft()
        if (x, y) == (m - 1, n - 1):   # Destination 
            path = []
            while (x, y) != (0, 0):
                path.append([x, y])
                x, y = parent[(x, y)]
            return [[0, 0]] + path[::-1]

        for nx, ny in ((x + 1, y), (x, y + 1)):  # 下、右
            if nx < m and ny < n and grid[nx][ny] == 0 and (nx, ny) not in parent:
                parent[(nx, ny)] = (x, y)
                queue.append((nx, ny))

    return []


grid = [[0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]]
print(find_path(grid))
    
