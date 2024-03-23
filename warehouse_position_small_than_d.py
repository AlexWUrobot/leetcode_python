# https://leetcode.com/discuss/interview-question/4791346/Coding-Round-for-Amazon-Online
def is_valid(center, d, x):
    return all(abs(c - x) <= d for c in center)

def find_suitable_locations(centers, d):
    left, right = -10**9, 10**9
    
    # Find the leftmost point
    while left < right:
        mid = (left + right) // 2
        if is_valid(centers, d, mid):
            right = mid
        else:
            left = mid + 1
    leftmost = left
    
    left, right = -10**9, 10**9
    
    # Find the rightmost point
    while left < right:
        mid = (left + right + 1) // 2
        if is_valid(centers, d, mid):
            left = mid
        else:
            right = mid - 1
    rightmost = left
    
    # Calculate the number of suitable locations
    return max(rightmost - leftmost, 0)

# Example usage:
n = 3
centers = [-2, 1, 0]
d = 8
print(find_suitable_locations(centers, d))
