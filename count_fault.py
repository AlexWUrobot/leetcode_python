# https://www.fastprep.io/problems/amazon-count-faults

def countFaults(n, logs):
    # Initialize a dictionary to keep track of server errors
    error_counts = {f's{i}': 0 for i in range(1, n+1)}
    replacements = 0

    # Iterate through the logs
    for log in logs:
        server_id, status = log.split()

        # Reset the error count for successes, increment for errors
        if status == 'success':
            error_counts[server_id] = 0
        else:
            error_counts[server_id] += 1

            # If a server has 3 consecutive errors, replace it
            if error_counts[server_id] == 3:
                replacements += 1
                error_counts[server_id] = 0

    return replacements

# Example usage:
n = 2
logs = ["s1 error", "s1 error", "s2 error", "s1 error", "s1 error", "s2 success"]
print(countFaults(n, logs))  # Output: 1
