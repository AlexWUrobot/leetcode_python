
# 0 → 1 → 2 → 3 → 4
#             ↑
#         6 → 5

# connections = [
#     [0, 1],
#     [1, 2],
#     [2, 3],
#     [3, 4],
#     [5, 3],
#     [6, 5],
# ]

# output: [
#     [0, 1, 2],
#     [3, 4],
#     [5, 6],
# ]

# Correctly Groups Nodes

# [0, 1, 2] → One parent rule is maintained.
# [3, 4] → 3 starts a new group because of multiple parents.
# [5, 6] → Another separate component.

from collections import defaultdict

def find_components(connections):
    # Step 1: Build adjacency list and reverse adjacency list
    graph = defaultdict(list)
    reverse_graph = defaultdict(list)  # Track parents

    for u, v in connections:
        graph[u].append(v)
        reverse_graph[v].append(u)

    # Step 2: Identify all unique nodes
    all_nodes = set(graph.keys()).union({v for u, v in connections})

    # Step 3: Identify nodes with multiple parents
    multiple_parents = {node for node, parents in reverse_graph.items() if len(parents) > 1}

    # Step 4: DFS Traversal with Controlled Expansion
    visited = set()
    components = []

    def explore_component(start_node):
        #print("start_node:", start_node)
        """Find all connected nodes from a starting node, following parent → child direction"""
        component = []
        stack = [start_node]

        while stack:
            node = stack.pop()
            if node in visited:
                continue

            visited.add(node)
            component.append(node)

            # Expand only in the child direction (graph[node])
            for neighbor in graph[node]:
                if neighbor not in visited and neighbor not in multiple_parents:
                    stack.append(neighbor)
                    
        stack = [start_node]
        #print("visited:", visited)
        
        # Go reverse and check 
        # ===============================
        #print("reverse:", stack)
        while stack:
            node = stack.pop()
            
            # go reverse, start_node is not viisted
            if node in multiple_parents or node != start_node:    # start node already visited, need to be skipped
                if node in visited:
                    continue
                visited.add(node)
                component.append(node)

            # Expand only in the child direction (graph[node])
            for neighbor in reverse_graph[node]:
                if neighbor not in visited and neighbor not in multiple_parents:
                    stack.append(neighbor)       
        # reverse explore 5 to 6 
        
        return component

    # Step 5: Identify Connected Components
    for node in sorted(all_nodes):  # Ensure ordered traversal
        if node not in visited:
            component = explore_component(node)
            components.append(sorted(component))  # Sort for consistency

    return components  # Final result

# Input Graph
connections = [
    [0, 1],
    [1, 2],
    [2, 3],
    [3, 4],
    [5, 3],
    [6, 5],
]

# Output Result
print(find_components(connections))
