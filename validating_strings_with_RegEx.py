#!/bin/python3

from os import environ
from re import compile
from re import match

#
# Write the regular expression in the blank space below
#


regularExpression = r'^(a.*a|b.*b|a|b)$'

pattern = compile(regularExpression)

query = int(input())
result = ['False'] * query

for i in range(query):
    someString = input()
    
    if pattern.match(someString):
        result[i] = 'True'

with open(environ['OUTPUT_PATH'], 'w') as fileOut:
    fileOut.write('\n'.join(result))



#^: This asserts the start of a line. It means that the pattern must match from the beginning of the string.
#(a.*a|b.*b|a|b): This is the main part of the pattern, enclosed in parentheses to group the alternatives. It contains four options separated by the pipe |, which means “or”:
#a.*a: This matches any string that starts with an ‘a’, followed by zero or more (*) of any character (.), and ends with an ‘a’.
#b.*b: Similar to the first, this matches any string that starts with a ‘b’, followed by zero or more of any character, and ends with a ‘b’.
#a: This matches a single character ‘a’. It’s necessary to include this because the previous expressions require at least two characters to match.
#b: This matches a single character ‘b’, included for the same reason as the single ‘a’.
#$: This asserts the end of a line. It ensures that the pattern must match up to the end of the string.
#The combination of ^ and $ ensures that the entire string must conform to the pattern, not just a substring. The pattern will match strings that start and end with the same letter (‘a’ or ‘b’), including strings that are just a single character long.
