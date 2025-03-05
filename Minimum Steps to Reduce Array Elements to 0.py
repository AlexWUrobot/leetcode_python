# https://www.fastprep.io/problems/amazon-minimum-operations-to-make-array-elements-zero

# https://chatgpt.com/share/67c7e0f7-5b48-8005-91d7-f775a486323a

def amazon_min_operations(nums):
    cur_sum = 0
    count = 0
    
    for i in range(len(nums) - 1, -1, -1):
        delta = nums[i] + cur_sum
        if delta > 0:
            count += delta
            cur_sum -= delta
        elif delta < 0:
            count += abs(delta)
            cur_sum += abs(delta)
    
    return count

# Example usage
arr = [3, 2, 1]
print(amazon_min_operations(arr))  # Output: 3


# Example usage
arr = [4, 4, 3]
print(amazon_min_operations(arr))  # Output: 4


# Example usage
arr = [2, 1, 0]
print(amazon_min_operations(arr))  # Output: 2
