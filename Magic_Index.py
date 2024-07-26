# https://doocs.github.io/leetcode/en/lcci/8.3/


def find_magic_index(nums):
    layer = []
    def binary_search(nums, left, right):
        layer.append(1)
        print("left:", left, "right:", right, "layer:", layer)
        if left > right:
            layer.pop()
            return -1
        
        mid = (left + right) >> 1

        if nums[mid] == mid:
            return mid
        
        # Search left half
        print("111111111111111111111111111111111111111", "left:", left, "right:", right, "mid:", mid, "layer", layer)
        left_index = binary_search(nums, left, mid - 1)
        
        if left_index != -1:
            layer.pop()
            print("20202020202020 layer:", layer)
            return left_index
        
        # Search right half
        print("222222222222222222222222222222222222222", "left:", left, "right:", right, "mid:", mid,"layer", layer)
        
        ans = binary_search(nums, mid + 1, right)
        layer.pop()
        return ans
    
    return binary_search(nums, 0, len(nums) - 1)

# Example usage:
nums2 = [1, 2, 1, 1, 1, 5]
print(find_magic_index(nums2))  # Output: 1
