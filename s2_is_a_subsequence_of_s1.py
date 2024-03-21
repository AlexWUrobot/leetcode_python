
# https://leetcode.com/discuss/interview-question/3838938/Online-assessment-or-Amazon


# Function to check if the old password is a subsequence of the new password
def is_similar_password(old_pass, new_pass):
    # If the new password is shorter, it can't contain the old password as a subsequence
    if len(new_pass) < len(old_pass):
        return False

    # Initialize pointers for old_pass (i) and new_pass (j)
    i, j = 0, 0

    # Loop through both passwords
    while i < len(old_pass) and j < len(new_pass):
        # Calculate the difference in ASCII values of the characters
        diff = ord(old_pass[i]) - ord(new_pass[j])
        # If the characters are the same or the new character is the next cyclic character
        if 0 <= diff <= 1:
            # Move both pointers forward
            i += 1
            j += 1
        else:
            # Move pointer of new_pass forward
            j += 1

    # If we've gone through the entire old password, it's a subsequence of the new password
    return i == len(old_pass)

# Function to check a list of password pairs
def check_passwords(old_passes, new_passes):
    result = []
    # Iterate over pairs of old and new passwords
    for old_pass, new_pass in zip(old_passes, new_passes):
        # Append "YES" if the old password is a subsequence of the new password, "NO" otherwise
        result.append("YES" if is_similar_password(old_pass, new_pass) else "NO")
    return result

# Example usage:
old_passes = ["abdbc", "ach", "abb"]
new_passes = ["baacbab", "accdb", "baacba"]
# The output should be ['YES', 'NO', 'YES'], indicating the similarity results for each pair
print(check_passwords(old_passes, new_passes))


#The time complexity of the check_passwords function, which includes the is_similar_password function, is O(n * m), where n is the number of password pairs, and m is the length of the longest new password in the list.

#Here’s the breakdown:

#The is_similar_password function has a while loop that runs at most m times, where m is the length of the new password.
#The check_passwords function calls is_similar_password for each of the n password pairs.
#Therefore, in the worst case, where each new password is checked against an old password of similar length, the function will perform n iterations of the is_similar_password function, each taking m steps, resulting in an overall time complexity of O(n * m).
