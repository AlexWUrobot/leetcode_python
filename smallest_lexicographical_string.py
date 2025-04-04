def solution(word):
    # Initialize the result with the original word
    smallest = word

    # Length of the input word
    n = len(word)

    # Try all possible prefix reversals
    for k in range(1, n + 1):
        # Reverse the first k characters: word[:k][::-1]
        # Append the rest unchanged: word[k:]
        reversed_prefix = word[:k][::-1] + word[k:]
        # Update the smallest string if the new one is lexicographically smaller
        if reversed_prefix < smallest:
            smallest = reversed_prefix

    # Try all possible suffix reversals
    for k in range(1, n + 1):
        # Keep the first part unchanged: word[:-k]
        # Reverse the last k characters: word[-k:][::-1]
        reversed_suffix = word[:-k] + word[-k:][::-1]
        # Update the smallest string if the new one is lexicographically smaller
        if reversed_suffix < smallest:
            smallest = reversed_suffix

    # Return the alphabetically smallest result
    return smallest
print(solution("dbaca"))  # Output: "abdca"
