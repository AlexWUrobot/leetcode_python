# https://www.fastprep.io/problems/amazon-get-pairs-count


def get_pairs_count(process, k):
    process.sort()  # Sort the process array
    count = 0
    left, right = 0, 0  # Initialize two pointers to the start of the array

    while right < len(process):
        # Find a pair where the difference is within k
        if process[right] - process[left] <= k:
            # Instead of incrementing count by (right - left) directly,
            # we increment it when we know a valid pair is found, accounting for all pairs between left and right
            count += right - left  # Count the pairs between the current left and right
            right += 1  # Expand the window to the right
        else:
            left += 1  # Shrink the window from the left
            if left == right:  # Ensure right is always ahead of left
                right += 1

    return count
    
process = [100, 200, 300, 400]
k = 250
print(get_pairs_count(process, k))

process = [10, 12, 11]
k = 0
print(get_pairs_count(process, k))

process = [7, 10, 13, 11]
k = 3
print(get_pairs_count(process, k))
