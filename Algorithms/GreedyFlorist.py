
import sys

def getMinimumCost(n, k, c):
	if n ==0 or k==0:
		return 0
	c.sort(reverse=True)
	cost = 0
	for i in range(n):
		cost += c[i] * (i//k + 1)

	return cost

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
c = list(map(int, input().strip().split(' ')))
minimumCost = getMinimumCost(n, k, c)
print(minimumCost)

