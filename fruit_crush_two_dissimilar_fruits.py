# https://leetcode.com/company/amazon/discuss/4919034/Amazon-OA

from collections import defaultdict
import heapq

def min_fruits_left(arr):
    # Dictionary to store the count of each fruit
    fruit_counts = defaultdict(int)
    
    # Count the frequency of each fruit
    for x in arr:
        fruit_counts[x] += 1
    
    # Priority queue to store the counts in descending order
    pq = []
    for value in fruit_counts.values():
        heapq.heappush(pq, -value)  # Push negative values to create a max heap
    
    # Perform the operation to crush fruits
    while pq:
        x = -heapq.heappop(pq)  # Get the count of the most frequent fruit
        y = 0
        if pq:
            y = -heapq.heappop(pq)  # Get the count of the second most frequent fruit
        else:
            return x  # If only one type of fruit left, return its count
        
        # Calculate the difference between counts
        diff = x - y
        if diff > 0:  # If there are remaining fruits after crushing, add to the priority queue
            heapq.heappush(pq, -diff)
    
    return 0  # If no fruits left, return 0

# Test cases
arr1 = [2, 2, 1, 3, 3]
arr2 = [2, 2, 1, 3, 3, 3]
arr3 = [2, 2, 1, 3, 3, 3, 5]
arr4 = [3, 3]

print(min_fruits_left(arr1))  # Output: 1
print(min_fruits_left(arr2))  # Output: 0
print(min_fruits_left(arr3))  # Output: 1
print(min_fruits_left(arr4))  # Output: 2
