#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    if len(arr) == 0:
        return []
    s = dict()

    min_num = min(arr)
    max_num = max(arr)
    for i in range(len(arr)):
        if arr[i] in s:
            s[arr[i]] += 1
        else:
            s[arr[i]] = 1
    arr = []

    for i in range(int(min_num), int(max_num)+1):
        if i in s:
            for k in range(s[i]):
                arr.append(i)
    return arr


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
