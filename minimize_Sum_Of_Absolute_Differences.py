# https://www.fastprep.io/problems/amazon-minimize-sum-of-absolute-differences
# more difficult : https://www.geeksforgeeks.org/minimize-sum-of-absolute-differences-between-given-arrays-by-replacing-at-most-1-element-from-first-array/


def minimizeSumOfAbsoluteDifferences(a, b):
    n = len(a)
    a.sort()
    b.sort()
    total_diff = 0
    pairings = []
    
    for i in range(n):
        total_diff += abs(a[i] - b[i])
        pairings.append((a[i], b[i]))
    
    pairing_str = " + ".join(f"|{pair[0]} - {pair[1]}|" for pair in pairings)
    print(f"{pairing_str} = {total_diff}")
    
    return total_diff

# Example usage:
a1 = [3, 2, 1]
b1 = [2, 1, 3]
print("Example 1:")
print("Output:", minimizeSumOfAbsoluteDifferences(a1, b1))  # Output: 0

a2 = [4, 1, 8, 7]
b2 = [2, 3, 6, 5]
print("Example 2:")
print("Output:", minimizeSumOfAbsoluteDifferences(a2, b2))  # Output: 6
