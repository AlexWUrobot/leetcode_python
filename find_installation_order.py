def dfs(node, dependencies, visited, result):
    # Mark the current node as visited
    visited.add(node)
    
    # Recur for all the nodes this node depends on
    for neighbor in dependencies.get(node, []):
        if neighbor not in visited:
            dfs(neighbor, dependencies, visited, result)
    
    # Add the current node to the result (stack) after visiting its dependencies
    result.append(node)

def find_installation_order(dependencies):
    visited = set()  # To keep track of visited nodes
    result = []  # To store the installation order
    
    # Perform DFS on each node
    for node in dependencies:
        if node not in visited:
            dfs(node, dependencies, visited, result)
    

    return result

# Example input
dependencies = {
    'A': ['B', 'C', 'D'],
    'B': ['C', 'D'],
    'C': ['E', 'F'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

# Get the installation order
order = find_installation_order(dependencies)
print(order)

# Expected output
# ['E', 'F', 'C', 'D', 'B', 'A', 'G']
