class Node:
	def __init__(self, label=None, data=None):
		self.label = label
		self.data = data
		self.children = dict()

	def addChild(self, key,data=None):
		if not isinstance(kwey, Node):
			self.childer[key] = Node(key,data)
		else:
			
