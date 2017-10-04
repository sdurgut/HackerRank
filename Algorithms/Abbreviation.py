##https://www.hackerrank.com/challenges/abbr


def howManyCapitals(foundS):
	capitalNum = 0
	for x in foundS:
		capitalFlag = 0
		for y in x:
			if y.isupper(): 
				capitalFlag = 1
		capitalNum = capitalNum + capitalFlag

	return capitalNum



def istransformable(s1,s2,foundS):
	if len(s1) == len(s2):
		if s1.upper() == s2.upper(): return 'YES'
		else: return 'NO'
	else: 
		myindex = s1.upper().find(s2)
		if myindex < 0 : return 'NO'
		else:
			myPreList = s1[:myindex]
			myList = s1[myindex:myindex+len(s2)]
			myPostList = s1[myindex+len(s2):]
			foundS.append(myList)
			

			#print myPreList, myList, myPostList

			for x in myPreList:
				if x.isupper():
					return 'NO'

			if len(myPostList)<s2:
				for x in myPostList:
					if x.isupper(): return 'NO'


			istransformable(myPostList,s2,foundS)


	print foundS


	if howManyCapitals(foundS) > 1:
		return 'NO'

	return 'YES'









s1 = ['adabcadaBCz']
s2 = ['ABC']




while s1:
	foundS = []
	print istransformable(s1[0],s2[0],foundS)
	del s1[0]
	del s2[0]



