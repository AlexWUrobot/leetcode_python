# https://medium.com/@yunhua.zhang94/amazon-oa-maximum-final-value-8dadee505e16


def maximumFinal(arr):
    # Step 1: Sort the array
    arr.sort()
    
    # Step 2: Set the first element to 1
    arr[0] = 1
    
    # Step 3: Adjust the array to maintain the constraint arr[i] - arr[i-1] <= 1
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1] + 1:
            arr[i] = arr[i-1] + 1
    
    # Step 4: Return the last element as the maximum possible value
    return arr[-1]

# Example usage
print(maximumFinal([3, 1, 3, 4]))  # Output: 4
print(maximumFinal([1, 3, 2, 2]))  # Output: 3
print(maximumFinal([3, 2, 3, 5]))  # Output: 4
