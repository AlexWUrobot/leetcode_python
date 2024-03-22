# Define the fizzBuzz function that takes an integer n as input
def fizzBuzz(n):
    # Loop through each number from 1 to n
    for i in range(1, n+1):
        # Check if the number is divisible by both 3 and 5
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")  # If so, print 'FizzBuzz'
        # Check if the number is divisible by 3
        elif i % 3 == 0:
            print("Fizz")  # If so, print 'Fizz'
        # Check if the number is divisible by 5
        elif i % 5 == 0:
            print("Buzz")  # If so, print 'Buzz'
        else:
            print(i)  # If none of the above, print the number itself

# Example usage:
# Prompt the user to enter a number and store it in the variable n
n = int(input("Enter a number: "))
# Call the fizzBuzz function with the user-provided number
fizzBuzz(n)
