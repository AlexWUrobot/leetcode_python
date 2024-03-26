# https://leetcode.com/discuss/interview-question/1532572/amazon-oa-max-profit


def contprofit(arr, k):
    profits = 0
    if 2*k == len(arr):
        return sum(arr)  # boundary condition, select all
    
    for i in range(len(arr) - k):
        window = sum(arr[i : i + k])
        for j in range(i + k, len(arr)):
            nextwindow = sum(arr[j : j + k])
            if j + k > len(arr) - 1:
                diff = (j + k) - len(arr)
                nextwindow += sum(arr[0:diff])
            profits = max(profits, window + nextwindow)
    return profits

k = 1 
arr = [3,-5]
print(contprofit(arr, k))


k = 2
arr = [1,5,1,3,7,-3]
print(contprofit(arr, k))
