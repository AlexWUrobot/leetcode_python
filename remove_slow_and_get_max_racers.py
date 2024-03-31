# https://www.fastprep.io/problems/amazon-get-max-racers
def maximize_speed_sequence(speed, k):
    # Step 1: Find all unique numbers in the speed list
    unique_numbers = set(speed)

    # Step 2: Initialize the answer
    max_length = 0
    best_sequence = []

    # Step 3: Try removing k numbers for each unique number
    for target in unique_numbers:
        # Create a temporary list to simulate removal of elements
        temp_speed = speed.copy()

        # Remove k elements that are not equal to the target
        count = 0
        for i in range(len(temp_speed)):
            if temp_speed[i] != target and count < k:
                temp_speed[i] = None
                count += 1

        # Filter out None values which represent removed elements
        temp_speed = list(filter(None, temp_speed))

        # Find the longest subsequence of target
        current_length = 0
        for num in temp_speed:
            if num == target:
                current_length += 1
            else:
                current_length = 0

            # Update max_length and best_sequence if current is longer
            if current_length > max_length:
                max_length = current_length
                best_sequence = temp_speed

    return best_sequence

# Example usage:
speed = [4, 4, 3, 3, 4, 3, 3, 4]
k = 2
result = maximize_speed_sequence(speed, k)
print("Output speed:", result)
