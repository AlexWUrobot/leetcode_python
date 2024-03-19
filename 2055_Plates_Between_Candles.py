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
