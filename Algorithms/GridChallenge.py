#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gridChallenge function below.
# Complete the gridChallenge function below.
def gridChallenge(grid):
	# print(grid)
	if len(grid) < 2: return "YES"

	for i in range(len(grid)):
		grid[i] = sorted(grid[i])

	# print(grid)

	for i in range(len(grid)-1):
		for j in range(len(grid)):
			# get ascii value vith ord()
			# print(grid[i][j],grid[i+1][j])
			if ord(grid[i][j])>ord(grid[i+1][j]):
				return "NO"

	return "YES"


if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	t = int(input())

	for t_itr in range(t):
		n = int(input())

		grid = []

		for _ in range(n):
			grid_item = input()
			grid.append(grid_item)

		result = gridChallenge(grid)

		fptr.write(result + '\n')

	fptr.close()
