#  https://www.fastprep.io/problems/find-median-of-subarray-uniqueness



from typing import List

class Solution:
  def findMedianOfSubarrayUniqueness(self, arr: List[int]) -> int:
    n = len(arr)
    def find_all_subarrays(arr):
      subarrays = []
      # Generate all possible subarrays
      for start in range(n):
          for end in range(start, n):
              subarray = arr[start:end + 1]
              subarrays.append(subarray)
      
      return subarrays
    all_subarrays = find_all_subarrays(arr)
    uniqueness = sorted([len(set(i)) for i in all_subarrays])
    median = uniqueness[n // 2]
    return median
    
    
ans = Solution()
arr = [1, 1]
print(ans.findMedianOfSubarrayUniqueness(arr))  # Output: 1

arr = [1, 2, 3]
print(ans.findMedianOfSubarrayUniqueness(arr))  # Output: 1

arr = [1, 2, 1]
print(ans.findMedianOfSubarrayUniqueness(arr))  # Output: 1
# Time complexity of O(n^2)
