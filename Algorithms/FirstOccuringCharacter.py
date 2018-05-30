input = "abc"

def find(input):
	mySet = set()
	for i in input:
		if i not in mySet:
			mySet.add(i)
		else:
			return i
	return None

print (find(input))