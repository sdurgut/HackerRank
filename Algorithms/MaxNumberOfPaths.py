arr = [[1,2,3,4],[4,5,6,7],[1,4,6,8]]

def numWays(arr):
	nrows = len(arr)
	ncols = len(arr[0])
	ways  = [[0 for i in range(nrows)] for j in range(ncols)]
	for i in range(nrows):
		ways[0][i] = 1
	for i in range(ncols):
		ways[i][0] = 1
	for i in range(1,ncols):
		for j in range(1,nrows):
			ways[i][j] = ways[i-1][j] + ways[i][j-1] 
	print(ways)
	return ways[ncols-1][nrows-1]


print(numWays(arr))