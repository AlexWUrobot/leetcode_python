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
