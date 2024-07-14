# https://www.fastprep.io/problems/amazon-count-pairs


def countPairs(numbers, k):
    # Create a set from the list to ensure distinct elements
    distinct_numbers = set(numbers)
    count = 0

    # Iterate over each number in the set
    for number in distinct_numbers:
        # Check if the pair (number, number + k) exists in the set
        if number + k in distinct_numbers:
            count += 1

    return count

# Example usage:
numbers1 = [1, 1, 1, 2]
k1 = 1
print(countPairs(numbers1, k1))  # Output: 1

numbers2 = [1, 2]
k2 = 0
print(countPairs(numbers2, k2))  # Output: 2
