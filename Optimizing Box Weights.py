# https://www.fastprep.io/problems/amazon-minimal-heaviest-set-a
from typing import List

class Solution:
  def minimalHeaviestSetA(self, arr: List[int]) -> List[int]:
    """
    First Approach : Backtracking with greedy
    """
    
    def backtrack(subarr1, subarr2):
        # Compare the sums of subarr1 and subarr2
        if sum(subarr1) > sum(subarr2):
            return subarr1[::-1]  # Return subarr1 in reverse order
        if len(subarr2) > 1:
            # Recurse by adding the first element of subarr2 to subarr1
            return backtrack(subarr1 + [subarr2[0]], subarr2[1:])

    # Sort the input array in descending order
    arr.sort(reverse=True)
    # Initialize the backtracking with the first element of arr
    return backtrack([arr[0]], arr[1:])
    

ans = Solution()
arr = [5, 3, 2, 4, 1, 2]
#Input:  arr = [5, 3, 2, 4, 1, 2]
#Output: [4, 5] 
print(ans.minimalHeaviestSetA(arr))


#Input:  arr = [4, 2, 5, 1, 6]
#Output: [5, 6] 
arr = [4, 2, 5, 1, 6]
print(ans.minimalHeaviestSetA(arr))

#Input:  arr = [3, 7, 5, 6, 2]
# Output: [6, 7] 
arr = [3, 7, 5, 6, 2]
print(ans.minimalHeaviestSetA(arr))

# time complexity O(ologn) + O(2^n . n) =   O(2^n . n)
