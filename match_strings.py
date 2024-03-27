# https://www.fastprep.io/problems/amazon-match-strings
#


def matchStrings(text, pat):
    def match(text, pattern):
        # Split the pattern by the wildcard character
        parts = pattern.split('*')
        
        # Check if the text starts with the first part and ends with the last part of the pattern
        if not text.startswith(parts[0]) or not text.endswith(parts[1]):
            return "NO"
        
        # Check if the middle part of the text (excluding the first and last parts of the pattern) 
        # only contains lowercase letters
        middle = text[len(parts[0]):-len(parts[1])]
        return "YES" if all(c.islower() for c in middle) else "NO"
    
    # Apply the match function to each pair of text and pattern
    return [match(t, p) for t, p in zip(text, pat)]

# Example usage:
text = ["abcbcd","abcefgbcd","abcbd","abzbcd","code", "coder","hackerrank", "hackerrnak","hackerrank"]
pat = ["abc*bcd","abc*bcd","abc*bcd","abc*bcd","co*d", "co*er","hac*rank", "hac*rnak", "hac*rnak" ]
print(matchStrings(text, pat))
