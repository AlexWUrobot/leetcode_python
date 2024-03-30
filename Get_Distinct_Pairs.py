# https://www.fastprep.io/problems/amazon-get-distinct-pairs
def getDistinctPairs(stocksProfit, target):
    # Sort the list to handle duplicates and ease pair formation
    stocksProfit.sort()
    seen = set()
    pairs = set()

    for profit in stocksProfit:
        if target - profit in seen:
            pairs.add((profit, target - profit) if profit <= target - profit else (target - profit, profit))
        seen.add(profit)

    # Print the distinct pairs
    for pair in pairs:
        print(pair)

    return len(pairs)

# Example usage:
stocksProfit = [5, 7, 9, 13, 11, 6, 6, 3, 3]
target = 12
print("Number of distinct pairs:", getDistinctPairs(stocksProfit, target))
