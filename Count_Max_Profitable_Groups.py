# https://www.fastprep.io/problems/count-maximum-profitable-groups
# https://fastprep.gitbook.io/amazon-2024-oa/count-max-profitable-groups-or-ft
def countMaximumProfitableGroups(stockPrice):
    n = len(stockPrice)
    # Initialize count of profitable groups
    count = 0
    
    # Check all possible subarrays
    for l in range(n):
        for r in range(l, n):
            # Extract the subarray
            subarray = stockPrice[l:r+1]
            # Check if the first or last element is the maximum of the subarray
            if subarray[0] == max(subarray) or subarray[-1] == max(subarray):
                count += 1
                
    return count

# Example usage:
stockPrice1 = [3, 1, 3, 5]
print(countMaximumProfitableGroups(stockPrice1))  # Output: 10

stockPrice2 = [1, 5, 2]
print(countMaximumProfitableGroups(stockPrice2))  # Output: 5

stockPrice3 = [2, 3, 2]
print(countMaximumProfitableGroups(stockPrice3))  # Output: 5
