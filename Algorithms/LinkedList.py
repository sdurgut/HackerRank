# follow the tutorial at http://interactivepython.org/runestone/static/pythonds/BasicDS/ImplementinganUnorderedListLinkedLists.html

class Node:
	def __init__(self,initdata):
		self.data = initdata
		self.next = None

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def setData(self, newData):
		self.data = newData

	def setNext(self,newNext):
		self.next = newNext

class LinkedList:
	def __init__(self):
		self.head = None
	
	def isEmpty(self):
		return self.head == None
	
	def addHead(self,item):
		temp = Node(item)
		temp.setNext(self.head)
		self.head = temp

	def size(self):
		current = self.head
		count = 0
		while current != None:
			count = count + 1
			current = current.getNext()
		return count
	
	def search(self,item):
		current = self.head
		found = False
		while current != None and not found:
			if current.getData() == item:
				found = True
			else:
				current = current.getNext()
		return found
	def remove(self,item):
		current = self.head
		previous = None
		found = False
		while not found:
			if current.getData() == item:
				found = True
			else:
				previous = current
				current = current.getNext()
		if previous == None:
			self.head = current.getNext()
		else:
			previous.setNext(current.getNext())
	
	def printList(self):
		current = self.head
		while current != None:
			print(current.getData())
			print("||")
			print("\/")
			current = current.getNext()
		print("None")
	
	def reverse(self):
		previous = None
		current = self.head
		while current != None:
			next = current.next
			current.next = previous
			previous = current
			current = next
		self.head = previous







myList = LinkedList()
for i in range(10):
	myList.addHead(10-i)

# print (myList.search(19))
# print (myList.size())
# myList.remove(10)
# print (myList.size())
# print("============================")
myList.printList()
print("============================")
myList.reverse()
myList.printList()
