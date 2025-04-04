# https://www.fastprep.io/problems/uber-count-ways-to-reach-a-sum

from collections import Counter

def countWays(a, b, queries):
    # Create a counter to track sums of elements from a and b
    sum_counter = Counter()
    
    # Initialize sum_counter with all possible sums from a and b
    for x in a:
        for y in b:
            sum_counter[x + y] += 1
    
    results = []
    
    for query in queries:
        if query[0] == 1:  # Query type [1, x] -> Count pairs summing to x
            results.append(sum_counter[query[1]])
        elif query[0] == 0:  # Query type [0, i, x] -> Update b[i] by adding x
            i, x = query[1], query[2]
            old_value = b[i]
            b[i] += x
            
            # Update sum_counter by removing old sums and adding new sums
            for num in a:
                sum_counter[num + old_value] -= 1
                sum_counter[num + b[i]] += 1
    
    return results
