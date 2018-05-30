l1 = [1, 3, 4, 7]
l2 = [0, 2, 5, 6, 8, 9]


def mergeSortedLists(l1,l2):
	result = []
	list1 = l1[:]
	list2 = l2[:]

	while list1 and list2:
		if list1[0]<list2[0]:
			result.append( list1.pop(0) )
		else:
			result.append( list2.pop(0) )

	if list1:
		result.extend(list1)
	else:
		result.extend(list2)

	return result

if __name__ == '__main__':
	print (mergeSortedLists(l1,l2))

