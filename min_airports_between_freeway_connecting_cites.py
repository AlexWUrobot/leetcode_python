#  There are N cities and a number of freeways. Each city has its own airport. 
#  A freeway connects two cities. You could either drive vehicles on these 
#  freeways or take flights between cities to travel. Given N cities and a 
#  list of freeways connecting 2 cities. In order to travel all cities, what's
#  the minimum number of airports do you need to go to?
# //
# // E.g
# // N = 5
# // freeways = [[0, 1], [1, 2], [3, 4]]
# // The minimum number of airport needed is 2.

from collections import defaultdict


def dfs(city, visited, graph, N):
    visited[city] = True
    
    for neighbor in graph[city]:
        if neighbor < N:
            if not visited[neighbor]:
                dfs(neighbor, visited, graph, N)
            

# find the minimun number of airport need 

def min_airport(N, freeways):

    
    # create a graph by using dict
    graph = defaultdict(list)
    
    for u, v in freeways: # load 
        graph[u].append(v)
        graph[v].append(u)
        
        if u > N-1 or v > N-1:
            print("one freeway connect to non-existing cities")
        
    # print("graph:", graph)
    # track of the visited cites
    
    visited = [False]*N
    
    # count how many total
    count = 0
    

    # iterate all cities
    for city in range(N):
        if not visited[city]:
            dfs(city, visited, graph, N)
            count += 1
            
    # If there is only one connected component, return 0, to deal with the circular city
    if count == 1:
        return 0        
            
    return count
     
# test 1  
N = 5
freeways = [[0, 1], [1, 2], [3, 4]]
print("N = 5  Ans = 2 Minimum # airports is", min_airport(N, freeways))

# test 2
N = 2
freeways = [[0, 1]]
print("N = 2  Ans = 0 Minimum # airports is", min_airport(N, freeways))

# # test 3
N = 3
freeways = [[0, 1]]
print("N = 3  Ans = 2 Minimum # airports is", min_airport(N, freeways))

# # test 4
N = 4
freeways = [[0, 1], [2, 3]]
print("N = 4  Ans = 2 Minimum # airports is", min_airport(N, freeways))

# # test 5
N = 3
freeways = [[0, 1], [2, 3]]
print("N = 3  Ans = 2 Minimum # airports is", min_airport(N, freeways))

############################################################################
#1, All cities are connected directly or indirectly
N = 4
freeways = [[0, 1], [1, 2], [2, 3]]
print("N = 4  Ans = 0 Minimum # airports is", min_airport(N, freeways))

#2, Disconnected Components:
N = 5
freeways = [[0, 1], [2, 3]]
print("N = 5  Ans = 3 Minimum # airports is", min_airport(N, freeways))


#3, Single City (Only one city, no airport needed)
N = 1
freeways = []
print("N = 1  Ans = 0 Minimum # airports is", min_airport(N, freeways))

#4, Multiple cities with no freeways
N = 3
freeways = []
print("N = 3  Ans = 3 Minimum # airports is", min_airport(N, freeways))

#5, All cities are connected in a circular manner.
N = 4
freeways = [[0, 1], [1, 2], [2, 3], [3, 0]]
print("N = 4  Ans = 0 Minimum # airports is", min_airport(N, freeways))

#6,  A more complex graph with multiple connections.
N = 6
freeways = [[0, 1], [1, 2], [2, 0], [3, 4], [4, 5]]
print("N = 6  Ans = 2 Minimum # airports is", min_airport(N, freeways))



