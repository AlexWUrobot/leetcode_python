# # https://leetcode.com/company/amazon/discuss/1826385/Amazon-or-Research-Scientist-Intern-or-Accept


# Function to find the length of the longest sequence of same consecutive numbers in an array.
def find_longest_consecutive_same_sequence(arr):
    # Return 0 if the array is empty.
    if not arr:
        return 0

    # Initialize the maximum sequence length and the current sequence length.
    max_length = 1
    current_length = 1
    same_number = 0

    # Iterate through the array starting from the second element.
    for i in range(1, len(arr)):
        # If the current element is the same as the previous one, increment the current sequence length.
        if arr[i] == arr[i - 1]:
            current_length += 1
            
            if current_length > max_length:
                same_number = arr[i]
                
            # Update the maximum sequence length if the current sequence is longer.
            max_length = max(max_length, current_length)
        else:
            # Reset the current sequence length if the current and previous elements are different.
            current_length = 1
    
    print("same number:", same_number)
    # Return the maximum sequence length found.
    return max_length

# Example usage:
# Define an array with a sequence of numbers.
array = [4, 4, 4, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4]
# Call the function and print the result.
print(find_longest_consecutive_same_sequence(array))
