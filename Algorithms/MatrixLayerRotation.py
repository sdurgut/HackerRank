def getCircles(myMatrix):
	M = len(myMatrix)
	N = len(myMatrix[0])
	i= M-1
	j=N-1
	circles = []
	while i>1 and j>1:
		circles.append((i,j))
		i -=2
		j -=2
	return circles

def rotate(myMatrix,R):
	nCircles = getCircles(myMatrix)

def main():
	inp = input().strip().split(" ")
	M = inp[int(0)]
	N = inp[int(1)]
	R = inp[int(2)]
	myMatrix = []
	for i in range(M):
		myMatrix.append( input().strip().split(" ") )

	rotate(myMatrix,R)

if __name__ == "__main__":
	main()