# https://www.fastprep.io/problems/amazon-reduce-gifts
def reduceGifts(prices, k, threshold):
    # If the number of prices is less than k, no removals are needed
    if len(prices) < k:
        return 0
    
    # Sort the prices in ascending order
    prices.sort()

    # Calculate the sum of the highest k prices
    current_sum = sum(prices[-k:])
    
    # If the sum of the highest k prices is within the threshold, no removals are needed
    if current_sum <= threshold:
        return 0
    
    # If the sum of the lowest k prices exceeds the threshold, remove all but one item
    if sum(prices[:k]) > threshold:
        return len(prices) - (k - 1)
    
    # Initialize a counter for removals
    removals = 0
    
    # While the sum of the highest k prices exceeds the threshold and there are more than k prices
    while current_sum > threshold and len(prices) > k:
        prices.pop()  # Remove the highest price
        current_sum = sum(prices[-k:])
        removals += 1
    
    return removals
# Example usage
prices = [3, 2, 1, 4, 6, 5]
k = 3
threshold = 14
result = reduceGifts(prices, k, threshold)
print(f"Minimum items to remove: {result}")

# Example usage
prices = [9, 6, 7, 2, 7, 2]
k = 2
threshold = 13
result = reduceGifts(prices, k, threshold)
print(f"Minimum items to remove: {result}")

# Example usage
prices = [9, 6, 3, 2, 9, 10, 10, 11]
k = 4
threshold = 1
result = reduceGifts(prices, k, threshold)
print(f"Minimum items to remove: {result}")


