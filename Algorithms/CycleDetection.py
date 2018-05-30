#https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle/problem
"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
	class Node(object):
		def __init__(self, data = None, next_node = None):
			self.data = data
			self.next = next_node
"""


def has_cycle(head):
	if head is None:
		# print (0)
		return False
	myList = []
	node = head
	while node is not None:
		if node in myList:
			# print (1)
			return True
		else:
			myList.append(node)
		node = node.next
	# print (0)
	return False
