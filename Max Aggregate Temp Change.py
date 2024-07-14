# https://www.fastprep.io/problems/amazon-get-max-aggregate-temperature-change



def getMaxAggregateTemperatureChange(tempChange):
    n = len(tempChange)
    prefixSums = [0] * n
    suffixSums = [0] * n
    
    # Compute prefix sums
    prefixSums[0] = tempChange[0]
    for i in range(1, n):
        prefixSums[i] = prefixSums[i - 1] + tempChange[i]
    
    # Compute suffix sums
    suffixSums[n - 1] = tempChange[n - 1]
    for i in range(n - 2, -1, -1):
        suffixSums[i] = suffixSums[i + 1] + tempChange[i]
    
    # Find maximum aggregate temperature change
    maxAggregateChange = float('-inf')
    for i in range(n):
        maxChange = max(prefixSums[i], suffixSums[i])
        maxAggregateChange = max(maxAggregateChange, maxChange)
    
    return maxAggregateChange

# Example usage
tempChange = [6, -2, 5]
result = getMaxAggregateTemperatureChange(tempChange)   # 9
print(f"Maximum aggregate temperature change: {result}")


# Example usage
tempChange = [-1, 2, 3]
result = getMaxAggregateTemperatureChange(tempChange)  # 5
print(f"Maximum aggregate temperature change: {result}")
