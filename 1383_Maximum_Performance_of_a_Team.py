import heapq

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        # Modulo constant for the large number
        MOD = 10**9 + 7
        
        # Pair up speed and efficiency and sort by efficiency in descending order
        engineers = sorted(zip(efficiency, speed), reverse=True)
        
        # Priority queue to store the lowest speeds
        speed_heap = []
        max_perf = total_speed = 0
        
        for eff, spd in engineers:
            # If we have more than k engineers, remove the one with the lowest speed
            if len(speed_heap) == k:
                total_speed -= heapq.heappop(speed_heap)
            
            # Add the current engineer's speed to the total speed
            heapq.heappush(speed_heap, spd)
            total_speed += spd
            
            # Calculate the performance with the current engineer
            perf = total_speed * eff
            
            # Update max performance if the current one is better
            max_perf = max(max_perf, perf)
        
        # Return the maximum performance modulo 10^9 + 7
        return max_perf % MOD
