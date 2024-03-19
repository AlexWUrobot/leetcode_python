# https://leetcode.com/problems/plates-between-candles/description/
# https://leetcode.com/discuss/interview-question/1955152/amazon-online-assessment-demo

class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        prefix_sum = [0] * (n + 1)
        left_candle = [-1] * n
        right_candle = [n] * n

        # Precompute the prefix sum of plates and the nearest candles to the left and right
        plates = 0
        for i in range(n):
            if s[i] == '|':
                left_candle[i] = i
            elif i > 0:
                left_candle[i] = left_candle[i - 1]
            plates += s[i] == '*'
            prefix_sum[i + 1] = plates

        for i in range(n - 1, -1, -1):
            if s[i] == '|':
                right_candle[i] = i
            elif i < n - 1:
                right_candle[i] = right_candle[i + 1]

        # Answer the queries using the precomputed values
        answer = []
        for left, right in queries:
            # Find the nearest candles to the left and right within the range
            left_bound = right_candle[left]
            right_bound = left_candle[right]

            # Calculate the number of plates between the candles
            plates_between = prefix_sum[right_bound + 1] - prefix_sum[left_bound] if left_bound < right_bound else 0
            answer.append(plates_between)

        return answer

#The time complexity of the optimized solution for the LeetCode problem 2055 “Plates Between Candles” is O(n + q), where n is the length of the string s and q is the number of queries.
#Here’s the breakdown of the complexity:
#O(n): We iterate through the string s three times independently (once for the prefix sum array, once for the left nearest candles, and once for the right nearest candles). Each of these operations is linear with respect to the length of s.
#O(q): We then iterate through the array of queries once. For each query, we perform a constant-time operation to find the number of plates between candles using the precomputed arrays. The time for processing all queries is therefore linear with respect to the number of queries.
#Since these operations are independent, we add the complexities, resulting in a total time complexity of O(n + q). This means the execution time grows linearly with the size of the input string and the number of queries, which is efficient for large datasets.
