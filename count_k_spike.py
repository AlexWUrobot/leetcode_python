#https://fastprep.gitbook.io/amazon-2024-oa/2023-june-aug/count-spikes
def countkSpikes(prices, k):
    # Initialize the length of the prices array
    n = len(prices)
    # Initialize the count of k-Spikes
    k_spikes_count = 0

    # Iterate through each price in the array
    for i in range(n):
        # Count how many elements before the current element are less than the current element
        left_count = sum(1 for left in prices[:i] if left < prices[i])
        # Count how many elements after the current element are less than the current element
        right_count = sum(1 for right in prices[i+1:] if right < prices[i])

        # If both counts are greater than or equal to k, it's a k-Spike
        if left_count >= k and right_count >= k:
            k_spikes_count += 1

    # Return the total count of k-Spikes
    return k_spikes_count

# Example usage:
prices = [1, 3, 2, 5, 4]
k = 1
# The function call prints the number of k-Spikes in the prices array
print(countkSpikes(prices, k))  # Output: 2


prices = [1, 2, 8, 5, 3, 4]
k = 2
print(countkSpikes(prices, k))  # Output: 2
