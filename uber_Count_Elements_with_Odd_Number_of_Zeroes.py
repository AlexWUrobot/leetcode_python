# https://www.fastprep.io/problems/uber-count-elements

def count_odd_zeroes(arr):
    count = 0
    for num in arr:
        zero_count = str(num).count('0')  # Count occurrences of '0' in the number
        if zero_count % 2 == 1:  # Check if the count is odd
            count += 1
    return count

# Example usage:
a = [20, 11, 10, 10070, 7]
print(count_odd_zeroes(a))  # Output: 3
