
# https://www.fastprep.io/problems/get-min-cost-data


def get_min_cost_data(data):
    # Initialize an array to keep track of character counts (26 letters)
    count = [0] * 26
    
    # Count occurrences of non-'?' characters
    for char in data:
        if char != '?':
            count[ord(char) - ord('a')] += 1

    cost = 0
    result = []
    for char in data:
        if char != '?':
            # Append non-'?' characters to the result
            result.append(char)
            # Update cost based on character count
            cost += count[ord(char) - ord('a')] - 1
        else:
            # Find the minimum value from the count array
            min_value = min(count)
            # Get the index of the minimum value
            min_index = count.index(min_value)
            # Determine the corresponding character
            min_char = chr(ord('a') + min_index)
            # Append the chosen character to the result
            result.append(min_char)
            # Update count and cost
            count[min_index] += 1
            cost += 1

    return ''.join(result)

# Example usage:
input_data = "aaaa?aaaa"
output = get_min_cost_data(input_data)
print(output)  


# Example usage:
input_data = "??????"
output = get_min_cost_data(input_data)
print(output) 

# Example usage:
input_data = "abcd?"
output = get_min_cost_data(input_data)
print(output) 
