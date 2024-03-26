# https://fastprep.gitbook.io/amazon-2024-oa/2023-june-aug/amazon-review-score
def longest_substring_without_prohibited_words(review, prohibitedWords):
    # Initialize the maximum length of valid substring found
    max_length = 0
    # Start index for searching the review string
    start = 0

    # Loop through the review string to find valid substrings
    while start < len(review):
        # Assume the substring starting at 'start' is valid
        valid = True
        # Check each prohibited word
        for word in prohibitedWords:
            # Find the position of the prohibited word in the review string
            end = review.find(word, start)
            # If a prohibited word is found
            if end != -1:
                # Update the maximum length if the current valid substring is longer
                max_length = max(max_length, end - start)
                # Move the start index past the prohibited word
                start = end + len(word)
                # Mark the substring as invalid and break to search for a new substring
                valid = False
                break
        # If no prohibited word is found, the rest of the string is valid
        if valid:
            # Update the maximum length for the remaining valid substring
            max_length = max(max_length, len(review) - start)
            # Break the loop as the longest valid substring is found
            break
    # Return the length of the longest valid substring found
    return max_length

# Example usage:
review = "GoodProductButScrapAfterWash"
prohibitedWords = ["crap", "odpro"]
# Call the function and print the result
print(longest_substring_without_prohibited_words(review, prohibitedWords))
