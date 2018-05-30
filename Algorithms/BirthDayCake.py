#!/bin/python3
# https://www.hackerrank.com/challenges/birthday-cake-candles/problem

import sys
from collections import defaultdict

def birthdayCakeCandles(n, ar):
	freqs = defaultdict(int)
	for candle in ar:
		freqs[candle] += 1
	sortedFreqs = sorted(freqs.items(), key=lambda x: x[1])
	print (sortedFreqs[-1][1])

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
birthdayCakeCandles(n, ar)
