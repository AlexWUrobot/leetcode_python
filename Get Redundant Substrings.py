# https://www.fastprep.io/problems/amazon-get-redundant-substrings


def generate_all_substring(word):
    # Generate all substrings
    n = len(word)
    all_substring = []
    for i in range(n):
        for j in range(i, n):
            all_substring.append(word[i:j+1])
    print(all_substring)
    return all_substring
            

def count_vowels_and_consonants(input_string):
    # Convert the input string to lowercase for case-insensitive matching
    input_string = input_string.lower()

    # Initialize counters for vowels and consonants
    vowel_count = 0
    consonant_count = 0

    # Define the set of vowels
    vowels = {'a', 'e', 'i', 'o', 'u'}

    # Iterate through each character in the input string
    for char in input_string:
        if char.isalpha():  # Check if the character is an alphabet
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    return vowel_count, consonant_count
    

def redundant_substrings(word,a,b):
    count_redundant = 0
    all_substrings = generate_all_substring(word)
    for substring in all_substrings:
        vowel_count, consonant_count = count_vowels_and_consonants(substring)
        if len(substring) == a*vowel_count+b*consonant_count:
            count_redundant+=1
    return count_redundant
        

word = "abbacc"
a = -1
b = 2
print(redundant_substrings(word, a, b))


word = "akljfs"
a = -2
b = 1
print(redundant_substrings(word, a, b))
