def is_balanced(s):
    # Dictionary to hold matching pairs of brackets
    bracket_pair = {')': '(', '}': '{', ']': '['}
    
    # Stack to keep track of opening brackets
    stack = []
    
    # Iterate over each character in the string
    for char in s:
        # If the character is an opening bracket, push to stack
        if char in '([{':
            stack.append(char)
        # If the character is a closing bracket
        elif char in ')]}':
            # If stack is empty or top of stack doesn't match, return False
            if not stack or stack[-1] != bracket_pair[char]:
                return False
            # Pop the matching opening bracket from stack
            stack.pop()
    
    # If stack is empty, all brackets are balanced
    return not stack

# Test the function with the given examples
print(is_balanced("{asdsdaS}"))  # Output: True
print(is_balanced("{[}]"))      # Output: False, as per the correct balanced check
print(is_balanced("({[})"))     # Output: False
