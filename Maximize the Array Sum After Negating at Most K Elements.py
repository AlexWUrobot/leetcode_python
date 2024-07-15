# https://www.fastprep.io/problems/amazon-maximize-the-array-sum-after-negating-at-most-k-elements

#1.Compute the prefix sums of the array.
#2. Sort the prefix sums along with their original indices.
#3. Negate the smallest prefix sums as long as they don't make any prefix sum non-positive.

def max_negate_prefix_positive(A):
    n = len(A)
    prefix_sums = [0] * n
    prefix_sums[0] = A[0]
    
    for i in range(1, n):
        prefix_sums[i] = prefix_sums[i-1] + A[i]
    
    indexed_A = sorted((val, idx) for idx, val in enumerate(A[:]))  # from small to bigger 
    #indexed_prefix_sums = sorted((val, idx) for idx, val in enumerate(prefix_sums))
    #print(indexed_A)
    
    B = A[:]
    negated_count = 0
    
    #print(prefix_sums)
    for value, idx in indexed_A:
        if value < 0:
            break
        # Negate the current element if it does not cause any prefix sum to be non-positive
        can_negate = True
        for j in range(idx, n):
            if prefix_sums[j] - 2 * A[idx] <= 0:
                can_negate = False
                break
        if can_negate:
            B[idx] = -B[idx]
            for j in range(idx, n):
                prefix_sums[j] -= 2 * A[idx]
            negated_count += 1
    
    return negated_count, B

# Example usage:
A1 = [4, 1, 1, 1]
A2 = [10, 9, 2, 3]
print(max_negate_prefix_positive(A1))  # Output: [4, -1, -1, -1]
print(max_negate_prefix_positive(A2))  # Output: [10, 9, -2, -3]
# Time complexity of O(n^2)



### Approach 2nd 
# https://www.fastprep.io/problems/amazon-maximize-the-array-sum-after-negating-at-most-k-elements

# from typing import List

# #1.Compute the prefix sums of the array.
# #2. Sort the prefix sums along with their original indices.
# #3. Negate the smallest prefix sums as long as they don't make any prefix sum non-positive.

# class Solution:
#   def maxNegations(self, A: List[int]) -> int:
#     s = sorted(A)
#     maximum = s[-1]

#     cnt = 0
#     for head in s:
#         maximum -= head
#         if maximum > 0:
#             cnt += 1
#         else:
#             return cnt

# # Example usage:
# A1 = [4, 1, 1, 1]
# A2 = [10, 2, 3, 4]
# ans = Solution()
# print(ans.maxNegations(A1))  # Output: [4, -1, -1, -1]
# print(ans.maxNegations(A2))  # Output: [10, 9, -2, -3]
# # Time complexity of O(n^2)
