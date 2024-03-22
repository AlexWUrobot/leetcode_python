#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'groupSort' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#
from collections import Counter

def groupSort(arr):
    # Write your code here

    # Initialize a dictionary to store frequency of each number
    freq_map = {}
    for num in arr:
        freq_map[num] = freq_map.get(num, 0) + 1
    
    # Convert the frequency map to a list of tuples and sort
    sorted_items = sorted(freq_map.items(), key=lambda x: (-x[1], x[0]))
    return sorted_items
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = groupSort(arr)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
