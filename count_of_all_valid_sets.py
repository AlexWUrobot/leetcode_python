def valid_sets(arr):
    # Function to count the number of valid sets
    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(i, n):
            sub_arr = arr[i:j+1]
            max_val = max(sub_arr)
            if max_val == sub_arr[0] or max_val == sub_arr[-1]:
                count += 1
    return count

# Example usage:
n = 3
arr = [2, 3, 1]
print("Total valid sets:", valid_sets(arr))
