# https://www.fastprep.io/problems/amazon-find-first-unique

def findFirstUnique(s):
    # Create a dictionary to store the frequency of each character
    char_frequency = {}
    for char in s:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1

    # Iterate over the string to find the first unique character
    for i, char in enumerate(s):
        if char_frequency[char] == 1:
            return i + 1  # Return 1-based index

    return -1  # No unique character found

# Example usage:
print(findFirstUnique("statistics"))  # Output: 3
