class Tree():
	def __init__(self,parent,value=None):
		self.parent = parent
		self.value = value
		self.childList = []
	def nChildren ( self ):
		return len(self.childList)
	def nthChild ( self, n ):
		return self.childList[n]








if __name__ == "__main__":
	nodes = int(input().strip())
	values = input().strip().split()
	edges = []
	for node in range(nodes):
		tmp = input().strip().split()
		edges.append( (int(tmp[0])),int(tmp[1]) )

		


