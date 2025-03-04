# Create lexicographically minimum String using given operation
# https://www.geeksforgeeks.org/create-lexicographically-minimum-string-using-given-operation/
# https://www.fastprep.io/problems/amazon-best-way-to-pack

def bestWayToPack(s):
 
    n = len(s)
    suf = [0 for _ in range(n)]
    sol = ""
 
    # Storing values in suf
    suf[n - 1] = ord(s[n - 1]) - ord('0')
    for i in range(n-2, -1, -1):
        suf[i] = min(suf[i + 1], ord(s[i]) - ord('0'))
 
    # Storing values of final sequence
    # after performing given operation
    res = []
    for i in range(0, n):
 
        # If smaller element is present
        # beyond index i
        if (suf[i] < ord(s[i]) - ord('0')):
            res.append(min(9, ord(s[i]) - ord('0') + 1))
        else:
            res.append(ord(s[i]) - ord('0'))
 
    # Sort the res in increasing order
    res.sort()
    for x in res:
        sol += str(x)
 
    return sol

id = "26547"

print(bestWayToPack(id))
