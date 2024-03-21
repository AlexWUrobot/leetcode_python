# https://leetcode.com/discuss/interview-question/4291609/Amazon-or-SDE-Online-Assessment
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



# The time complexity of the provided Python code is O(n^3). Here’s why:
# There are two nested loops, where the outer loop runs n times and the inner loop runs up to n times in the worst case, giving us O(n^2) for these loops.
# Inside the inner loop, we’re creating a sub-array and finding its maximum value. The max() function runs in O(n) time in the worst case, as it has to check each element of the sub-array.
# So, combining these, we have O(n^2) * O(n) = O(n^3) for the overall time complexity of the function. This means that the time taken by the algorithm increases cubically with the number of elements in the input array.


