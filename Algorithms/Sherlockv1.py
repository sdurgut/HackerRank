
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

	print(freqList)
	print(letList)
	if len(set(freqList)) == 1:
		return "YES"
	elif len(set(freqList)) > 2:
		return "NO"
	elif len(set(freqList)) == 2:
		freqList.sort()
		if freqList[0] == 1 and freqList[1] != freqList[0]:
			return "YES"
		if abs(freqList[0]-freqList[1]) > 1:
			return "NO"
		elif abs(freqList[len(freqList)-1]-freqList[len(freqList)-2]) > 1:
			return "NO"
		elif freqList[0]==freqList[1] and freqList[len(freqList)-1]==freqList[len(freqList)-2]:
			return "NO"
		else:
			return "YES"




myString = input().strip()
result = isValid(myString)
print(result)


