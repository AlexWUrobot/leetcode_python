# https://youtu.be/yygB8BtdTgs?si=efYHeLf0dL6Y80v5
# https://leetcode.com/discuss/interview-question/1332412/Amazon-Online-Assessment-Question

from collections import Counter
from collections import defaultdict
s = "][?)?["
def solve (s):
    right = Counter(s)
    left = defaultdict(int)
    ans = 0
    
    for i, c in enumerate(s[:-1]):
        right[c] -= 1
        left[c] += 1
    
        left_bra_diff = abs(left['['] - left[']'])
        left_par_diff = abs(left['('] - left[')'])
        left_diff = left_bra_diff + left_par_diff
    
        right_bra_diff = abs(right['['] - right[']'])
        right_par_diff = abs(right['('] - right[')'])
        right_diff = right_bra_diff + right_par_diff
    
        if (left_diff <= left['?'] and (left['?'] - left_diff) % 2 == 0) and (right_diff <= right['?'] and (right['?'] - right_diff) % 2 == 0):
            # print i
            ans += 1
    return ans
print(solve(s))


# Approach 2 ###################################################
# def solution(s):
#     ans = 0
#     if s is None:
#         return ans

#     length = len(s)
#     if length % 2 == 1:
#         return ans

#     count = [[0] * length for _ in range(3)]
#     circ_count = rev_circ_count = sq_count = rev_sq_count = 0

#     for i in range(length):
#         c = s[i]  # char from left of string
#         rev_c = s[length - 1 - i]  # char from right of string

#         circ_count += 1 if c == '(' else -1 if c == ')' else 0
#         sq_count += 1 if c == '[' else -1 if c == ']' else 0
#         rev_circ_count += 1 if rev_c == '(' else -1 if rev_c == ')' else 0
#         rev_sq_count += 1 if rev_c == '[' else -1 if rev_c == ']' else 0

#         count[0][i] = abs(circ_count) + abs(sq_count)  # additional brackets needed from left
#         count[1][length - 1 - i] = abs(rev_circ_count) + abs(rev_sq_count)  # additional brackets needed from right
#         count[2][i] = 1 + count[2][i - 1] if c == '?' else 0 if i == 0 else count[2][i - 1]  # count of '?' so far

#     for i in range(1, length - 1):
#         left_diff = count[2][i] - count[0][i]
#         if left_diff >= 0 and left_diff % 2 == 0:  # if the left half is balanced, check the right half
#             right_diff = (count[2][length - 1] - count[2][i]) - count[1][i + 1]
#             if right_diff >= 0 and right_diff % 2 == 0:  # increment counter if the right half is balanced
#                 ans += 1

#     return ans

# # Example usage:
# string_input = "][?)?["
# print("Number of ways to divide the string:", solution(string_input))
# string_input = "[(?][??["
# print("Number of ways to divide the string:", solution(string_input))
# string_input = "][)("
# print("Number of ways to divide the string:", solution(string_input))
# string_input = "][?["
# print("Number of ways to divide the string:", solution(string_input))
