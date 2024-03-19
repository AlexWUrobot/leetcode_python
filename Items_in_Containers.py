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



# def numberOfItems(s, startIndices, endIndices):
#     # Convert all indices from 1-based to 0-based for Python indexing
#     startIndices = [i - 1 for i in startIndices]
#     endIndices = [i - 1 for i in endIndices]

#     # Precompute the number of items between each pair of compartments
#     items_between = []
#     count = 0
#     for char in s:
#         if char == '|':
#             items_between.append(count)
#             count = 0
#         elif char == '*':
#             count += 1
#     items_between.append(count)  # Add the last count

#     # Calculate prefix sums of items_between to quickly compute ranges
#     prefix_sums = [0]
#     for count in items_between:
#         prefix_sums.append(prefix_sums[-1] + count)

#     # Helper function to find the index of the next compartment
#     def find_next_compartment(index, direction=1):
#         while 0 <= index < len(s) and s[index] != '|':
#             index += direction
#         return index

#     # Calculate the number of items for each query
#     results = []
#     for start, end in zip(startIndices, endIndices):
#         # Find the compartments that enclose the current range
#         start_compartment = find_next_compartment(start, 1)
#         end_compartment = find_next_compartment(end, -1)

#         # If there is no enclosing compartment, the result is 0
#         if start_compartment >= end_compartment or start_compartment >= len(s) or end_compartment < 0:
#             results.append(0)
#         else:
#             # Calculate the number of items within the enclosed compartments
#             # Ensure the indices for prefix_sums are within the valid range
#             start_compartment = max(0, min(start_compartment, len(prefix_sums) - 1))
#             end_compartment = max(0, min(end_compartment, len(prefix_sums) - 1))
#             result = prefix_sums[end_compartment] - prefix_sums[start_compartment]
#             results.append(result)

#     return results

# # Example usage
# s = '|**|*|*'
# startIndices = [1, 1]
# endIndices = [5, 6]
# print(numberOfItems(s, startIndices, endIndices))  # Output should be [2, 3]
