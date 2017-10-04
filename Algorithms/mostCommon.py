import operator
def mostCommon(s):
	letters = "abcdefghijklmnopqrstuvwxyz"
	myDict = {}
	for letter in letters:
		myDict[letter] = 0

	

	for letter in s:
		myDict[letter] = myDict[letter] + 1

	myTuple = myDict.items()
	mySortedTuple=sorted(myTuple, key=lambda x: x[0],reverse=False)
	mySortedTuple = sorted(mySortedTuple, key=lambda x: (x[1]), reverse = True)
	

	return mySortedTuple



if __name__ == "__main__":
	# s = "qwertyuiopasdfghjklzxcvbnm"
	s = input().strip()
	mySortedTuple = mostCommon(s)
	
	for i in range(3):
		print (mySortedTuple[i][0], mySortedTuple[i][1])