# https://www.fastprep.io/problems/amazon-find-overlapping-times

def findOverlappingTimes(intervals):
    if not intervals:
        return []

    # Sort intervals based on start times
    intervals.sort(key=lambda x: x[0])

    merged_intervals = [intervals[0]]
    
    # Iterate through sorted intervals and merge overlapping intervals
    for interval in intervals[1:]:
        if interval[0] <= merged_intervals[-1][1]:
            # Overlapping intervals, merge them
            merged_intervals[-1][1] = max(merged_intervals[-1][1], interval[1])
        else:
            # Non-overlapping interval, add it to the merged intervals
            merged_intervals.append(interval)

    return merged_intervals

# Example usage
intervals = [[7, 7], [2, 3], [6, 11], [1, 2]]
print(findOverlappingTimes(intervals))
