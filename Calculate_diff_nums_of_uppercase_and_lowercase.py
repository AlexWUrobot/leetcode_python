def solution(typedText):
    # Initialize counters for uppercase and lowercase letters
    uppercase_count = 0
    lowercase_count = 0

    # Loop through each character in the input string
    for char in typedText:
        # Check if the character is an uppercase letter
        if char.isupper():
            uppercase_count += 1
        # Check if the character is a lowercase letter
        elif char.islower():
            lowercase_count += 1
        # Other characters (if any) are ignored as per problem constraints (English letters only)

    # Calculate the difference: uppercase letters minus lowercase letters
    difference = uppercase_count - lowercase_count

    # Return the computed difference
    return difference

# Example test cases
print(solution("CodeSignal"))  # Output: -6
print(solution("a"))           # Output: -1
print(solution("AbCdEf"))      # Output: 0
