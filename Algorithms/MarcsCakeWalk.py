#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marcsCakewalk function below.
def marcsCakewalk(calorie):
	sortedCal = sorted(calorie, reverse=True)
	minimumWalk = 0
	for i in range(len(sortedCal)):
		minimumWalk += sortedCal[i]*2**(i)
	return minimumWalk

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    calorie = list(map(int, input().rstrip().split()))

    result = marcsCakewalk(calorie)

    fptr.write(str(result) + '\n')

    fptr.close()
