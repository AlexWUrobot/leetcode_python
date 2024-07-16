
# https://www.fastprep.io/problems/amazon-maximum-stability




def maximumStability2(reliability, availability):
    # Create a list of pairs (reliability[i], availability[i])
    container = []
    n = len(reliability)
    for i in range(n):
        container.append([reliability[i], availability[i]])
    
    # Sort the container by availability (descending) and reliability (ascending)
    container.sort(key=lambda x: (x[1], -x[0]), reverse=True)
    mod = 10**9 + 7
    
    # Initialize variables for cumulative reliability and availability
    cur_relia, cur_avail = container[0]
    max_sta = cur_relia * cur_avail
    
    # Calculate maximum stability
    for i in range(1, n):
        cur_relia += container[i][0]
        cur_avail = container[i][1]
        max_sta = max(max_sta, cur_relia * cur_avail)
    
    return max_sta
    
    
reliability = [1, 2, 2]
availability = [1, 1, 3]
print(maximumStability2(reliability, availability))

# the time complexitｙ　：　O(n log n) 
