# https://nickel-suede-088.notion.site/Three-Amazon-1ad181310f458050bbdaf234bfc8adc6


def findLongestRegex(x, y, z):
    if z == x or z == y:
        return "-1"
    
    heap = []
    for i in range(len(z)):
        if z[i] != x[i] and z[i] != y[i]:
            heap.append((z[i], i))
    
    heap = sorted(heap, key = lambda x : x[0], reverse = True)
    maxChar, maxIdx = heap[0]
    
    ans = ""
    regex = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    modRegex = [x for x in regex if x != maxChar]
    
    for i in range(len(z)):
        if i == maxIdx:
            ans = ans + "[" + "".join(modRegex) + "]"
        else:
            ans = ans + "[" + "".join(regex) + "]"
    
    return ans

x = "AB"
y = "BD"
z = "CD"
print(findLongestRegex(x, y, z))

x = "AERB"
y = "ATRC"
z = "AGCB"
print(findLongestRegex(x, y, z))

