
# https://leetcode.com/discuss/interview-question/2299560/Amazon-SDE-or-Online-Assessment-(OA)-or-July-2022

class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        # The length of the security array.
        n = len(security)

        # dec[i] will hold the count of consecutive days before day 'i'
        # where the security value has been non-increasing.
        dec = [0] * n

        # inc[i] will hold the count of consecutive days after day 'i'
        # where the security value has been non-decreasing.
        inc = [0] * n

        # Calculate the non-increasing streaks of security values.
        for i in range(1, n):
            if security[i - 1] >= security[i]:
                dec[i] = dec[i - 1] + 1

        # Calculate the non-decreasing streaks of security values.
        for i in range(n - 2, -1, -1):
            if security[i] <= security[i + 1]:
                inc[i] = inc[i + 1] + 1

        # Return the list of days where the number of non-increasing days before 'i'
        # and the number of non-decreasing days after 'i' are both at least 'time'.
        return [i for i, (a, b) in enumerate(zip(dec, inc))
                if a >= time and b >= time]
