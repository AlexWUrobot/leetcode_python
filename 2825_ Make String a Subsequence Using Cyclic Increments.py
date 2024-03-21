class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        # Initialize pointers for str1 (l) and str2 (r)
        l, r = 0, 0
        
        # Loop through both strings as long as we haven't reached the end of either
        while l < len(str1) and r < len(str2):
            # Check if the current characters in str1 and str2 match,
            # or if the next character in the alphabet of str1's current character matches str2's current character
            if str1[l] == str2[r] or chr((ord(str1[l]) - 96) % 26 + 97) == str2[r]:
                # If there's a match, move the pointer in str2 to check the next character
                r += 1
            # Always move the pointer in str1 to continue checking against str2's current character
            l += 1
        
        # If we've gone through all of str2, then str2 is a subsequence of str1
        return r >= len(str2)
