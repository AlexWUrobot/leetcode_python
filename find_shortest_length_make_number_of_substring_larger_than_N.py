# https://leetcode.com/discuss/interview-question/2325441/Amazon-Online-Assessment-Question


def find_shortest_length(n):
    # Initialize an array to store counts of characters 'z', 'e', 'r', and 'o' respectively
    dp = [1, 1, 1, 1]
    # Initialize a variable to keep track of the product of elements in dp
    mult = 1
    # Initialize an index iterator to iterate over elements of dp
    idx_iter = -1
    # Loop until the product of elements in dp is less than n
    while mult < n:
        # Increment the index iterator, and if it exceeds the last index, reset it to 0
        idx_iter = idx_iter + 1 if idx_iter < 3 else 0
        # Update the product by dividing it by the current element at idx_iter
        mult /= dp[idx_iter]
        # Increment the current element at idx_iter
        dp[idx_iter] += 1
        # Update the product by multiplying it by the updated element at idx_iter
        mult *= dp[idx_iter]
    # Return the sum of all elements in dp, which represents the length of the shortest string
    return sum(dp)

# Test the function with an example input and print the result
print(find_shortest_length(12))
