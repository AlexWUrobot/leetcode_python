#https://www.fastprep.io/problems/amazon-kth-smallest-in-subarray

import collections
import heapq

def kth_smallest_sliding_window(nums, k, m):
    # Initialize two heaps: max_heap for the largest k elements and min_heap for the rest
    max_heap = []
    min_heap = []
    # Initialize the result list
    res = []
    # Keep track of the frequency of elements to delete later
    to_delete = collections.defaultdict(int)
    
    # Process the first m elements
    for i in range(m):
        heapq.heappush(max_heap, -nums[i])  # Push the negation of the element to max_heap
        if len(max_heap) > k:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))  # Balance heaps
    
    # Append the maximum element from max_heap to the result
    res.append(-max_heap[0])
    
    # Process the remaining elements
    for i in range(m, len(nums)):
        prev = nums[i - m]  # The element to remove from the sliding window
        to_delete[prev] += 1  # Increment its frequency
        balance = -1 if prev <= res[-1] else 1  # Determine the balance factor
        
        # Update heaps based on the current element
        if nums[i] <= res[-1]:
            balance += 1
            heapq.heappush(max_heap, -nums[i])
        else:
            balance -= 1
            heapq.heappush(min_heap, nums[i])
        
        # Rebalance heaps if necessary
        if balance < 0:
            heapq.heappush(max_heap, -heapq.heappop(min_heap))
        elif balance > 0:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        
        # Remove elements with zero frequency from both heaps
        while max_heap and to_delete[-max_heap[0]] > 0:
            to_delete[-max_heap[0]] -= 1
            heapq.heappop(max_heap)
        while min_heap and to_delete[min_heap[0]] > 0:
            to_delete[min_heap[0]] -= 1
            heapq.heappop(min_heap)
        
        # Append the maximum element from max_heap to the result
        res.append(-max_heap[0])
    
    return res

arr = [3, 1, 4, 2]
k = 2
m = 3
print(kth_smallest_sliding_window(arr, k, m))
