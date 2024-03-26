# https://fastprep.gitbook.io/amazon-2024-oa

def getMeanRankCount(rank):
    n = len(rank)
    mean_rank_count = [0] * n

    # Iterate over each possible mean value
    for x in range(1, n + 1):
        # Check each subarray for the mean value
        for start in range(n):
            for end in range(start, n):
                subarray = rank[start:end + 1]
                if sum(subarray) / len(subarray) == x:
                    mean_rank_count[x - 1] += 1

    return mean_rank_count

# Example usage:
rank = [1, 2, 3, 4, 5]
print(getMeanRankCount(rank))

# The time complexity of the provided Python code is O(n^3). This is because there are three nested loops:

# The outermost loop runs n times (for each possible mean value x).
# The middle loop runs up to n times to determine the start of the subarray.
# The innermost loop also runs up to n times to determine the end of the subarray.
# Each iteration of the innermost loop involves calculating the sum and mean of the subarray, which is O(k) where k is the number of elements in the subarray. However, since k is at most n, and these calculations are within the innermost loop, the overall time complexity remains O(n^3).

# For large values of n, this code may not be efficient due to the high time complexity. If you’re looking for a more optimized solution, I can assist with that as well. Just let me know!
