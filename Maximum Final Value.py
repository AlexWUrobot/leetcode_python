# https://www.fastprep.io/problems/amazon-maximum-final



def maximum_final(arr):
    arr.sort()
    n = len(arr)
    for i in range(1, n):
        if arr[i] - arr[i-1] > 1:
            arr[i] = arr[i-1] + 1
    return arr[-1]



arr = [3, 1, 3, 4]
print(maximum_final(arr))


arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
print(maximum_final(arr))


arr = [1, 1, 2, 3, 5, 8, 13, 21]
print(maximum_final(arr))

arr = [100, 1, 100, 1, 100, 1]
print(maximum_final(arr))
