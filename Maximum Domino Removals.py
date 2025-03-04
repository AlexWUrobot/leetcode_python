# https://www.fastprep.io/problems/amazon-maximum-domino-removals
# https://chatgpt.com/share/67c7593b-29ec-8005-8a1e-8bab07f4b572

# Understanding the Game
# You have a set of dominoes, each with a distinct size represented by an array tiles. The order of these dominoes is defined as the length of the longest strictly increasing subsequence (LIS).

# What is LIS (Longest Increasing Subsequence)?
# The longest increasing subsequence (LIS) is the longest sequence of numbers from an array such that:

# The numbers are strictly increasing (each number is larger than the previous one).
# The numbers appear in the same relative order as in the original array.
# Example of LIS
# For tiles = [1, 4, 4, 2, 5, 3], some possible increasing subsequences are:

# [1, 4, 5] (length 3)
# [1, 2, 3] (length 3)
# [1, 4] (length 2)
# The longest among these has length 3, so LIS(tiles) = 3.

# How to Play the Game?
# You are given an array removalOrder, which tells you which domino to remove one by one. Your goal is to remove as many dominoes as possible while ensuring that the LIS of the remaining tiles stays at least minOrder.

# Example Walkthrough
# Given:

# python
# Copy
# Edit
# tiles = [1, 4, 4, 2, 5, 3]
# removalOrder = [2, 1, 4, 0, 5, 3]  
# minOrder = 3
# You must remove the dominoes in the given order (not randomly).
# After each removal, the LIS of the remaining tiles should be at least minOrder.


# Step-by-Step Process
# Step	Remove Index	Remaining Tiles	LIS
# Start	-	[1, 4, 4, 2, 5, 3]	3 ✅
# 1	Remove tiles[2] = 4	[1, 4, 2, 5, 3]	3 ✅
# 2	Remove tiles[1] = 4	[1, 2, 5, 3]	3 ✅
# 3	Remove tiles[4] = 5	[1, 2, 3]	3 ✅
# 4	Remove tiles[0] = 1	[2, 3]	2 ❌ (LIS < minOrder)
# Since the LIS drops below minOrder = 3 after the 4th removal, the maximum valid removals is 3.

# Final Answer: 3


from bisect import bisect_left

def length_of_LIS(arr):
    """ Returns the length of the Longest Increasing Subsequence using O(n log n) approach. """
    lis = []
    for num in arr:
        pos = bisect_left(lis, num)
        if pos == len(lis):
            lis.append(num)
        else:
            lis[pos] = num
    return len(lis)

def maxDominoRemovals(tiles, removalOrder, minOrder):
    n = len(tiles)
    
    # Binary search for max removals
    left, right = 0, n
    removal_pos = {val: idx for idx, val in enumerate(removalOrder)}  # Store removal positions

    def canRemove(k):
        """ Check if we can remove k elements while keeping LIS >= minOrder """
        # Mark the first k elements as removed
        removed = set(removalOrder[:k])
        filtered_tiles = [tiles[i] for i in range(n) if i not in removed]
        
        return length_of_LIS(filtered_tiles) >= minOrder

    # Binary search for maximum k
    while left < right:
        mid = (left + right + 1) // 2
        if canRemove(mid):
            left = mid  # Try removing more
        else:
            right = mid - 1  # Reduce removals
    
    return left

# Example usage:
tiles = [1, 4, 4, 2, 5, 3]
removalOrder = [2, 1, 4, 0, 5, 3]
minOrder = 3

print(maxDominoRemovals(tiles, removalOrder, minOrder))
