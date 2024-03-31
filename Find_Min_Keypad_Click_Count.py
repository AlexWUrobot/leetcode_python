
# https://www.fastprep.io/problems/amazon-find-minimum-keypad-click-count

def calculate_clicks(text, keypad):
    # Create a dictionary to map each letter to its click count
    letter_to_clicks = {}
    for button, letters in enumerate(keypad, start=1):
        for i, letter in enumerate(letters, start=1):
            letter_to_clicks[letter] = i

    # Calculate the total number of clicks for the text
    total_clicks = sum(letter_to_clicks[letter] for letter in text if letter in letter_to_clicks)
    return total_clicks

# Define the left and right keypad mappings
left_keypad = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz']
right_keypad = ['ajs', 'bot', 'cpu', 'dkv', 'hmz', 'gl', 'enw', 'fqx', 'iry']

# Input string
letters = "abacadefghibj"

# Calculate clicks for both keypads
left_clicks = calculate_clicks(letters, left_keypad)
right_clicks = calculate_clicks(letters, right_keypad)

print(f"Left Keypad Clicks: {left_clicks}")
print(f"Right Keypad Clicks: {right_clicks}")
