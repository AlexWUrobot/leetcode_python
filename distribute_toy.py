# https://leetcode.com/discuss/interview-question/4106381/Amazon-Online-Assessment-2023/
from collections import deque
from typing import List
import math

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def ways(n: int) -> int:
            #"""
            #Returns the number of ways to distribute n candies to 3 children.   
            #This function uses the combinatorial 'stars and bars' method to calculate the number of distributions.
            #For example, '**|**|*' represents distributing 5 candies to 3 children, where
            #stars (*) represent candies and bars (|) represent dividers between children.
            #"""
            # If n is negative, no distribution is possible
            if n < 0:
                return 0
            # Calculate combinations using the formula C(n+k-1, k-1) where k is the number of children
            return math.comb(n + 2, 2)

        # Calculate the number of ways to distribute candies such that at least one child receives more than the limit
        limitPlusOne = limit + 1
        oneChildExceedsLimit = ways(n - limitPlusOne)
        twoChildrenExceedLimit = ways(n - 2 * limitPlusOne)
        threeChildrenExceedLimit = ways(n - 3 * limitPlusOne)
            
            # Apply the Principle of Inclusion-Exclusion (PIE) to avoid overcounting
            # Start with the total number of ways to distribute candies
            # Subtract the scenarios where one child exceeds the limit (counted 3 times for each child)
            # Add back the scenarios where two children exceed the limit (counted 3 times for each pair of children)
            # Subtract the scenarios where all three children exceed the limit (counted once)
        return ways(n) \
            - 3 * oneChildExceedsLimit \
            + 3 * twoChildrenExceedLimit \
            - threeChildrenExceedLimit        


# O(1) 
        
test_class = Solution()
                                  # total no more 
print(test_class.distributeCandies(15,5))
