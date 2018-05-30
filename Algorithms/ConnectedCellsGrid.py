
def findLargestCluster(matrix):
	


m = int(input().strip()) # rows
n= int(input().strip()) # cols
matrix = []
for i in range(m):
	line = list(input().strip())
	matrix.append(line)

print ( findLargestCluster(matrix) )