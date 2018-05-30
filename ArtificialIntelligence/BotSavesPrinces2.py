
#!/usr/bin/python

# https://www.hackerrank.com/challenges/saveprincess2?hr_b=1


def getMoves(dx,dy):
	moves = []
	if dx<0:
		# for i in range(abs(dx)):
		moves.append("RIGHT")
	if dx>0:
		# for i in range(abs(dx)):
		moves.append("LEFT")
	if dy<0:
		# for i in range(abs(dy)):
		moves.append("DOWN")
	if dy>0:
		# for i in range(abs(dy)):
		moves.append("UP")
	return moves



def nextMove(n,r,c,grid):
	botLocation  = []
	princesLocation = []
	for i in range(len(grid)):
		if 'm' in grid[i]:
			botLocation.append(i)
			botLocation.append( grid[i].index('m') )
		if 'p' in grid[i]:
			princesLocation.append(i)
			princesLocation.append( grid[i].index('p') )


	
	dy = botLocation[0] - princesLocation[0]
	dx = botLocation[1] - princesLocation[1]
	# print ("bot location = ", botLocation)
	# print ("princes location = ", princesLocation)
	# print ("dx,dy =", dx,dy)
	moves = getMoves(dx,dy)
	print(moves[0])
	# for move in moves:
	# 	print (move)


def main():
	n = int(input())
	r,c = [int(i) for i in input().strip().split()]
	grid = []
	for i in range(0, n):
		grid.append(input())
	
	nextMove(n,r,c,grid)


if __name__ == '__main__':
	main()