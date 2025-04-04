
# https://www.fastprep.io/problems/uber-minimum-right-shifts-to-sort-the-array

def minimumRightShiftsToSortArray(nums):
    n = len(nums)
    drop_index = -1

    for i in range(1, n):
        if nums[i] < nums[i - 1]:
            if drop_index != -1:
                return -1  # More than one drop, can't be sorted with shifts
            drop_index = i

    if drop_index == -1:
        return 0  # Already sorted

    # Rotate and check if sorted
    rotated = nums[drop_index:] + nums[:drop_index]
    if all(rotated[i] <= rotated[i + 1] for i in range(n - 1)):
        return n - drop_index

    return -1
    
    
    
nums = [3,4,5,1,2]    
print(minimumRightShiftsToSortArray(nums))


nums = [2,1,4] 
print(minimumRightShiftsToSortArray(nums))
