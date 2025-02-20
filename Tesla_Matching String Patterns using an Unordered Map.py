#
# Q1: Matching String Patterns using an Unordered Map (Dictionary)
# Why do we need reverse_mapping?
# The mapping dictionary ensures that each character in str1 maps uniquely to a character in str2.
# However, we also need to ensure that no two different characters in str1 map to the same character in str2.
# This is where reverse_mapping helps: It ensures that each character in str2 is assigned to only one character from str1, preventing multiple mappings to the same character.
#


def match_pattern(str1: str, str2: str) -> bool:
    # If lengths of the strings don't match, they can't have a one-to-one mapping
    if len(str1) != len(str2):
        return False

    mapping = {}  # Maps characters from str1 to str2
    reverse_mapping = {}  # Ensures that no two str1 characters map to the same str2 character

    for ch1, ch2 in zip(str1, str2):
        # If ch1 is already mapped, it must always map to the same ch2
        if ch1 in mapping and mapping[ch1] != ch2:
            return False
        # If ch2 is already mapped to a different ch1, mapping is invalid
        if ch2 in reverse_mapping and reverse_mapping[ch2] != ch1:
            return False

        # Establish bidirectional mapping
        mapping[ch1] = ch2
        reverse_mapping[ch2] = ch1  # Prevents multiple characters from mapping to the same value

    return True

# Test cases
print(match_pattern("abb", "cdd"))  # True
print(match_pattern("aba", "cde"))  # False (because 'a' maps to both 'c' and 'e')
print(match_pattern("foo", "bar"))  # False (because 'o' would map to two different letters)
print(match_pattern("paper", "title"))  # True (consistent mapping)

# Time Complexity: O(N)
# Space Complexity: O(N)

