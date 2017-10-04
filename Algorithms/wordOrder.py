from collections import OrderedDict
def mostCommon(words):
	myDict=OrderedDict()
	for word in words:
		if word not in myDict:
			myDict[word] = 1
		else:
			myDict[word] += 1
	return myDict




if __name__ == "__main__":
	num = input()
	myWordList = []
	for i in range(int(num)):
		s = input()
		s = s.replace('\\n','')
		myWordList.append(s)
	myDict = mostCommon(myWordList)
	print (len(myDict))
	string = ''
	for key, value in myDict.items():
		string = string + str(value) + " "

	print (string.strip())