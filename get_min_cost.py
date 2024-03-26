# https://fastprep.gitbook.io/amazon-2024-oa/2023-june-aug/get-minimum-cost
# learn heapq : https://docs.python.org/3/library/heapq.html


import heapq

def getMinimumCost(a, b, m):
    # Create a priority queue with initial costs of the first item of each type
    costs = [(cost, increment) for cost, increment in zip(a, b)]
    print(costs)
    heapq.heapify(costs)  # sorted from small to big 
    print(costs)
    
    total_cost = 0
    for _ in range(m):
        # Pop the smallest cost item
        cost, increment = heapq.heappop(costs)  # Pop and return the smallest item from the heap
        print(cost,increment)
        total_cost += cost
        # Push the next item of the same type with incremented cost
        heapq.heappush(costs, (cost + increment, increment)) # Push item on the heap, then pop and return the smallest item from the heap
        print("costs:",costs)

    return total_cost

# Example usage:
n = 3
a = [2, 1, 1]
b = [1, 2, 3]
m = 4
print(getMinimumCost(a, b, m))  # Output should be 7
