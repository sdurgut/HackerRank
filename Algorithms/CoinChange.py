def count(N, coins):
	numWays = [[1] + N * [0] for j in range(len(coins) + 1)]
	# print (numWays)
	for i in range(1, len(coins) + 1):
		for j in range(1, N + 1):
			numWays[i][j] = numWays[i-1][j] + (numWays[i][j - coins[i-1]] if coins[i-1] <= j else 0)
			print (numWays)
	return numWays[-1][-1]

if __name__ == "__main__":
	N= int(input().strip().split()[0])
	s = input().split()
	coins = [int(i) for i in s]
	print (count(N, coins))