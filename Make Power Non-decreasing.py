# https://www.fastprep.io/problems/1.amazon-make-power-non-decreasing

from typing import List

class Solution:
  def makePowerNonDescreasing(self, power: List[int]) -> int:
    units_added = 0
    for i in range(1, len(power)):
      if power[i] < power[i-1]:
        units_added += power[i-1] - power[i]
    return (units_added)
    
    
sol = Solution()
powa = [3, 4, 1, 6, 2]
print(sol.makePowerNonDescreasing(powa))
powa = [3, 2, 1]
print(sol.makePowerNonDescreasing(powa))
powa = [3, 5, 2, 3]
print(sol.makePowerNonDescreasing(powa))
