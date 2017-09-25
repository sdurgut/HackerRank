from itertools import combinations
def generate(s,K):
	myList = s.split()
	return list(combinations(myList,K))


def calculateProbability(N,s,K):
	myList = s.split()
	combinations = generate(s,K)
	count = 0
	for comb in combinations:
		if 'a' in comb:
			count +=1
	return float(count)/len(combinations)



if __name__ == '__main__':
	N = int(input())
	s = input()
	K = int(input())
	print (calculateProbability(N,s,K))

	
