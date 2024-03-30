# https://www.fastprep.io/problems/amazon-maximum-times-word-removed

from collections import Counter

def maximumTimesWordRemoved(s, t):
    # Count the frequency of each character in s and t
    s_count = Counter(s)
    t_count = Counter(t)
    
    # Find the minimum ratio of s_count to t_count for each character in t
    max_times = float('inf')
    for char in t_count:
        if char not in s_count:
            return 0
        max_times = min(max_times, s_count[char] // t_count[char])
    
    return max_times

# Example usage:
s1 = "abacbc"
t1 = "bca"
print(maximumTimesWordRemoved(s1, t1))  # Output: 2

s2 = "abdadccacd"
t2 = "edac"
print(maximumTimesWordRemoved(s2, t2))  # Output: 0
