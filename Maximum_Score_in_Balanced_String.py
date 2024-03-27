# https://www.fastprep.io/problems/maximum-score-in-balanced-string

def max_score(s):
    stack = []
    score = 0

    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        elif char == ')' and stack:
            print("stack:",stack)
            temp = i - stack.pop()
            print("------score:", temp)
            score = score + temp

    return score

# Example usage:
s1 = "(())"
print(f"Input: s = '{s1}'")
print("Output:", max_score(s1))

s2 = "()"
print(f"Input: s = '{s2}'")
print("Output:", max_score(s2))


s1 = "((()))"
print(f"Input: s = '{s1}'")
print("Output:", max_score(s1))
