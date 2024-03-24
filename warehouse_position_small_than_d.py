# complete question : https://leetcode.com/company/amazon/discuss/4882294/Amazon-OA-Question
# https://leetcode.com/discuss/interview-question/4791346/Coding-Round-for-Amazon-Online






def solve(arr, d, n): # Get the left and right boundaries using the given array and distance 'd'
    left_boundary = get_left_b(d, arr)
    right_boundary = get_right_b(d, arr)
    # print(left_boundary, right_boundary)
    if left_boundary == right_boundary:
        return 0
    
    count = 0
    for i in range(left_boundary, right_boundary + 1):
        count += 1
    return count

def get_left_b(d, arr): # Set initial low and high values for binary search
    low = -int(1e9)
    high = int(1e9)
    ans = 0
    while low <= high:
        mid = (low + high) // 2
        if check(mid, arr, d):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

def get_right_b(d, arr): # Set initial low and high values for binary search
    low = -int(1e9)
    high = int(1e9)
    ans = 0
    while low <= high:
        mid = (low + high) // 2
        if check(mid, arr, d):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return ans

def check(mid, arr, d): # Calculate the total distance from 'mid' to all elements in 'arr'
    total = 0
    for i in arr:
        total += (2 * abs(mid - i))
    return total <= d # Return True if the total distance is less than or equal to 'd'

# Main execution
if __name__ == "__main__":
    # n = 4
    # arr = [2, 0, 3, -4]
    # d = 22
    n = 3
    arr = [-2, 1, 0]
    d = 8 # Call the solve function and print the result
    print(solve(arr, d, n))


# def is_valid(center, d, x):
#     return all(abs(c - x) <= d for c in center)

# def find_suitable_locations(centers, d):
#     left, right = -10**9, 10**9
    
#     # Find the leftmost point
#     while left < right:
#         mid = (left + right) // 2
#         if is_valid(centers, d, mid):
#             right = mid
#         else:
#             left = mid + 1
#     leftmost = left
    
#     left, right = -10**9, 10**9
    
#     # Find the rightmost point
#     while left < right:
#         mid = (left + right + 1) // 2
#         if is_valid(centers, d, mid):
#             left = mid
#         else:
#             right = mid - 1
#     rightmost = left
    
#     # Calculate the number of suitable locations
#     return max(rightmost - leftmost, 0)

# # Example usage:
# n = 3
# centers = [-2, 1, 0]
# d = 8
# print(find_suitable_locations(centers, d))
