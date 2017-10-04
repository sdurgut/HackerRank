from fractions import Fraction
from itertools import combinations
def simplify(nbothOnes,total):
	tmp = Fraction(nbothOnes,total)
	res = str(tmp.numerator) + "/" + str( tmp.denominator )
	return res


def generate(s):
	myList = list(s)
	return list(combinations(myList,2))

def moveWindow(S,K):
	nbothOnes = 0
	total = 2**len(S)
	for i in range(K,len(S)+1):
		sSlice = S[i-K:i]
		list = generate(sSlice)
		print (list)
		for s in list:
			if s[0] =="1" and s[1] == "1":
				nbothOnes +=1


	
	# print ("nbothOnes=",nbothOnes, "total=" ,total)	
	return nbothOnes,total
		



def sherlockProbability(inputValues):
	res = []
	for case in inputValues:
		N = case["NandK"][0]
		K = case["NandK"][1]
		S = case["S"]
		nbothOnes,nOther = moveWindow(S,K)
		print (simplify(nbothOnes,nOther))




if __name__ == "__main__":
	nTestCase = int(input())
	inputValues = []
	for i in range(nTestCase):
		case = {}
		NandK = [int(i) for i in input().strip().split()]
		S = input().strip()
		
		case["NandK"] = NandK
		case["S"] = S
		inputValues.append(case)
	sherlockProbability(inputValues)