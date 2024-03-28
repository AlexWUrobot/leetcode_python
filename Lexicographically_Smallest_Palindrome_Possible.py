# https://www.fastprep.io/problems/amazon-lexicographically-smallest-palindrome-possible

def lexicographically_smallest_palindrome(s):
    s = list(s)
    n = len(s)
    i, j = 0, n - 1
    
    while i < j:
        if s[i] == '?' and s[j] != '?':
            s[i] = s[j]
        elif s[i] != '?' and s[j] == '?':
            s[j] = s[i]
        elif s[i] == '?' and s[j] == '?':
            s[i] = s[j] = 'a'  # Replace '?' with 'a'
        elif s[i] != s[j]:
            return "-1"  # If characters at both ends are not same and not '?', palindrome not possible
        i += 1
        j -= 1
    
    # After the loop, i and j may be equal for odd-length strings, handle the middle character
    if i == j and s[i] == '?':
        s[i] = 'a'  # If middle character is '?', replace with 'a'
    
    return ''.join(s)

# Test cases
test_cases = ["a?rt???", "bx??tm", "ai?a??a"]
for s in test_cases:
    print("Input:", s)
    print("Output:", lexicographically_smallest_palindrome(s))
    print()
