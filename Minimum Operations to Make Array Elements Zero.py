#https://www.fastprep.io/problems/amazon-minimum-operations-to-make-array-elements-zero

def amazon_min_operations(nums):
    cur_sum = 0  # Initialize a variable to keep track of the cumulative sum.
    count = 0     # Initialize a variable to count the total number of operations.

    # Iterate through the array in reverse order.
    for i in range(len(nums) - 1, -1, -1):
        delta = nums[i] + cur_sum  # Calculate the difference between the current element and the cumulative sum.
        print("delta:",delta,  end=' ')
        if delta > 0:
            # If the difference is positive, update the count and adjust the cumulative sum.
            count += delta
            cur_sum -= delta
        elif delta < 0:
            # If the difference is negative, update the count and adjust the cumulative sum.
            count += abs(delta)
            cur_sum += abs(delta)
        print("cur_sum",cur_sum)

    return count  # Return the total count of operations.


# Example usage
arr = [3, 2, 1]
result = amazon_min_operations(arr)
print(result)  # Output: 3


# Example usage
arr = [1, 2, 3]
result = amazon_min_operations(arr)
print(result)  # Output: 3
