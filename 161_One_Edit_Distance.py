class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        ls = len(s)
        lt = len(t)
        if abs(ls-lt) > 1 or t == s:    # same or oversize
            return False

        for i in range ( min(ls,lt) ):
            if s[i] != t[i]:
                return s[i+1:]==t[i+1:] or s[i+1:] == t[i:] or s[i:] == t[i+1:]    # replace or delete or add
        # to deal with on char
        return True  # there is no length to deal with false
