
# https://www.fastprep.io/problems/amazon-find-k-level-permutation

from itertools import permutations

def max_min_diff(segment_sums):
    return max(segment_sums) - min(segment_sums)

def calculate_segment_sums(arr, window_size):
    segment_sums = []
    for i in range(len(arr) - window_size + 1):
        segment_sum = sum(arr[i:i + window_size])
        segment_sums.append(segment_sum)
    return segment_sums

def arrange_list(a, K):
    N = len(a)
    window_size = N - K + 1
    best_arrangement = None
    smallest_diff = float('inf')
    
    for perm in permutations(a):
        
        #print(perm)
        
        segment_sums = calculate_segment_sums(perm, window_size)
        current_diff = max_min_diff(segment_sums)
        if current_diff < smallest_diff:
            smallest_diff = current_diff
            best_arrangement = perm
        if smallest_diff == 1:
            break  # If we find the optimal solution, break early
    
    return best_arrangement

a = [1, 2, 3, 4, 5, 6, 7]
K = 4
result = arrange_list(a, K)
print(f"Best arrangement: {result}")



# def arrange_list(a, K):
#     N = len(a)
#     a_sorted = sorted(a)  # Sort the array
    
#     window_size = N - K + 1
#     min_diff = float('inf')
#     best_arrangement = None
    
#     # Use two pointers technique
#     left = 0
#     right = window_size - 1
    
#     # Calculate initial sum and difference
#     current_sum = sum(a_sorted[left:right+1])
#     current_diff = a_sorted[right] - a_sorted[left]
    
#     min_diff = current_diff
#     best_arrangement = a_sorted[left:right+1]
    
#     # Slide the window from left to right
#     while right < N - 1:
#         current_sum -= a_sorted[left]
#         left += 1
#         right += 1
#         current_sum += a_sorted[right]
        
#         current_diff = a_sorted[right] - a_sorted[left]
        
#         # Update minimum difference and best arrangement if found a better one
#         if current_diff < min_diff:
#             min_diff = current_diff
#             best_arrangement = a_sorted[left:right+1]
        
#         # Early exit if we find the optimal solution
#         if min_diff <= 1:
#             break
    
#     # Return the best arrangement found
#     return best_arrangement


# a = [1, 2, 3, 4, 5, 6, 7]
# K = 4
# result = arrange_list(a, K)
# print(f"Best arrangement: {result}")
