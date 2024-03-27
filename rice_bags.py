# https://www.fastprep.io/problems/max-set-size
# https://medium.com/@yunhua.zhang94/amazon-oa-rice-bags-d4bcb9965433
# https://leetcode.com/discuss/interview-question/4628170/Amazon-OA


from typing import List

def func(arr: List[int]) -> int:
    n = len(arr)
    max_length = 0
    for i in range(n):
        cur = arr[i]
        tmp = [cur,]
        while cur**2 in arr:
            tmp.append(cur**2)
            cur = cur**2
        if len(tmp) > 1:
            max_length = max(max_length, len(tmp))

    return max_length

riceBags = [625, 4, 2, 5, 25]
print(riceBags, "output:", func(riceBags))

riceBags = [3, 9, 4, 2, 16]
print(riceBags, "output:", func(riceBags))

riceBags = [3, 9, 4, 2, 16, 256]
print(riceBags, "output:", func(riceBags))


# another solution :


# def max_size_perfect_set(nums):
#     nums_set = set(nums)
#     max_size = 0

#     for num in nums:
#         current_size = 1
#         current_num = num
#         while current_num * current_num in nums_set:
#             current_num *= current_num
#             current_size += 1
#         if current_size >= 2:
#             max_size = max(current_size, max_size)

#     return max_size
