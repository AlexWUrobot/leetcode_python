# https://www.fastprep.io/problems/uber-build-blocks-and-obstacles

def process_operations(operations):
    obstacles = set()
    result = []
    
    for op in operations:
        if op[0] == 1:
            # Place an obstacle
            obstacles.add(op[1])
        elif op[0] == 2:
            # Check if a block can be built
            end, size = op[1], op[2]
            start = end - size
            
            # Check if any obstacle exists in the range [start, end - 1]
            if any(pos in obstacles for pos in range(start, end)):
                result.append("0")
            else:
                result.append("1")
    
    return "".join(result)

# Example usage
operations = [[1, 2], [1, 5], [2, 5, 2], [2, 6, 3], [2, 2, 1], [2, 3, 2]]
print(process_operations(operations))  # Output: "1010"
