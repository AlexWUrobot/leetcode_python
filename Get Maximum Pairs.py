
#https://www.fastprep.io/problems/amazon-get-max-pairs

def getMaxPairs(frontend, backend):
    # Sort both arrays in descending order
    frontend.sort(reverse=True)
    backend.sort(reverse=True)
    
    # Initialize pointers and count for valid pairs
    i, j = 0, 0
    valid_pairs = 0
    
    # Iterate through both arrays
    while i < len(frontend) and j < len(backend):
        if frontend[i] > backend[j]:
            # Valid pair found, increment count
            valid_pairs += 1
            i += 1
            j += 1
        else:
            # Frontend quality is not greater, move to next backend server
            j += 1
    
    return valid_pairs

# Example usage
frontend = [1, 2, 3]
backend = [1, 2, 1]
print(getMaxPairs(frontend, backend))  # Output: 2
