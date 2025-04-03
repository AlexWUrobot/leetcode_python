# https://www.fastprep.io/problems/uber-generate-array

def generateArray(words):
    result = []
    n = len(words)
    
    for i in range(n):
        first_letter = words[i][0]  # First letter of current word
        last_letter_next = words[(i+1) % n][-1]  # Last letter of next word (circular indexing)
        result.append(first_letter + last_letter_next)
    
    return result

# Example usage:
words = ["cat", "dog", "flower", "bed"]
print(generateArray(words))
