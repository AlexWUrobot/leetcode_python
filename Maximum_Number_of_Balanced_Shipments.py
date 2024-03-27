# https://www.fastprep.io/problems/amazon-maximum-number-of-shipments


def split_array(weights):
    groups = []
    current_group = []
    max_so_far = float('-inf')

    for i, weight in enumerate(weights):
        # Update the maximum number encountered so far
        max_so_far = max(max_so_far, weight)

        # Add weight to the current group
        current_group.append(weight)

        # Check if this is the last element, or if the next element is greater
        if (i == len(weights) - 1) or (weights[i + 1] > weight):
            # If the current group has more than one element and the last element is not the max
            if len(current_group) > 1 and current_group[-1] != max_so_far:
                groups.append(current_group)
                current_group = []
            max_so_far = float('-inf')  # Reset for the next group

    # Add the remaining group if it's not empty and doesn't end with the max
    if current_group and current_group[-1] != max_so_far:
        groups.append(current_group)

    return groups

# Example usage
weights = [4, 3, 6, 5, 3, 4, 7, 1]
print(split_array(weights))
