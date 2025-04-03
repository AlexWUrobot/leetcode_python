# https://www.fastprep.io/problems/uber-match-subarray-to-pattern

def count_matching_subarrays(numbers, pattern):
    count = 0
    n, m = len(numbers), len(pattern)
    
    for i in range(n - m):
        matches = True
        for j in range(m):
            if pattern[j] == 1 and numbers[i + j + 1] <= numbers[i + j]:
                matches = False
                break
            elif pattern[j] == 0 and numbers[i + j + 1] != numbers[i + j]:
                matches = False
                break
            elif pattern[j] == -1 and numbers[i + j + 1] >= numbers[i + j]:
                matches = False
                break
        if matches:
            count += 1
    
    return count

# Example usage:
numbers = [4, 1, 3, 4, 4, 5, 5, 1]
pattern = [1, 0, -1]
print(count_matching_subarrays(numbers, pattern))  # Output: 1
