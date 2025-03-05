# https://algo.monster/problems/amazon-oa-merge-intervals


def merge_intervals(intervals):
    if not intervals:
        return []
    
    # Sort intervals based on the start time
    intervals.sort()
    
    merged = [intervals[0]]
    
    for start, end in intervals[1:]:
        last_end = merged[-1][1]
        
        if start <= last_end:  # Overlapping intervals
            merged[-1][1] = max(last_end, end)  # Merge intervals
        else:
            merged.append([start, end])
    
    return merged

# Example usage
intervals = [[7,7],[2,3],[6,11],[1,2]]
print(merge_intervals(intervals))  # Output: [[1,3],[6,11]]


#  O(n log n) + O(n) = O(n log n)
