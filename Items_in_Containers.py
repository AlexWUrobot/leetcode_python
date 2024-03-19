# https://leetcode.com/discuss/interview-question/1955152/amazon-online-assessment-demo



def numberOfItems(s, startIndices, endIndices):
    # Preprocess the string to calculate the prefix sum of items
    prefix_sum = [0] * (len(s) + 1)
    compartment_open = False
    item_count = 0

    for i, char in enumerate(s):
        if char == '|':
            compartment_open = True
            prefix_sum[i + 1] = item_count
        elif char == '*' and compartment_open:
            item_count += 1
            prefix_sum[i + 1] = item_count
        else:
            prefix_sum[i + 1] = item_count

    # Function to count items in a single compartment
    def count_items(start, end):
        if start >= end:
            return 0
        start_compartment = end_compartment = 0
        # Find the position of the first compartment opening after start
        for i in range(start, end + 1):
            if s[i - 1] == '|':
                start_compartment = i
                break
        # Find the position of the last compartment closing before end
        for i in range(end, start - 1, -1):
            if s[i - 1] == '|':
                end_compartment = i
                break
        # Return the count of items between the compartments
        return prefix_sum[end_compartment] - prefix_sum[start_compartment]

    # Calculate the number of items for each query
    result = []
    for start, end in zip(startIndices, endIndices):
        result.append(count_items(start, end))

    return result

# Example usage:
s = '|**|*|*'
startIndices = [1, 1]
endIndices = [5, 6]
print(numberOfItems(s, startIndices, endIndices))  # Output: [2, 3]
