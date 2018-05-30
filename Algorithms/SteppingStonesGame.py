# https://www.hackerrank.com/challenges/stepping-stones-game

import math

def isTriangular(x):
	n = (math.sqrt(8 * x + 1) - 1) / 2
	if int(n) == n:
		return int(n)
	return -1

if __name__ == "__main__":
	T = int(input().strip())
	for i in range(T):
		N = int(input().strip())
		steps = isTriangular(N)
		print ('Go On Bob %i' % steps if steps > -1 else 'Better Luck Next Time')