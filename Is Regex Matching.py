
# https://leetcode.com/discuss/interview-question/5358811/amazon-oa

######################################### Approach 1
import re

def isRegexMatching(regex, arr):
    result = []
    for string in arr:
        pattern = re.compile(regex)
        if pattern.fullmatch(string):
            result.append("YES")
        else:
            result.append("NO")
    return result


################################################# Approach 2

def match_paranthesis(i, j, width, regex, string):
    if i + width - 1 > len(string):
        return False
    for k in range(width):
        if regex[j + k + 1] != '.' and regex[j + k + 1] != string[i + k]:
            return False
    return True

def get_width(regex, start):
    i = start
    while regex[i] != ')':
        i += 1
    return i - start

def dfs(i, j, regex, string):
    if i >= len(string) and j >= len(regex):
        return True
    if j >= len(regex):
        return False

    if regex[j] != '(':
        is_match = i < len(string) and (string[i] == regex[j] or regex[j] == '.')
        
        if j + 1 < len(regex) and regex[j + 1] == '*':
            return dfs(i, j + 2, regex, string) or (is_match and dfs(i + 1, j, regex, string))
        
        if is_match:
            return dfs(i + 1, j + 1, regex, string)
        
    else:
        width = get_width(regex, j + 1)
        if width != 0:
            is_paranthesis_expression_match = match_paranthesis(i, j, width, regex, string)
            
            if is_paranthesis_expression_match and (dfs(i + width, j, regex, string) or dfs(i + width, j + width + 3, regex, string)):
                return True
        else:
            return dfs(i, j + 3, regex, string)
    
    return False

def is_regex_matching(regex, arr):
    ret_arr = []
    for string in arr:
        if dfs(0, 0, regex, string):
            ret_arr.append("YES")
        else:
            ret_arr.append("NO")
    return ret_arr



regex = "ab(e.r)*e"
arr = ["abbeere", "abefretre"]
print(isRegexMatching(regex, arr))


regex = "..()*e*"
arr = ["code", "abeee", "cd"]
print(isRegexMatching(regex, arr))


regex = "ab(e.r)*e"
arr = ["abbeere", "abefretre"]
print(is_regex_matching(regex, arr))


regex = "..()*e*"
arr = ["code", "abeee", "cd"]
print(is_regex_matching(regex, arr))
 
