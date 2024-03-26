# https://www.fastprep.io/problems/max-set-size
# https://medium.com/@yunhua.zhang94/amazon-oa-rice-bags-d4bcb9965433
from typing import List

def func(arr: List[int]) -> int:
    n = len(arr)
    max_length = 0
    for i in range(n):
        cur = arr[i]
        tmp = [cur,]
        while cur**2 in arr:
            tmp.append(cur**2)
            cur = cur**2
        if len(tmp) > 1:
            max_length = max(max_length, len(tmp))

    return max_length

riceBags = [625, 4, 2, 5, 25]
print(riceBags, "output:", func(riceBags))

riceBags = [3, 9, 4, 2, 16]
print(riceBags, "output:", func(riceBags))

riceBags = [3, 9, 4, 2, 16, 256]
print(riceBags, "output:", func(riceBags))
