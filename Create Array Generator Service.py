#https://www.fastprep.io/problems/amazon-create-array-generator-service


def generate_largest_sequence(arr, state, m):
    S = []  # Initialize the sequence S

    # Perform m operations
    for _ in range(m):
        available_indices = [i for i, s in enumerate(state) if s == '1']
        
        print("available_indices:", available_indices)
        max_value = max(arr[i] for i in available_indices)
        S.append(max_value)

        # Update state
        original_state = state[:]# name a new one cancel mutable 
        for i in range(len(state)):
            if original_state[i] == '0' and i > 0 and original_state[i-1] == '1':  #change "10" to "11"
                state = state[:i] + '1' + state[i+1:]

    return S

# Example usage
arr = [5, 3, 4, 6]
state = "1100"
m = 5
result = generate_largest_sequence(arr, state, m)
print(result)  # Correct output: [5, 5, 6, 6, 6]


# Example usage
arr = [10, 5, 7, 6]
state = "0101"
m = 2
result = generate_largest_sequence(arr, state, m)
print(result)  # Correct output: [5, 5, 6, 6, 6]
