
#https://www.fastprep.io/problems/max-lucky-numbers

def get_max_lucky_number(x, y, n):
    def dfs(num, total):
        nonlocal max_lucky
        if total > n:
            return
        if total == n:
            max_lucky = max(max_lucky, num)  # Update the maximum lucky number

        dfs(num * 10 + x, total + x)  # Explore using digit 'x'
        dfs(num * 10 + y, total + y)  # Explore using digit 'y'

    max_lucky = 0  # Initialize the maximum lucky number
    dfs(0, 0)  # Start the depth-first search
    return max_lucky  # Return the final result
    


print(get_max_lucky_number(3, 4, 13))
print(get_max_lucky_number(2, 5, 6))
