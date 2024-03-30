# https://leetcode.com/discuss/interview-question/4804678/Amazon-OA-Reverse-Binary-String/
# https://www.fastprep.io/problems/amazon-reverse-binary-string
def solve(s):
    n = len(s)

    # Reverse the string
    rev = s[::-1]
    
    lp = 0
    # Iterate through each character in the string
    for i in range(n):
        # If the characters in original and reversed string match, increment lp
        if s[i] == rev[lp]:
            lp += 1

    # Return the difference between the length of the string and lp
    return n - lp

# Test the function
print(solve("00110101"))  # Output: 3
