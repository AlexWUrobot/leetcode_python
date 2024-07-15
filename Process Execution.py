
# https://www.fastprep.io/problems/amazon-process-execution

def processExecution(power, minPower, maxPower):
    # Initialize an empty result list
    result = []

    # Iterate over each processor
    for i in range(len(minPower)):
        # Initialize counters for number of processes and total power
        num_processes = 0
        total_power = 0

        # Iterate over each process
        for j in range(len(power)):
            # Check if the process power lies within the processor range
            if minPower[i] <= power[j] <= maxPower[i]:
                num_processes += 1
                total_power += power[j]

        # Append the results for the current processor to the result list
        result.append([num_processes, total_power])

    return result

# Example input
power = [7, 6, 8, 10]
minPower = [6, 3, 4]
maxPower = [10, 7, 9]

# Call the function and print the output
print(processExecution(power, minPower, maxPower))


# Example input
power = [11, 11, 11]
minPower = [8, 13]
maxPower = [11, 100]

# Call the function and print the output
print(processExecution(power, minPower, maxPower))

# time complexity O(n * m)
