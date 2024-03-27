# https://algo.monster/problems/amazon-oa-max-subjects-number
# https://www.fastprep.io/problems/amazon-find-maximum-num

# Overall, the dominant time complexity comes from the sorting step, so the total time complexity of the solution is O(n log n).
def max_subjects_passed(answered, needed, q):
    n = len(answered)
    # Calculate the additional answers needed for each subject
    additional_needed = [max(0, needed[i] - answered[i]) for i in range(n)]
    # Sort subjects by additional needed answers
    sorted_subjects = sorted(range(n), key=lambda i: additional_needed[i])

    subjects_passed = 0
    subjects_passed_indices = []  # List to store indices of subjects passed
    for i in sorted_subjects:
        # Distribute available extra answers to pass subjects
        if q >= additional_needed[i]:
            q -= additional_needed[i]
            subjects_passed += 1
            subjects_passed_indices.append(i)
        else:
            break

    return subjects_passed, subjects_passed_indices

# Example usage:
answered = [24, 27, 0]
needed = [51, 52, 100]
q = 100
num_passed, passed_indices = max_subjects_passed(answered, needed, q)
print("Output for Example 1:")
print("Maximum subjects passed:", num_passed)  
print("Subjects chosen:", passed_indices)  

answered = [2, 4]
needed = [4, 5]
q = 1
num_passed, passed_indices = max_subjects_passed(answered, needed, q)
print("\nOutput for Example 2:")
print("Maximum subjects passed:", num_passed)
print("Subjects chosen:", passed_indices)
