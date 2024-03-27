# https://www.fastprep.io/problems/amazon-find-number-of-possible-unique-strings


def findNumberOfPossibleUniqueStrings(s):
    unique_strings = set()

    # Iterate over all possible substrings
    for i in range(len(s)):
        for j in range(i, len(s)):
            # Reverse the substring and form a new string
            new_string = s[:i] + s[i:j+1][::-1] + s[j+1:]
            unique_strings.add(new_string)
    
    # Print all unique substrings except the original string
    for unique_string in unique_strings:
        if unique_string != s:
            print(unique_string)

    #nclude the original string
    return len(unique_strings) 

# Example usage:
input_string = "abc"
print("Number of possible unique strings:", findNumberOfPossibleUniqueStrings(input_string))
