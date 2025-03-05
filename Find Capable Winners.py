# O(n) solution
# If one can win over all others, that means it can always use the largest two power boosts to defeat other's smallest two power boosts. That's their best strategy, if that cannot work, they cannot defeat all others. In order to have that strategy works, the largest power boost should at least be larger than other's second large power boost and the second large power boost should at least be larger than other's smallest power boost.
# So the question becomes how many of them has largest power boost larger than the max of others' second large power boost and second largest power boost larger than the max of other's smallest power boost.

from typing import List

class Solution:
    def findCapableWinners(self, power_a: List[int], power_b: List[int], power_c: List[int]) -> int:
        """
        Determines the number of capable winners based on the given conditions:
        - The largest value in each triplet must defeat all second-largest values.
        - The second-largest value must defeat all third-largest values.

        :param power_a: List of first power values.
        :param power_b: List of second power values.
        :param power_c: List of third power values.
        :return: The number of capable winners.
        """
        res = 0  # Counter for capable winners
        l1 = []  # List to store the smallest values in each triplet
        l2 = []  # List to store the second-largest values in each triplet
        l3 = []  # List to store the largest values in each triplet
        max1 = 0  # Tracks the maximum value among the smallest elements (l1)
        max2 = 0  # Tracks the maximum value among the second-largest elements (l2)

        # Process each triplet and sort the values
        for i in range(len(power_a)):
            x1, x2, x3 = power_a[i], power_b[i], power_c[i]

            # Ensure x1 is the smallest, x2 is the second-largest, and x3 is the largest
            if x1 > x2:
                x1, x2 = x2, x1
            if x1 > x3:
                x1, x3 = x3, x1
            if x2 > x3:
                x2, x3 = x3, x2

            # Store the sorted values in respective lists
            l1.append(x1)
            l2.append(x2)
            l3.append(x3)

            # Update max1 (largest among all l1 values) and max2 (largest among all l2 values)
            max1 = max(max1, x1)
            max2 = max(max2, x2)

        # Check conditions to determine capable winners
        for i in range(len(power_a)):
            # A triplet is considered a "capable winner" if:
            # - The largest element (l3[i]) is greater than the max of all second-largest values (max2)
            # - The second-largest element (l2[i]) is greater than the max of all smallest values (max1)
            if l3[i] > max2 and l2[i] > max1:
                res += 1

        return res  # Return the total number of capable winners

# Example usage
power_a = [9, 4, 2]
power_b = [5, 12, 10]
power_c = [11, 3, 13]
sol = Solution()
print(sol.findCapableWinners(power_a, power_b, power_c))  # Output: 1
