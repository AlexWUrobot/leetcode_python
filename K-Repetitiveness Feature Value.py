# https://www.fastprep.io/problems/amazon-get-k-rep-value

def getkRepValue(user_history, k):
    n = len(user_history)
    count = 0
    
    # Iterate through all possible substrings
    for i in range(n):
        freq = {}
        for j in range(i, n):
            # Update the frequency of the current character
            if user_history[j] in freq:
                freq[user_history[j]] += 1
            else:
                freq[user_history[j]] = 1
            
            # Check if any character appears at least k times in the current substring
            if any(value >= k for value in freq.values()):
                count += 1
    
    return count

# Example usage
user_history = "ceccca"
k = 3
print(getkRepValue(user_history, k))  # Output: 7

# Example usage
user_history = "acaab"
k = 3
print(getkRepValue(user_history, k))  # Output: 7
