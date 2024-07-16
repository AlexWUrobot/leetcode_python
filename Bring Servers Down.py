
# https://www.fastprep.io/problems/amazon-bring-servers-down

def minimum_requests(request, health, k):
    if len(request) != len(health):
        return 0
    
    l = len(request)
    total_sum = 0
    
    for i in range(l):
        if health[i] % k == 0:
            total_sum += request[i] * (health[i] // k + 1) #  must send one more request 
        else:
            total_sum += request[i] * (health[i] // k + 2) #  must send one more request 

        
    
    return total_sum
    
request = [3, 4]  # the number of requests each server can serve
health = [4, 6]   # 
# total life for a server is request & health
k = 3
print(minimum_requests(request, health, k))
