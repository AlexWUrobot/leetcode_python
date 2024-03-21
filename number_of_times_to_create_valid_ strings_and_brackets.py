def fun(ind, st, s):
    # base case
    if ind >= len(s):
        return 1 if not st else 0

    # when we have an opening bracket straight
    if s[ind] == '(' or s[ind] == '[':
        st.append(s[ind])
        return fun(ind + 1, st, s)

    # when we have a closing bracket straight
    elif s[ind] == ')' or s[ind] == ']':
        # cases where we have to return false
        if not st or (s[ind] == ')' and st[-1] == '[') or (s[ind] == ']' and st[-1] == '('):
            return 0
        st.pop()
        return fun(ind + 1, st, s)

    # when we have '?' char in string s
    ways = 0
    for char in ['(', ')', '[', ']']:
        s = s[:ind] + char + s[ind + 1:]
        ways += fun(ind, st[:], s)
    return ways

def solve(s):
    st = []
    return fun(0, st, s)

# Example usage:
#n = int(input("Enter the number of test cases: "))
#for _ in range(n):
s = "([])?"
print(solve(s))
