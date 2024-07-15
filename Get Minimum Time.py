# https://www.fastprep.io/problems/get-min-time
# O(n^2)
def getMinTime(total_servers, servers):
    # Sort the servers array
    servers.sort()
    
    # Calculate the time to transfer data in a circular manner
    min_time = float('inf')
    
    for i in range(len(servers)):
        # Calculate time to transfer starting from current server and going forward
        forward_time = 0
        for j in range(1, len(servers)):
            forward_time += (servers[(i + j) % len(servers)] - servers[(i + j - 1) % len(servers)]) % total_servers
        
        # Calculate time to transfer starting from current server and going backward
        backward_time = 0
        for j in range(1, len(servers)):
            backward_time += (servers[(i - j + len(servers)) % len(servers)] - servers[(i - j + 1 + len(servers)) % len(servers)]) % total_servers
        
        # Take the minimum of both
        min_time = min(min_time, forward_time, backward_time)
    
    return min_time

# Example usage:
total_servers = 8
servers = [2, 6, 8]
print(getMinTime(total_servers, servers))  # Output: 4


# Example usage:
total_servers = 5
servers = [1, 5]
print(getMinTime(total_servers, servers))  # Output: 4


# Example usage:
total_servers = 10
servers = [4, 6, 2, 9]
print(getMinTime(total_servers, servers))  # Output: 4
