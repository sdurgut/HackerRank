
import sys

def gridSearch(G,P):
	nCol_P = len(P)
	nRow_P = len(P[0])
	for i in range(len(G)-nCol_P+1):
		if P[0] not in G[i]:
			continue
		for j in range( len(G[0])-nRow_P +1):
			tmpArr= []
			for x in  G[i:i+nCol_P]:
				tmpArr.append(x[j:j+nRow_P])
			if tmpArr == P:
				return "YES"
	return "NO"




t = int(input().strip()) # T number of test cases
for a0 in range(t):
	R,C = input().strip().split(' ') # nRows, nCols
	R,C = [int(R),int(C)]
	G = [] # fill the grid
	G_i = 0
	for G_i in range(R): 
		G_t = str(input().strip())
		G.append(G_t)
	r,c = input().strip().split(' ') #nrows ncols for pattern P
	r,c = [int(r),int(c)]
	P = []
	P_i = 0
	for P_i in range(r):
		P_t = str(input().strip())
		P.append(P_t)

	print (gridSearch(G,P))

