# https://leetcode.com/discuss/interview-question/1955152/amazon-online-assessment-demo

def find_users_with_excessive_transactions(logs, threshold):
    # Initialize a dictionary to keep track of the transaction counts
    transaction_counts = {}
    
    # Iterate over each log entry
    for log in logs:
        # Split the log entry into its components
        sender, receiver, _ = log.split()
        
        # Update the transaction count for the sender
        if sender not in transaction_counts:
            transaction_counts[sender] = 0
        transaction_counts[sender] += 1
        
        # Update the transaction count for the receiver if it's a different user
        if sender != receiver:
            if receiver not in transaction_counts:
                transaction_counts[receiver] = 0
            transaction_counts[receiver] += 1
    
    # Find users with a transaction count greater than or equal to the threshold
    users_over_threshold = [user for user, count in transaction_counts.items() if count >= threshold]
    
    # Return the list of users sorted in ascending order by their user ID
    return sorted(users_over_threshold, key=int)

# Example usage:
logs = ["88 99 200", "88 99 300", "99 32 100", "12 12 15"]
threshold = 2
print(find_users_with_excessive_transactions(logs, threshold))


The time complexity of the function find_users_with_excessive_transactions is O(n log n). Here’s the breakdown:

#O(n): We iterate over each log entry once, where n is the number of logs. The operations within the loop are constant time operations, except for the split function, which is also O(n) in the size of the log entry, but since the log entry size is fixed and small, it can be considered O(1).
#O(n log n): The final step is to sort the users who meet the threshold. The sorting is done based on the numeric value of the user IDs, which is an integer sort. Python’s sort function uses Timsort, which has a worst-case time complexity of O(n log n).
#Therefore, the most time-consuming operation is the sorting step, which gives us the overall time complexity of O(n log n). The space complexity is O(u), where u is the number of unique users, because we store each user’s transaction count in a dictionary.
