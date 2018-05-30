#!/bin/python3

import sys

def bigSorting(arr):
	arr.sort(key=int) # faster method
	return arr

if __name__ == "__main__":
	n = int(input().strip())
	arr = []
	arr_i = 0
	for arr_i in range(n):
		arr_t = str(input().strip())
		arr.append(arr_t)
	result = bigSorting(arr)
	print ("\n".join(map(str, result)))


