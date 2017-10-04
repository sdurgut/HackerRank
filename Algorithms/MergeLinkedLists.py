

# def MergeLists(headA, headB):
# 	orderedList = Node()

# 	if headA is None:
# 		return headB
# 	if headB is None:
# 		return headA

# 	while headA is not None or headB is not None:
# 		if headA is None:
# 			tmpB = Node(headB.data, None)
# 			orderedList.next = headB
# 			headB = headB.next
# 		elif headB is None:
# 			tmpA = Node(headA.data,None)
# 			orderedList.next = headA
# 			headA = headA.next

# 		elif headA.data <= headB.data:
# 			tmpA = Node(headA.data,None)
# 			orderedList.next = headA
# 			headA = headA.next

# 		else headA.data>headB.data:
# 			tmpB = Node(headB.data,None)
# 			orderedList.next = headB
# 			headB = headB.next

# 	return orderedList

def MergeLists(headA, headB):
	if headA is None:
		return headB
	if headB is None:
		return headA
	if headA.data <= headB.data:
		headA.next = MergeLists(headA.next, headB)
		return headA
	headB.next = MergeLists(headA, headB.next)
	return headB
