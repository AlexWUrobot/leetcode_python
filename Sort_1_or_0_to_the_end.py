# Sort 1's and 0's in array to the end

# https://leetcode.com/discuss/interview-question/1471459/Amazon-OA

def countMovesToLeft(nums, target):
	count = 0
	last = 0
	for i in range(len(nums)):
		if nums[i] == target:
			count += i - last
			last += 1
	return count
	

nums = [1,1,1,0,0,0]
print( min(countMovesToLeft(nums, 1), countMovesToLeft(nums, 0)))


nums = [0,0,0,1,1,1]
print( min(countMovesToLeft(nums, 1), countMovesToLeft(nums, 0)))


nums = [0,0,0,0,1,0,1,0,0]
print( min(countMovesToLeft(nums, 1), countMovesToLeft(nums, 0)))


nums = [0,0,1,0,1,0]
print( min(countMovesToLeft(nums, 1), countMovesToLeft(nums, 0)))
