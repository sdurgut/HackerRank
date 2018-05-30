
#!/usr/bin/python

# https://www.hackerrank.com/challenges/saveprincess/problem

def getMoves(dx,dy):
	moves = []
	if dx<0:
		for i in range(abs(dx)):
			moves.append("RIGHT")
	if dx>0:
		for i in range(abs(dx)):
			moves.append("LEFT")
	if dy<0:
		for i in range(abs(dy)):
			moves.append("DOWN")
	if dy>0:
		for i in range(abs(dy)):
			moves.append("UP")
	return moves



def displayPathtoPrincess(n,grid):
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
	for move in moves:
		print (move)


def main():
	m = int(input())
	grid = [] 
	for i in range(0, m): 
		grid.append(input().strip())

	displayPathtoPrincess(m,grid)


if __name__ == '__main__':
	main()