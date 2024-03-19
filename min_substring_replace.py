def min_substring_replace(s):
    n = len(s)
    target_count = n // 4
    count = {'B': 0, 'D': 0, 'U': 0, 'H': 0}
    
    # Count the occurrences of each character in the string
    for char in s:
        if char in count:
            count[char] += 1
    
    # Find the minimum length of the substring to replace
    min_length = n
    left = 0
    for right in range(n):
        count[s[right]] -= 1
        while all(x <= target_count for x in count.values()) and left <= right:
            min_length = min(min_length, right - left + 1)
            count[s[left]] += 1
            left += 1
    
    return min_length

# Example usage:
input_string = "HBBBUBBB"
print(min_substring_replace(input_string))
# https://leetcode.com/discuss/interview-question/4357263/Amazon-Online-Assessment-question
