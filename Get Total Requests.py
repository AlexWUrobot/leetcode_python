# https://www.fastprep.io/problems/amazon-get-total-requests


from typing import List


class Solution:
    def getTotalRequests(self, server: List[int], replaced: List[int], new_id: List[int]) -> List[int]:
        results = []  # Initialize an empty list to store the results
        n = len(replaced)  # Get the number of days (length of 'replaced' list)
        count_map = {}  # Create an empty dictionary to keep track of counts

        # Populate the count_map with the initial counts for each server ID
        for id in server:
            if id in count_map:
                count_map[id] += 1
            else:
                count_map[id] = 1

        # Process each day
        for day in range(n):
            to_replace = replaced[day]  # Get the server ID to be replaced
            new_replacement = new_id[day]  # Get the new server ID

            # Update the count_map based on replacements
            if to_replace in count_map:
                count = count_map[to_replace]
                del count_map[to_replace]  # Remove the old server ID
                if new_replacement in count_map:
                    count_map[new_replacement] += count
                else:
                    count_map[new_replacement] = count

            # Calculate the total requests for the current state of count_map
            total_requests = 0
            for id, count in count_map.items():
                total_requests += id * count

            results.append(total_requests)  # Add the total requests to the results list

        return results  # Return the final results
# Time complexity : time complexity
ans = Solution()
server = [20, 10]
replaced = [10, 20]
newId = [20, 1]
print(ans.getTotalRequests(server,replaced,newId))  # [40, 2]


server = [3, 3]
replaced = [3, 1]
newId = [1, 5]
print(ans.getTotalRequests(server,replaced,newId))  #  [2, 10] 


server = [2, 5, 2]
replaced = [2, 5, 3]
newId = [3, 1, 5]
print(ans.getTotalRequests(server,replaced,newId))  #  [11, 7, 11] 
 
