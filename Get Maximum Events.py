
# https://www.fastprep.io/problems/amazon-get-maximum-events


from typing import List

from collections import Counter
class Solution:
  def getMaximumEvents(self, payload: List[int]) -> int:
      freq=Counter(payload)
      minV=min(payload)
      maxV=max(payload)
      n=len(freq)
      total=0
      for key, v in freq.items():
          if key==minV or key==maxV:
              total+=min(2, v)
          else:
              total+=min(3, v)
      return total
      
sol = Solution()
payload = [1, 3, 5, 4, 2, 6, 8, 7, 9]
print(sol.getMaximumEvents(payload))
