def findShortestPath(list):
	robot1Pos = list[0][0]
	robot2Pos = list[1][0]
	distbyRobot1 = abs(list[0][0]-list[0][1])
	distbyRobot2 = abs(list[1][0]-list[1][1])
	robot1Pos = list[0][1]
	robot2Pos = list[1][1]
	del list[0]
	del list[0]
	idx = 0
	while idx < len(list):
		


nTestCase = 3
QueryInput = [[5, 4],[1, 5], [3, 2],[4, 1],[2, 4],[4, 2],[1, 2],[4, 3],[10, 3],[2, 4],[5, 4],[9, 8]]
robot1Pos = -1
robot2Pos = -1

nQuerry = -1
nContainers = -1
tmpQueryList = []
while QueryInput:
	nContainers = QueryInput[0][0]
	nQuerry = QueryInput[0][1]
	del QueryInput[0]
	idx = 0
	while idx < nQuerry:
		tmpQueryList.append(QueryInput[0])
		del QueryInput[0]
		idx = idx + 1
	print tmpQueryList
	tmpQueryList = []

