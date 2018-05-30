
import sys
import collections

def isValid(myString):
	if len(myString)<=1:
		return "YES"

	myDict = collections.OrderedDict()
	for s in myString:
		if s not in myDict:
			myDict[s] = 1
		else:
			myDict[s] += 1

	freqList = []
	letList = []
	for k,v in myDict.items():
		freqList.append(v)
		letList.append(k)
	# use sets
	if len(set(freqList)) == 1:
		return "YES"
	elif len(set(freqList)) > 2:
		return "NO"
	elif len(set(freqList)) == 2:
		freqList.sort()
		if freqList[0] == 1 and freqList[1] != freqList[0]:
			return "YES"
		elif freqList[len(freqList)-1]-freqList[len(freqList)-2] == 1:
			return "YES"
		else:
			return "NO"

myString = input().strip()
result = isValid(myString)
print(result)


