# https://www.fastprep.io/problems/amazon-find-minimum-time
# https://chatgpt.com/share/67c7df36-2a3c-8005-a522-01585c4132fa

def findMinimumTime(n, position):
    # Sort apple positions for an optimal path
    position.sort()
    
    min_time = float('inf')

    # Iterate over all possible n-sized subsets to find the optimal path
    for i in range(len(position) - n + 1):
        # Consider eating n apples starting from index i to i+n-1
        left_most = position[i]
        right_most = position[i + n - 1]
        
        # Strategy 1: Go to the leftmost apple first, then the rightmost
        time1 = abs(left_most) + abs(right_most - left_most)
        
        # Strategy 2: Go to the rightmost apple first, then the leftmost
        time2 = abs(right_most) + abs(right_most - left_most)
        
        # Take the minimum time of both strategies
        min_time = min(min_time, min(time1, time2))

    return min_time

# Example usage:
n = 3
position = [-20, 5, 10]
print(findMinimumTime(n, position))  # Output: 40

n = 2
position = [-40, 5, 10, 15]
print(findMinimumTime(n, position))  # Output: 70
