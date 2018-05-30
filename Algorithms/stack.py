class Stack:
	def __init__(self):
		self.items = []
	def isEmpty(self):
		return self.items == []
	def push(self,item):
		self.items.append(item)
	def pop(self,item):
		return self.items.pop()
	def peek(self):
		return self.items[len(self.items-1)]
	def size(self):
		return len(self.items)


stack = Stack()

stack.push(5)
stack.push(51)
stack.push(52)
stack.push(53)
stack.push(54)
print(stack.isEmpty())
print(stack.size())
