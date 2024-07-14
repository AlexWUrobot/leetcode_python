


# https://github.com/Rohit91singh9/Coding-DP-DSA/blob/main/findEarliestmonth.py

# https://www.fastprep.io/problems/amazon-find-earliest-month


import math
# 1st Approach
def findEarliestMonth(stockPrice):
    """
    Finds the earliest month with the smallest difference in average stock price.

    Args:
        stockPrice (list): List of stock prices for each month.

    Returns:
        int: Index of the earliest month with the smallest difference in average stock price.
    """
    n = len(stockPrice)  # Number of months
    first = stockPrice[0]  # Initial sum of stock prices
    average_frst = math.floor(first)  # Floor of the average of the first month
    second = sum(stockPrice[1:])  # Sum of stock prices from the second month onwards
    average_scnd = math.floor(second / (n - 1))  # Floor of the average of the remaining months
    diff = abs(average_frst - average_scnd)  # Initialize the minimum difference
    result = 1  # Initialize the result (earliest month index)

    for i in range(1, n - 1):
        # Update the cumulative sums
        first += stockPrice[i]
        second -= stockPrice[i]

        # Calculate the updated averages
        average_frst = math.floor(first / (i + 1))
        average_scnd = math.floor(second / (n - i - 1))

        # Update the minimum difference and result if needed
        difference_temp = abs(average_frst - average_scnd)
        if difference_temp < diff:
            diff = difference_temp
            result = i + 1

    return result

stockPrice = [1, 3, 2, 3]
print(findEarliestMonth(stockPrice))# 2

stockPrice = [1, 3, 2, 4, 5]
print(findEarliestMonth(stockPrice))# 2
