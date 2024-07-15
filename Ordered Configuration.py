# https://www.fastprep.io/problems/amazon-ordered-configuration
from typing import List

class Solution:
  def orderedConfiguration(self, configuration: str) -> List[str]:
    config = sorted(configuration.split('|'))
    order = [i[:4] for i in config]
    if len(set(order)) != len(order):
      return ["Invalid configuration"]
    return [i[4:] for i in config]
    
    
ans = Solution()
configuration = "0001LAJ5KBX9H8|0003UKURNK403F|0002MO6K1Z9WFA|0004OWRXZFMS2C"
print(ans.orderedConfiguration(configuration))  

configuration = "000533B8XLD2EZ|0001DJ2M2JBZZR|0002Y9YK0A7MYO|0004IKDJCAPG5Q|0003IBHMH59SBO"
print(ans.orderedConfiguration(configuration))  

configuration = "0002f7c22e7904|000176a3a4d214|000305d29f4a4b"
print(ans.orderedConfiguration(configuration))  

configuration = "0002f7c22e7904|000176a3a4d214|000205d29f4a4b"
print(ans.orderedConfiguration(configuration)) 
# Time complexity O(n log n)

