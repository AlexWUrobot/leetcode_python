def is_valid_string(s: str) -> int:
    # Convert the string to an integer and check divisibility by 3
    if int(s) % 3 != 0:
        return 0
    
    # Count occurrences of '7'
    if s.count('7') < 2:
        return 0
    
    return 1

# Example test cases
print(is_valid_string("771"))    # Output: 1
print(is_valid_string("777"))    # Output: 1
print(is_valid_string("123777")) # Output: 1
print(is_valid_string("123"))    # Output: 0
print(is_valid_string("700"))    # Output: 0
