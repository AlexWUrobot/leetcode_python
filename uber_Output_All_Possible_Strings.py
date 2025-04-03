
# https://www.fastprep.io/problems/uber-output-all-possible-strings
def reverseAndAppend(s: str):
    result = set()
    n = len(s)
    
    for i in range(1, n):  # i is the index to start reversing
        # Reverse from 0 to i (inclusive)
        left_reversed = s[:i+1][::-1] + s[i+1:]
        result.add(left_reversed)
        
        # Reverse from i to the end
        right_reversed = s[:i] + s[i:][::-1]
        result.add(right_reversed)
    
    return list(result)

# Example usage:
s = "dbaacca"
print(reverseAndAppend(s))
