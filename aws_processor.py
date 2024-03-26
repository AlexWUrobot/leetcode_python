
# https://fastprep.gitbook.io/amazon-2024-oa/2023-june-aug/aws-processors

import math

def execute_processes(execution):
    total_time = 0
    for i in range(len(execution)):
        # Execute the current process
        total_time += execution[i]
        
        # Update the execution times of cohesive processes
        for j in range(i+1, len(execution)):
            if execution[j] == execution[i]:
                execution[j] = math.ceil(execution[i] / 2)
        print('execution:', i, execution, total_time)
                
    return total_time

# Example usage:
execution_times = [5, 5, 3, 6, 5, 3]
total_execution_time = execute_processes(execution_times)
print(f"Total execution time: {total_execution_time}")
