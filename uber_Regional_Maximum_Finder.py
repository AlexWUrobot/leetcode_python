# https://www.fastprep.io/problems/uber-regional-maximum-finder

from collections import deque

def findRegionalMaxima(array):
    if not array or not array[0]:
        return []
    
    rows, cols = len(array), len(array[0])
    maxima = []
    
    def is_regional_maximum(i, j):
        if array[i][j] == 0:
            return False
        
        value = array[i][j]
        region_min_row = max(0, i - value)
        region_max_row = min(rows - 1, i + value)
        region_min_col = max(0, j - value)
        region_max_col = min(cols - 1, j + value)
        
        queue = deque()
        queue.append((i, j))
        visited = set()
        visited.add((i, j))
        
        while queue:
            r, c = queue.popleft()
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (1, -1), (1, 1), (-1, -1)]:
                nr, nc = r + dr, c + dc
                if (region_min_row <= nr <= region_max_row and
                    region_min_col <= nc <= region_max_col and
                    (nr, nc) not in [(i - value, j - value), (i - value, j + value), (i + value, j - value), (i + value, j + value)]):
                    if array[nr][nc] > value:
                        return False
                    if (nr, nc) not in visited:
                        queue.append((nr, nc))
                        visited.add((nr, nc))
        
        return True
    
    for i in range(rows):
        for j in range(cols):
            if is_regional_maximum(i, j):
                maxima.append([i, j])
    
    return maxima

# Example usage:
array = [
    [3, 0, 1],
    [2, 0, 0],
    [0, 0, 0]
]
print(findRegionalMaxima(array))
