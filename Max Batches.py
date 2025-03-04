# https://www.fastprep.io/problems/amazon-max-batches
# https://chatgpt.com/share/67c76501-1830-8005-bc4e-83e4c6139c60

# Understanding the Problem
# We need to determine the maximum number of batches that can be packed while adhering to the following rules:

# Each batch consists of only unique product types (no duplicates).
# Each subsequent batch must contain more items than the previous one (strictly increasing order).
# Each item can be used at most once.
# Our goal is to find the maximum number of batches we can form.

from typing import List

class Solution:
    def maxBatches(self, products: List[int]) -> int:
        n = len(products)
        inventory = products[:]
        batch_number = 1
        
        # Helper function to check if we can form k batches
        def can_pack(k):
            required = k * (k + 1) // 2  # Total items needed
            available = sum(min(p, k) for p in inventory)  # Total available items
            return available >= required
        
        # Binary search for the maximum number of batches
        lo, hi = 0, 2 * n  # Upper bound is a loose estimate
        max_batches = 0
        
        while lo <= hi:
            mid = (lo + hi) // 2
            if can_pack(mid):
                max_batches = mid  # Update max_batches if mid is possible
                lo = mid + 1  # Try to increase k
            else:
                hi = mid - 1  # Reduce k
        
        # Now construct the batches and print each step
        k = max_batches
        inventory = products[:]  # Reset inventory for tracing process
        
        for batch_size in range(1, k + 1):
            batch = []
            sorted_indices = sorted(range(n), key=lambda i: -inventory[i])  # Sort indices by inventory count (descending)
            for i in sorted_indices:
                if inventory[i] > 0 and len(batch) < batch_size:
                    batch.append(i)
                    inventory[i] -= 1
            print(f"{batch_number}⃣ Batch: Contains {batch_size} items of product types {batch}")
            print(f"Remaining inventory: {inventory}\n")
            batch_number += 1
        
        print(f"Maximum number of batches that can be prepared: {max_batches}")
        return max_batches

# Example usage
solution = Solution()
inventory = [2, 3, 1, 4, 2]
solution.maxBatches(inventory)
