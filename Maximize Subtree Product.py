# https://www.fastprep.io/problems/amazon-maximize-subtree-product

from collections import defaultdict

def max_subtree_product(n, edges):
    def dfs(node, parent):
        # Initialize the size of the current subtree
        size = 1
        for neighbor in tree[node]:
            if neighbor != parent:
                child_size = dfs(neighbor, node)
                size += child_size
                subtree_sizes.append(child_size)
        return size

    # Create adjacency list for the tree
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)

    # List to store the sizes of subtrees
    subtree_sizes = []

    # Calculate the size of the entire tree and fill subtree_sizes
    total_size = dfs(1, -1)

    # Calculate the maximum product
    max_product = 0
    print("subtree_sizes:", subtree_sizes)
    for size in subtree_sizes:
        product = size * (total_size - size)
        if product > max_product:
            max_product = product
    

    return max_product if max_product > 0 else n

# Example usage
n1 = 5
edges1 = [[1, 2], [2, 3], [3, 4], [4, 5]]
print(max_subtree_product(n1, edges1))  # Output: 6


n1 = 6
edges1 = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
print(max_subtree_product(n1, edges1))  # Output: 6

n2 = 2
edges2 = [[1, 2]]
print(max_subtree_product(n2, edges2))  # Output: 2
