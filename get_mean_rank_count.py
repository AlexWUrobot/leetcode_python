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
