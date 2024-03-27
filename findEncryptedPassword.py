
# https://www.fastprep.io/problems/amazon-find-encrypted-password

def findEncryptedPassword(password):
    # Since the input is always a palindrome, we only need to sort the first half of the string
    half = len(password) // 2
    # Sort the first half and keep the second half as it is because it's a palindrome
    smallest_half = ''.join(sorted(password[:half]))
    # If the length of the password is odd, include the middle character
    middle = password[half] if len(password) % 2 != 0 else ''
    # The second half is a reverse of the first half for it to remain a palindrome
    encrypted_password = smallest_half + middle + smallest_half[::-1]
    return encrypted_password

# Example usage:
print(findEncryptedPassword("babab"))  # Output: "abbba"
print(findEncryptedPassword("yxxy"))   # Output: "xyyx"
