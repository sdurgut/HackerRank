array = [2,3,4,0,4,5,0,3,2,7,0,7]

def countZeros1(array):
	counter = 0
	for i in array:
		if i == 0:
			counter += 1
	return counter

def countZeros2(array):
	counter = 0
	for i in sorted(array):
		if i != 0:
			return counter
		else:
			counter += 1
	return counter

print(countZeros1(array))
print(sorted(array))
print (array)
print(countZeros2(array))