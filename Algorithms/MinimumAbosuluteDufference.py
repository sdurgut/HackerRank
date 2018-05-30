#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(n, arr):
	sortedArr = sorted(arr)
	minimumDiff = sys.maxsize
	for i in range(n-1):
		if abs(sortedArr[i]-sortedArr[i+1])<minimumDiff:
			minimumDiff = abs(sortedArr[i]-sortedArr[i+1])
	return minimumDiff

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
