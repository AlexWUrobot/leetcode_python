# https://www.fastprep.io/problems/amazon-get-max-total-area


def getMaxTotalArea(sideLengths):
    """
    Calculates the maximum total area of rectangles that can be formed using side lengths from the input list.

    Args:
        sideLengths (List[int]): A list of positive integers representing side lengths.

    Returns:
        int: The maximum total area modulo 10^9 + 7.
    """
    if len(sideLengths) < 4:
        return 0

    MOD = 10**9 + 7

    # Create a frequency dictionary to count occurrences of each side length
    freq = {}
    for length in sideLengths:
        freq[length] = freq.get(length, 0) + 1

    # Initialize a list to store pairs of side lengths
    pair = []
    for length in sorted(freq.keys(), reverse=True):
        while freq[length] >= 2:
            freq[length] -= 2
            pair.append(length)
        if freq[length] == 1 and length - 1 in freq and freq[length-1] > 0:
            pair.append(length-1)
            freq[length] -= 1
            freq[length-1] -= 1

    # Calculate the total area by multiplying adjacent pairs of side lengths
    area = 0
    for i in range(1, len(pair), 2):
        area += pair[i] * pair[i-1]

    return area % MOD
    
sideLengths = [2, 6, 2, 6, 3, 5]
print(getMaxTotalArea(sideLengths))# 12

sideLengths = [2, 3, 3, 4, 6, 8, 8, 6]
print(getMaxTotalArea(sideLengths))# 54

sideLengths = [3, 4, 5, 5, 6]
print(getMaxTotalArea(sideLengths))# 20
