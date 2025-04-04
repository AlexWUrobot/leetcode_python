# https://www.fastprep.io/problems/uber-count-the-number-of-good-subarrays
# https://chatgpt.com/share/67ef39b4-dddc-8004-b4db-f3800bcdca87

from collections import defaultdict

def count_good_subarrays(nums, k):
    n = len(nums)
    freq = defaultdict(int)
    left = 0
    count_pairs = 0
    result = 0

    for right in range(n):
        # Add nums[right] to the frequency map
        count_pairs += freq[nums[right]]
        freq[nums[right]] += 1

        # Shrink the window from the left if count_pairs >= k
        while count_pairs >= k:
            # All subarrays from left to right to end are valid
            result += n - right
            freq[nums[left]] -= 1
            count_pairs -= freq[nums[left]]
            left += 1

    return result
    
print(count_good_subarrays([1,1,1,1,1], 10))        # Output: 1
print(count_good_subarrays([3,1,4,3,2,2,4], 2))     # Output: 4
