# https://www.fastprep.io/problems/amazon-find-max-value






import heapq
def findMaxValue(factor, data, x):
    if x > sum(factor): return -1
    h = []
    for i, row in enumerate(data):
      h.extend([-n for n in sorted(row, reverse=True)[0:factor[i]]])
    ans = 0
    heapq.heapify(h)
    for _ in range(x):
      ans += heapq.heappop(h)
    return -ans

factor = [1, 2, 1]
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
x = 2

print(findMaxValue(factor, data, x))










# https://chatgpt.com/share/67c856b4-3234-8005-b561-1f9cbb2a0a1e
