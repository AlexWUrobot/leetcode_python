# https://www.fastprep.io/problems/amazon-assign-requests-to-servers


def assign_requests_to_servers(num_servers, request):
    # Initialize the list to store the number of requests for each server
    server_requests = [0] * num_servers
    result = []

    # Process each request
    for r in request:  
        # Find the server with the minimum number of requests
        min_requests = float('inf')
        min_server = None
        # find the min loading server id also the id should smaller than request number
        for i in range(r):  
            if server_requests[i] < min_requests:
                min_requests = server_requests[i]
                min_server = i

        # Assign the request to the chosen server
        server_requests[min_server] += 1
        result.append(min_server)

    return result

# Example usage
num_servers = 5
request = [3, 2, 3, 2, 4]
output = assign_requests_to_servers(num_servers, request)
print(output)  # Output: [0, 1, 2, 0, 3]
