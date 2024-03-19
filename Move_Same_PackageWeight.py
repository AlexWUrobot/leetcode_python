from collections import Counter

def solve(nums):
    d = Counter(nums)  #  key : value
    ans = 0  # do not forget initial 
    for i in d:    # i will be key 
        if d[i] == 1:   # d[i] will be value 
            return -1
        ans += (d[i]+2)//3
    return ans

print(solve([2, 4, 6, 6, 4, 2, 4]))
