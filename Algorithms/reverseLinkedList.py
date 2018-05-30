"""
 Reverse a linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
	   self.data = data
	   self.next = next_node

 return back the head of the linked list in the below method.
"""

def Reverse(head):
	curr = head
	prev = None
	while curr is not None:
		next = curr.next
		curr.next = prev
		prev = curr
		curr = next
	return prev

#
# 1->2->3->4->Null
# curr = 1, prev = None, 
# next = 2, <-1, prev = 1, curr 2,  	
# next 3, <-1<-2, prev = 2, curr 3
#
#